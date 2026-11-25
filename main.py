"""One Line, One Laugh — make.fun entry.

Writes a single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
"""

import os
from pathlib import Path

LINE = "My smartwatch congratulated me on burning 400 calories, then watched me eat a whole pizza and quietly updated my funeral playlist."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    assert entry_path.read_text(encoding="utf-8") == LINE
    assert 1 <= len(LINE) <= 140
    assert "\n" not in LINE and LINE.strip() == LINE  # one line, no padding
    print(LINE)


if __name__ == "__main__":
    main()
