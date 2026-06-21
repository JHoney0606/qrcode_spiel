"""
Orchestriert alle Komponenten zu einem durchgängigen Ablauf:
UUIDs generieren -> URLs bauen -> protokollieren -> QR-Codes erzeugen -> in Vorlagenbild einsetzen.
"""

from .config import Config
from .uuid_generator import UUIDGenerator
from .url_builder import URLBuilder
from .result_logger import ResultLogger
from .qr_code_generator import QRCodeGenerator
from .image_composer import ImageComposer


class QRPipeline:

    def __init__(self, config: Config):
        self.config = config
        self.uuid_generator = UUIDGenerator()
        self.url_builder = URLBuilder(config.base_url)
        self.logger = ResultLogger(config.log_file_path)
        self.qr_generator = QRCodeGenerator(config.qr_size)
        self.composer = ImageComposer(
            config.source_image_path,
            config.output_image_dir,
            config.qr_position,
        )

    def run(self) -> None:
        print(f"[Pipeline] Starte mit {self.config.uuid_count} UUIDs …")

        # 1. UUIDs generieren
        uuids = self.uuid_generator.generate(self.config.uuid_count)
        print("uuids")
        # 2. URLs bauen
        entries: list[tuple[int, str, str]] = self.url_builder.build_all(uuids)
        print("entries")
        # 3. Ergebnisse protokollieren
        self.logger.log(entries)
        print("log")
        # 4. Pro Eintrag: QR-Code erstellen & ins Bild einsetzen
        for nummer, uuid_value, url in entries:
            qr_img = self.qr_generator.generate(url, nummer)
            out_path = self.composer.compose(qr_img, uuid_value)
            print(f"[Compose]{nummer}: {uuid_value} → {out_path}")
        print("bilder")
        print("[Pipeline] Fertig.")
