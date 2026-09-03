import os


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while iterating over a range."""
    total = len(lst)
    width = os.get_terminal_size().columns

    for i, elem in enumerate(lst, 1):
        percent = int(i * 100 / total)

        prefix = f"\r{percent:3d}%|"
        suffix = f"| {i}/{total}"

        bar_size = width - len(prefix) - len(suffix)
        filled = int(bar_size * i / total)

        bar = "█" * filled + " " * (bar_size - filled)

        os.write(1, f"{prefix}{bar}{suffix}".encode())

        yield elem

    os.write(1, b"\n")
