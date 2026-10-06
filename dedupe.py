"""Core logic for the duplicate line remover (pure Python, no dependencies)."""


def remove_duplicates(text, ignore_case=False, trim_spaces=False, sort_az=False):
    """Remove duplicate lines from `text`.

    Returns (result_text, removed_count, kept_count).
    The first occurrence of each line is kept, in its original order,
    unless `sort_az` is True.
    """
    lines = text.splitlines()
    if trim_spaces:
        lines = [line.strip() for line in lines]

    seen = set()
    unique = []
    for line in lines:
        key = line.casefold() if ignore_case else line
        if key not in seen:
            seen.add(key)
            unique.append(line)

    if sort_az:
        unique.sort(key=lambda s: (s.casefold(), s))

    removed = len(lines) - len(unique)
    return "\n".join(unique), removed, len(unique)
