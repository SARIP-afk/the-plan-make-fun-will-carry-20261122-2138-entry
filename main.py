"""Write the final plan to /output/entry.txt.

Pure stdlib, no network, deterministic: the same bytes on every run.
The plan text is validated against the 280-character limit before
anything is written, so an out-of-range plan fails loudly instead
of silently submitting a truncated or oversized entry.

Strategy summary (the 30-day loop the plan encodes):
  * Day 1 takes the smallest open bounty so the first submission lands
    fast, before the leaderboard cutoff moves away.
  * Afterwards the agent enters 1-2 bounties a day for 30 days, always
    free ones, so volume compounds without ever risking the $100.
  * The $100 goes to API credits only -- it funds the work, it is never
    staked, bet, or spent on entry fees, so the downside is bounded at
    the cost of credits while the upside is a few paid placements.

Validation matters because the entry is graded on the exact bytes the
program writes: a plan that drifts over 280 characters, or gains a
trailing newline, would be a different submission. validate_plan()
enforces the length and write_plan() writes the text verbatim, so
every run reproduces the same 274 code points.
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


def summarize_plan(text: str) -> dict:
    """Return a small summary of the plan for logging or inspection.

    Pure function: it reads the text and counts, it never touches the
    plan itself, so the output bytes are unaffected.
    """
    words = text.split()
    return {
        "chars": len(text),
        "words": len(words),
        "days": 30,
        "daily_entries": "1-2",
        "capital_at_risk": "$0",
    }


def validate_plan(text: str) -> None:
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"plan length {len(text)} outside {MIN_CHARS}-{MAX_CHARS} chars"
    )


def write_plan(text: str, path: str = OUTPUT_PATH) -> None:
    import os

    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    except OSError as exc:
        raise RuntimeError(f"cannot create output directory for {path}: {exc}") from exc
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
    except OSError as exc:
        raise RuntimeError(f"cannot write plan to {path}: {exc}") from exc


def main() -> None:
    validate_plan(PLAN)
    summary = summarize_plan(PLAN)
    assert summary["chars"] == len(PLAN), "summary disagrees with plan length"
    write_plan(PLAN)


if __name__ == "__main__":
    main()
