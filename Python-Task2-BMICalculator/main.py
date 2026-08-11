def calculate_bmi(weight, height):
    """Calculate BMI using weight in kilograms and height in meters."""
    return weight / (height ** 2)


def get_bmi_category(bmi):
    """Determine BMI category according to standard BMI ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_bmi_range(category):
    """Return the standard BMI range for the category."""
    ranges = {
        "Underweight": "Below 18.5",
        "Normal": "18.5 - 24.9",
        "Overweight": "25.0 - 29.9",
        "Obese": "30.0 and above"
    }

    return ranges[category]


def get_suggestion(category):
    """Return a general health suggestion."""
    suggestions = {
        "Underweight": "Consider a balanced and nutritious diet.",
        "Normal": "Great! Maintain your healthy lifestyle.",
        "Overweight": "Regular exercise and a balanced diet are recommended.",
        "Obese": "Consider seeking professional healthcare guidance."
    }

    return suggestions[category]


def display_header():
    """Display the application header."""
    print()
    print("+" + "-" * 66 + "+")
    print("|" + " " * 66 + "|")
    print("|" + " " * 23 + "BMI CALCULATOR" + " " * 29 + "|")
    print("|" + " " * 14 + "Python Programming Internship" + " " * 22 + "|")
    print("|" + " " * 66 + "|")
    print("+" + "-" * 66 + "+")


def display_result(name, weight, height, bmi, category):
    """Display the BMI result."""
    bmi_range = get_bmi_range(category)
    suggestion = get_suggestion(category)

    print()
    print("+" + "=" * 66 + "+")
    print("|" + " " * 66 + "|")
    print("|" + " " * 25 + "BMI RESULT" + " " * 31 + "|")
    print("+" + "=" * 66 + "+")

    print(f"|  {'Name':<18}: {name:<44}|")
    print(f"|  {'Weight':<18}: {weight:.2f} kg{' ' * 38}|")
    print(f"|  {'Height':<18}: {height:.2f} m{' ' * 40}|")
    print(f"|  {'BMI Value':<18}: {bmi:.2f}{' ' * 45}|")
    print(f"|  {'BMI Category':<18}: {category:<44}|")
    print(f"|  {'Healthy Range':<18}: {bmi_range:<44}|")

    print("+" + "-" * 66 + "+")
    print("|  HEALTH STATUS" + " " * 51 + "|")
    print("|" + " " * 66 + "|")

    if len(suggestion) <= 64:
        print(f"|  {suggestion:<64}|")
    else:
        print(f"|  {suggestion[:64]:<64}|")
        print(f"|  {suggestion[64:]:<64}|")

    print("+" + "=" * 66 + "+")


def main():
    display_header()

    while True:
        print()
        print("+" + "-" * 66 + "+")
        print("|" + " " * 22 + "ENTER USER DETAILS" + " " * 26 + "|")
        print("+" + "-" * 66 + "+")

        name = input("|  Enter Your Name       : ").strip()

        if not name:
            print("|  Error: Name cannot be empty.")
            print("+" + "-" * 66 + "+")
            continue

        try:
            weight = float(input("|  Enter Weight (kg)     : "))
            height = float(input("|  Enter Height (m)      : "))

        except ValueError:
            print("|  Error: Please enter numeric values only.")
            print("+" + "-" * 66 + "+")
            continue

        if weight <= 0:
            print("|  Error: Weight must be greater than zero.")
            print("+" + "-" * 66 + "+")
            continue

        if height <= 0:
            print("|  Error: Height must be greater than zero.")
            print("+" + "-" * 66 + "+")
            continue

        print("+" + "-" * 66 + "+")

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        display_result(
            name,
            weight,
            height,
            bmi,
            category
        )

        choice = input(
            "\nCalculate another BMI? (Y/N): "
        ).strip().lower()

        if choice != "y":
            print()
            print("+" + "=" * 66 + "+")
            print("|" + " " * 66 + "|")
            print("|" + "        Thank You for Using BMI Calculator!" + " " * 22 + "|")
            print("|" + " " * 66 + "|")
            print("+" + "=" * 66 + "+")
            print()
            break


if __name__ == "__main__":
    main()
