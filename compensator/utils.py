# compensator/utils.py

def hex_to_rgb(hex_color: str) -> list[float]:
    """Convert '#RRGGBB' to [r, g, b] in 0–1 range."""
    return [int(hex_color[i : i + 2], 16) / 255.0 for i in (1, 3, 5)]


def rgb_to_hex(rgb: list[float]) -> str:
    """Convert [r, g, b] in 0–1 range to '#RRGGBB'."""
    def clamp(x):
        return max(0, min(int(round(x * 255)), 255))
    return "#" + "".join(f"{clamp(c):02X}" for c in rgb)
