"""Write the final plan to /output/entry.txt.

Pure stdlib, no network, deterministic: the same bytes on every run.
"""

PLAN = (
    "Enter free make.fun coding bounties, paid in USDC on Solana \u2014 pots "
    "$50\u2013$1,666, top 10\u201320 paid. Spend the $100 on API credits. "
    "Day 1: take the smallest open bounty, build, test, submit. "
    "Enter 1\u20132 daily for 30 days. Likely: a few paid places, "
    "$300\u2013$600, the $100 never staked."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
