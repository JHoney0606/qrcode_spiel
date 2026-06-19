"""
Lädt alle konfigurierbaren Parameter aus einer INI-Datei.
"""

import configparser
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Config:
    uuid_count: int
    base_url: str
    log_file_path: Path
    source_image_path: Path
    output_image_dir: Path
    qr_position: tuple[int, int]
    qr_size: int

    @classmethod
    def from_file(cls, config_path: str = "config.ini") -> "Config":
        parser = configparser.ConfigParser()
        if not parser.read(config_path):
            raise FileNotFoundError(f"Config-Datei nicht gefunden: {config_path}")

        return cls(
            uuid_count=parser.getint("general", "uuid_count"),
            base_url=parser.get("general", "base_url"),
            log_file_path=Path(parser.get("logging", "log_file_path")),
            source_image_path=Path(parser.get("image", "source_image_path")),
            output_image_dir=Path(parser.get("image", "output_image_dir")),
            qr_position=(
                parser.getint("image", "qr_position_x"),
                parser.getint("image", "qr_position_y"),
            ),
            qr_size=parser.getint("image", "qr_size"),
        )
