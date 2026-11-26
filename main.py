"""One-line entry: The Funniest Excuse for Skipping a Meeting."""

LINE = "Sorry, I can't make the meeting — my calendar and I are in couples therapy and it says I need boundaries."

MAX_CHARS = 200


def main() -> None:
    if len(LINE) > MAX_CHARS:
        raise SystemExit(f"line is {len(LINE)} chars, cap is {MAX_CHARS}")
    print(LINE)


if __name__ == "__main__":
    main()
