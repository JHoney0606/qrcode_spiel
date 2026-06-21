"""
Erstellt QR-Code-Bilder aus URLs.
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont


class QRCodeGenerator:

    def __init__(self, size: int):
        self.size = size

    def generate(self, url: str, nummer: int) -> Image.Image:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        img = img.resize((self.size, self.size), Image.Resampling.NEAREST)

        img = self.zahl_einfuegen(img, nummer)
        return img

    def zahl_einfuegen(self, img: Image.Image, nummer: int) -> Image.Image:
        
        # Zahl in QR-Code einfügen
        draw = ImageDraw.Draw(img)
        text = str(nummer)

        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except OSError:
            font = ImageFont.load_default()
        padding = 10
        center_x = self.size // 2
        center_y = self.size // 2

        text_box = draw.textbbox(
            (center_x, center_y),
            text,
            font=font,
            anchor="mm",
        )

        background = (
            text_box[0] - padding,
            text_box[1] - padding,
            text_box[2] + padding,
            text_box[3] + padding,
        )

        draw.rectangle(
            background,
            fill="white",
            outline="black",
            width=2,
        )

        draw.text(
            (center_x, center_y),
            text,
            fill="black",
            font=font,
            anchor="mm",
        )

        return img
