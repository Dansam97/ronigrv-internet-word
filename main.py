import os

WORD = "Procrastination"

# Gate from competition.yaml: entry.txt must be UTF-8 text of 1-30
# characters, not only white space, and a single word.
MIN_LEN = 1
MAX_LEN = 30


def validate(word):
    if not word or word != word.strip():
        raise ValueError("entry word must not be empty or padded")
    if not MIN_LEN <= len(word) <= MAX_LEN:
        raise ValueError("entry word must be 1-30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word")


def main():
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
