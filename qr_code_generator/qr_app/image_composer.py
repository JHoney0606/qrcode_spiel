"""
Fügt einen QR-Code an einer festen Position in ein Vorlagenbild ein
und speichert das Ergebnis mit der UUID als Dateinamen.
"""

from pathlib import Path

from PIL import Image


class ImageComposer:

    def __init__(self, source_image_path: Path, output_dir: Path, position: tuple[int, int]):
        self.source_image_path = source_image_path
        self.output_dir = output_dir
        self.position = position
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def compose(self, qr_image: Image.Image, uuid_value: str) -> Path:
        base = Image.open(self.source_image_path).convert("RGB")
        base.paste(qr_image, self.position)
        out_path = self.output_dir / f"{uuid_value}.png"
        base.save(out_path)
        return out_path
