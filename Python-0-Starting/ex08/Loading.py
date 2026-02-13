import os


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    for i, item in enumerate(lst, 1):
        yield item
        width = os.get_terminal_size().columns
        reserved = 40
        bar_length = width - reserved if width > reserved else 10
        progress = i / total
        filled = int(bar_length * progress)
        bar = "█" * filled + " " * (bar_length - filled)
        percent = int(progress * 100)
        print(f"\r{percent:3d}%|{bar}| {i}/{total}", end="", flush=True)
    print()
