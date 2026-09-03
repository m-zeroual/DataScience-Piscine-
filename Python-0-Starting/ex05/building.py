import sys


def count_characters(text):
    """Count upper, lower, punctuation, spaces and digits."""
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            punctuation += 1

    return upper, lower, punctuation, spaces, digits


def ft_readline(prompt: str) -> str:
    """Read input character by character until newline or EOF."""
    if prompt:
        print(prompt)
    text = ""

    while True:
        char = sys.stdin.read(1)
        if char == "":
            break

        text += char
        if char == "\n":
            break
    return text


def main():
    """Read a string and display its character statistics."""
    try:
        if len(sys.argv) == 1:

            text = ft_readline("What is the text to count?")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("more than one argument is provided")

        upper, lower, punctuation, spaces, digits = count_characters(text)

        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
