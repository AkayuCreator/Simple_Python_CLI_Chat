def categorize_items(categories, items):
    categorized_dict = {}
    for category in set(categories):
        categorized_dict[category] = [item for item, cat in zip(items, categories) if cat == category]
    return categorized_dict
