input_angles = []
for _ in range(1, 4):
    try:
        angle = float(input())
        if angle > 0:
            input_angles.append(angle)
        else:
            angle = float(input())
    except EOFError:
        input_angles.append(0)
angles_sum = sum(input_angles)
if angles_sum == 180:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")


