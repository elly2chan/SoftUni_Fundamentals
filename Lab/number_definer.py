floating_number = float(input())

if floating_number == 0:
    print("zero")
elif floating_number > 0:
    if floating_number < 1:
        print("small positive")
    elif floating_number > 1_000_000:
        print("large positive")
    else:
        print("positive")
else:
    if floating_number > -1:
        print("small negative")
    elif floating_number < -1_000_000:
        print("large negative")
    else:
        print("negative")