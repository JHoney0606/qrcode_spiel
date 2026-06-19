"""
Protokolliert die generierten UUID/URL-Paare in einer Textdatei.
"""

from pathlib import Path


class ResultLogger:
    def __init__(self, log_file_path: Path):
        self.log_file_path = log_file_path

    def log(self, entries: list[tuple[str, str]]) -> None:
        self.log_file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_file_path.open("w", encoding="utf-8") as f:
            f.write("UUID;URL\n")
            for uuid_value, url in entries:
                f.write(f"{uuid_value};{url}\n")
        print(f"[Logger] {len(entries)} Einträge gespeichert → {self.log_file_path}")
