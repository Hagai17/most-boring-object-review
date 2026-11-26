"""Entry for make.fun: The Most Boring Object, Reviewed in One Line.

Writes one funny, true review line about a nail clipper to
/output/entry.txt and prints it.

The joke is the object's own behaviour: a nail clipper trims neatly
and in silence, then fires a clipping across the room, where a bare
foot finds it days later. The line is built in three beats — the
quiet trim, the launch, and the bare foot's report.

Why this line (duel record in candidates.md): the brief rewards a
laugh at a real, recognisable detail of the object, truth that
arrives as recognition, and last words that sharpen. Of 247 live
field entries sampled, none reviewed a nail clipper; the crowded
lanes (doorstop, rubber band, dustpan's last line of dust) were
avoided. This draft beat twelve others in both-orders duels under
the published brief, and beat or levelled the strongest sampled
field lines (cable tie, coaster, USB plug, bookmark, toothpick).
"""

import os

BEATS = [
    "The nail clipper trims all ten nails in silence,",
    "then fires the last clipping across the room",
    "— a bare foot will find it next week and file the report.",
]

LINE = " ".join(BEATS)


def main() -> None:
    # Gate self-check: UTF-8 text of 1-200 characters, a single line,
    # not only white space.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
