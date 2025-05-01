# Implement the Python code using the `openai` library to create the assistant.
# Start with a system prompt for the chat completion API.
# Send a static message and receive a response from the API.
# Show the chat completion message.
import json
import os
import openai

from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://litellm.aks-hs-prod.int.hyperskill.org/"
)

def calculate_token_cost(model,chat_completion):
    input_tokens_cost = chat_completion.usage.prompt_tokens * MODEL["input_cost"]
    output_tokens_cost = chat_completion.usage.completion_tokens * MODEL["output_cost"]
    return input_tokens_cost + output_tokens_cost

MODEL = {"input_cost": 0.0003 / 1000, "output_cost": 0.0012 / 1000}

def end_conversation(indication):
    if indication.lower() == "end conversation":
        return "None"

functions_list = [
    {
        "type": "function",
        "function": {
            "name": "end_conversation",
            "description": "End the conversation with a final response",
            "parameters": {
                "type": "object",
                "properties": {
                    "indication":{
                        "type": "string",
                        "description": "End conversation",
                    }
                },
                "required": ["indication"],
            },
        },
    }
]

def chat_content(messages):
    return client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.5,
    tools=functions_list,
    tool_choice="auto"
)

prompt = input("Enter a message:")

messages = [{"role": "user", "content": prompt}]

chat_completion = chat_content(messages)
message = chat_completion.choices[0].message

total_cost = calculate_token_cost("gpt-4o-mini", chat_completion)

while prompt != "End conversation":
    print("You: " + prompt)
    print("Assistant: " + message.content)
    print(f'Cost: ${total_cost:.8f}\n')
    prompt = input("Enter a message:")
    messages = [{"role": "user", "content": prompt}]

    chat_completion = chat_content(messages)
    message = chat_completion.choices[0].message

    total_cost = calculate_token_cost("gpt-4o-mini", chat_completion)

if message.tool_calls:
    tool_call = message.tool_calls[0]
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)
    function_response = end_conversation(**function_args)

    messages.append({"tool_call_id": tool_call.id,
                     "role": "tool",
                     "name": function_name,
                     "content": function_response
                     })

    print(tool_call.id)
    print("You: " + prompt)
    print(f'Assistant: {function_response}')
    print(f'Cost: ${total_cost:.8f}')






