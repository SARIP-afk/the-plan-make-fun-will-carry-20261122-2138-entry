"""Write the final plan to /output/entry.txt.

Pure stdlib, no network, deterministic: the same bytes on every run.
The plan text is validated against the 280-character limit before
anything is written, so an out-of-range plan fails loudly instead
of silently submitting a truncated or oversized entry.
"""

MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"

PLAN = (
    "Enter free make.fun coding bounties, paid in USDC on Solana \u2014 pots "
    "$50\u2013$1,666, top 10\u201320 paid. Spend the $100 on API credits. "
    "Day 1: take the smallest open bounty, build, test, submit. "
    "Enter 1\u20132 daily for 30 days. Likely: a few paid places, "
    "$300\u2013$600, the $100 never staked."
)


def validate_plan(text: str) -> None:
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"plan length {len(text)} outside {MIN_CHARS}-{MAX_CHARS} chars"
    )


def write_plan(text: str, path: str = OUTPUT_PATH) -> None:
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    validate_plan(PLAN)
    write_plan(PLAN)


if __name__ == "__main__":
    main()
