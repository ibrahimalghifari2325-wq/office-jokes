"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one line about office life (under 200 characters) to /output/entry.txt.
"""

import os

JOKE = "I put 'proficient in Excel' on my CV, which in office terms means I can make a spreadsheet cry and a pivot table confess."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
