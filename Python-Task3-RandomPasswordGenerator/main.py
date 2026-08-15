import random
import string


def generate_password(length, use_uppercase, use_lowercase,
                      use_numbers, use_symbols):
    """Generate a random password based on selected character types."""

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_numbers:
        character_sets.append(string.digits)

    if use_symbols:
        character_sets.append(string.punctuation)

    password_characters = []

    for character_set in character_sets:
        password_characters.append(random.choice(character_set))

    character_pool = "".join(character_sets)

    while len(password_characters) < length:
        password_characters.append(random.choice(character_pool))

    random.shuffle(password_characters)

    return "".join(password_characters)


def get_yes_no(prompt):
    """Get a valid Y/N response from the user."""

    while True:
        answer = input(prompt).strip().lower()

        if answer == "y":
            return True

        elif answer == "n":
            return False

        else:
            print("|  Error: Please enter Y or N.")


def display_header():
    """Display the application header."""

    print()
    print("+" + "-" * 66 + "+")
    print("|" + " " * 66 + "|")
    print("|" + " " * 18 + "RANDOM PASSWORD GENERATOR" + " " * 23 + "|")
    print("|" + " " * 13 + "Python Programming Internship" + " " * 24 + "|")
    print("|" + " " * 66 + "|")
    print("+" + "-" * 66 + "+")


def display_settings(length, uppercase, lowercase,
                     numbers, symbols):
    """Display the selected password settings."""

    print()
    print("+" + "-" * 66 + "+")
    print("|" + " " * 22 + "PASSWORD SETTINGS" + " " * 27 + "|")
    print("+" + "-" * 66 + "+")

    print(f"|  {'Password Length':<22}: {length:<40}|")
    print(f"|  {'Uppercase Letters':<22}: "
          f"{'Yes' if uppercase else 'No':<40}|")
    print(f"|  {'Lowercase Letters':<22}: "
          f"{'Yes' if lowercase else 'No':<40}|")
    print(f"|  {'Numbers':<22}: "
          f"{'Yes' if numbers else 'No':<40}|")
    print(f"|  {'Symbols':<22}: "
          f"{'Yes' if symbols else 'No':<40}|")

    print("+" + "-" * 66 + "+")


def display_password(password):
    """Display the generated password."""

    print()
    print("+" + "=" * 66 + "+")
    print("|" + " " * 66 + "|")
    print("|" + " " * 22 + "GENERATED PASSWORD" + " " * 26 + "|")
    print("|" + " " * 66 + "|")
    print("|" + f"{password:^66}" + "|")
    print("|" + " " * 66 + "|")
    print("+" + "=" * 66 + "+")


def main():

    display_header()

    while True:

        print()
        print("+" + "-" * 66 + "+")
        print("|" + " " * 20 + "PASSWORD CONFIGURATION" + " " * 23 + "|")
        print("+" + "-" * 66 + "+")

        while True:

            try:
                length = int(
                    input("|  Enter Password Length (minimum 8): ")
                )

                if length < 8:
                    print(
                        "|  Error: Password length must be at least 8."
                    )
                    continue

                break

            except ValueError:
                print(
                    "|  Error: Please enter a valid whole number."
                )

        print("|")
        print("|  Select Character Types")
        print("|")

        use_uppercase = get_yes_no(
            "|  Include Uppercase Letters? (Y/N): "
        )

        use_lowercase = get_yes_no(
            "|  Include Lowercase Letters? (Y/N): "
        )

        use_numbers = get_yes_no(
            "|  Include Numbers? (Y/N): "
        )

        use_symbols = get_yes_no(
            "|  Include Symbols? (Y/N): "
        )

        selected_types = sum([
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        ])

        if selected_types < 2:

            print()
            print(
                "|  Error: Please select at least two character types."
            )
            print("+" + "-" * 66 + "+")
            continue

        display_settings(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        )

        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_symbols
        )

        display_password(password)

        print()

        generate_again = get_yes_no(
            "Generate another password? (Y/N): "
        )

        if not generate_again:

            print()
            print("+" + "=" * 66 + "+")
            print("|" + " " * 66 + "|")
            print("|" + "       Thank You for Using Password Generator!"
                  + " " * 18 + "|")
            print("|" + " " * 66 + "|")
            print("+" + "=" * 66 + "+")
            print()

            break


if __name__ == "__main__":
    main()