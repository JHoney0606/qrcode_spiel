"""
Erstellt QR-Code-Bilder aus URLs.
"""

import qrcode
from PIL import Image


class QRCodeGenerator:

    def __init__(self, size: int):
        self.size = size

    def generate(self, url: str) -> Image.Image:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        return img.resize((self.size, self.size), Image.LANCZOS)
