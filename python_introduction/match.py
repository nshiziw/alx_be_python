day = input("Enter a day of the week (Monday-Sunday): ").lower()
match day:
    case "monday":
        print("Ugh, Mondays...")
    case "tuesday":
        print("Just another work day!")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there...")
    case "friday":
        print("Weekend loading...")
    case "saturday" | "sunday":
        print("Weekend vibes!")
    case _:
        print("Invalid day entered!")


value = input("Enter a value (number, float or string)")

match value:
    case int():
        print("The value is an integer.", value)
    case float():
        print("The value is a float.", value)
    case str():
        print("The value is a string.", value)
    case _:
        print("Invalid datatype entered!")