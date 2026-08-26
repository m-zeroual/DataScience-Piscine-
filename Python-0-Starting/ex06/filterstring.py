import sys


def main():
    """Print words whose length is greater than the given number."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        number = int(sys.argv[2])

        if not isinstance(text, str) or not isinstance(number, int):
            raise AssertionError("the arguments are bad")

        words = text.split(" ")
        result = [word for word in words if (lambda x: len(x) > number)(word)]

        print(result)

    except (ValueError, AssertionError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
