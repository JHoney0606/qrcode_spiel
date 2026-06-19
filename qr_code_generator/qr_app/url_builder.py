"""
Hängt UUIDs an eine Basis-URL an.
"""

class URLBuilder:
    """Hängt UUIDs an eine Basis-URL."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def build(self, uuid_value: str) -> str:
        return f"{self.base_url}{uuid_value}"

    def build_all(self, uuids: list[str]) -> list[tuple[str, str]]:
        """Gibt eine Liste von (uuid, url)-Paaren zurück."""
        return [(u, self.build(u)) for u in uuids]
