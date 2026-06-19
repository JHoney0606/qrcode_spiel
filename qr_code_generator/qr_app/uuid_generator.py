"""
Erzeugt zufällige UUIDs.
"""

import uuid


class UUIDGenerator:
    """Erzeugt eine Liste zufälliger UUIDs (Version 4)."""

    def generate(self, count: int) -> list[str]:
        return [str(uuid.uuid4()) for _ in range(count)]
