"""
Hängt UUIDs an eine Basis-URL an.
"""

class URLBuilder:
    """Hängt UUIDs an eine Basis-URL."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def build(self, uuid_value: str) -> str:
        return f"{self.base_url}/qr_id={uuid_value}"

    def build_all(self, uuids: list[str]) -> list[tuple[int, str, str]]:
        """Gibt eine Liste von (nummer,uuid, url)-Tupeln zurück."""
        return [
        (nummer, uuid_value, self.build(uuid_value))
        for nummer, uuid_value in enumerate(uuids, start=1)
    ]
