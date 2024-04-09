path = "books/frankenstein.txt"
with open(path) as f:
    file_contents = f.read()
    letter_counts = {}

    for c in file_contents:
        lowered = c.lower()

        if not lowered.isalpha():
            continue

        if lowered in letter_counts:
            letter_counts[lowered] += 1
        else:
            letter_counts[lowered] = 1

    print(f"--- Begin report of {path} ---")
    print("")

    sorted_keys = sorted(letter_counts.keys())

    for letter in sorted_keys:
        print(f"The '{letter}' character was found {letter_counts[letter]} times")

    print("--- End Report ---")
