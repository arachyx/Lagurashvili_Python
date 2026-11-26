
"""Andersen QA Automation Technical Task"""


def get_integer(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print(f"'{user_input}' is not a valid number. Try again: ")


def get_integer_array(prompt: str) -> list[int]:
    while True:
        raw_input = input(prompt).replace(",", " ")
        tokens = raw_input.split()

        if not tokens:
            print("Invalid input. Enter at least one number: ")
            continue

        try:
            return [int(token) for token in tokens]
        except ValueError:
            print("Invalid input. Enter numbers separated by spaces or commas: ")


def check_number(number: int) -> str | None:
    return "Hello" if number > 7 else None


def check_name(name: str) -> str:
    return "Hello, John" if name.strip().upper() == "JOHN" else "There is no such name"


def get_multiples_of_three(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 3 == 0]


def main() -> None:
    # 1. number check (> 7)
    number = get_integer("Enter a number: ")
    print(check_number(number))

    # 2. name check ("John")
    name = input("\nEnter a name: ")
    print(check_name(name))

    # 3. array multiples of 3
    numbers = get_integer_array("\nEnter numbers separated by spaces or commas: ")
    print(get_multiples_of_three(numbers))


if __name__ == "__main__":
    main()