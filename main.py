import os

POEM = (
    "I keep a spare key under the mat\n"
    "for the asking hand.\n"
    "Knock once, and the door is yours —\n"
    "not opened for you, but by you.\n"
    "I hold the key. You hold the knock.\n"
    "Between us, the hinge learns\n"
    "how light a yes can be\n"
    "when it is given, not taken."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
