# Task 2

OPEN_TO_CLOSE = {"(": ")", "[": "]", "{": "}"}
CLOSE_TO_OPEN = {")": "(", "]": "[", "}": "{"}
VALID_BRACKETS = set(OPEN_TO_CLOSE) | set(CLOSE_TO_OPEN)


def get_bracket_sequence(prompt: str) -> str:
    while True:
        sequence = input(prompt).strip()
        if not sequence:
            print("Please enter a non-empty bracket sequence.")
            continue

        invalid_chars = sorted({char for char in sequence if char not in VALID_BRACKETS})
        if invalid_chars:
            print(f"Invalid characters found: {invalid_chars}. Please use only (), [], {{}}.")
            continue

        return sequence


def analyze_bracket_sequence(sequence: str) -> tuple[bool, list[str], str]:

    stack: list[tuple[int, str]] = []
    errors: list[str] = []
    corrected_chars: list[str] = list(sequence)

    for index, char in enumerate(sequence):
        if char in OPEN_TO_CLOSE:
            stack.append((index, char))
        elif char in CLOSE_TO_OPEN:
            if not stack:
                expected_open = CLOSE_TO_OPEN[char]
                errors.append(
                    f"Index {index}: Unexpected closing '{char}' with no matching '{expected_open}'."
                )
                corrected_chars[index] = ""
            else:
                open_index, open_char = stack.pop()
                expected_close = OPEN_TO_CLOSE[open_char]
                if char != expected_close:
                    errors.append(
                        f"Index {index}: Found '{char}', expected '{expected_close}' "
                        f"to match '{open_char}' at index {open_index}."
                    )
                    corrected_chars[index] = expected_close

    while stack:
        open_index, open_char = stack.pop()
        expected_close = OPEN_TO_CLOSE[open_char]
        errors.append(
            f"Index {open_index}: Unclosed '{open_char}', missing '{expected_close}'."
        )
        corrected_chars.append(expected_close)

    is_valid = len(errors) == 0
    corrected_sequence = "".join(corrected_chars)
    return is_valid, errors, corrected_sequence


def check_bracket_sequence(sequence: str) -> None:
    is_valid, errors, corrected = analyze_bracket_sequence(sequence)

    print(f"\nInput sequence: {sequence}")
    if is_valid:
        print("Can this sequence be considered correct? Yes.")
    else:
        print("Can this sequence be considered correct? No.")
        print("Errors found:")
        for error in errors:
            print(f"  - {error}")
        print(f"Suggested corrected sequence: {corrected}")



    # default example from the task
    # as well as an interactive user-provided sequence
def main() -> None:
    default_sequence = "[((())()(())]]"
    check_bracket_sequence(default_sequence)

    user_sequence = get_bracket_sequence("Enter a bracket sequence to validate: ")
    check_bracket_sequence(user_sequence)


if __name__ == "__main__":
    main()