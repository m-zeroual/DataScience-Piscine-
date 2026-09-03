import sys


def main():
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")

        text = sys.argv[1].upper()

        for char in text:
            if char == " " or char.isalnum():
                continue
            raise AssertionError("the arguments are bad")

        print(" ".join(NESTED_MORSE[char] for char in text))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
