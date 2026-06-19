"""
Aufruf:
    python main.py [pfad/zur/config.ini]
"""

import sys

from qr_app.config import Config
from qr_app.pipeline import QRPipeline


def main() -> None:
    config_path = sys.argv[1] if len(sys.argv) > 1 else "config.ini"
    config = Config.from_file(config_path)
    pipeline = QRPipeline(config)
    pipeline.run()


if __name__ == "__main__":
    main()
