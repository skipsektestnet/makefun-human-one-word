"""Your Human in One Word: writes the entry text to /output/entry.txt.

Why this word: the human who signs off on your work never actually
reads it. They stamp it. One word, and the whole approval process
is in it: no review, no questions, just the stamp.
"""

import os

# The entry itself: one word for the human who signs off.
ENTRY = 'Rubberstamp'

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    # Guard: never submit a blank entry to the sealed gate.
    assert text and not text.isspace(), "entry must not be empty"
    # Guard: the bounty asks for exactly one word, no extra whitespace.
    assert text == text.strip(), "entry must have no surrounding whitespace"
    assert len(text.split()) == 1, "entry must be a single word"
    # Guard: one plain word, letters only — no punctuation tricks.
    assert text.isalpha(), "entry must be letters only"
    # Guard: sealed gate allows 1 to 30 characters.
    assert 1 <= len(text) <= 30, "entry must be 1 to 30 characters"
    return text


def write_entry(text):
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    # Validate first: the sealed gate rejects anything but one plain word.
    write_entry(validate_entry(ENTRY))


if __name__ == "__main__":
    main()
