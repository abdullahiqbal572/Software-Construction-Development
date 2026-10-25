def validate_mark(mark):
    while mark < 0 or mark > 100:
        print("Invalid marks. Enter 0-100.")
        mark = float(input("Enter marks again: "))
    return mark