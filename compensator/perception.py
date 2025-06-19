# compensator/perception.py

import numpy as np
from colour import sRGB_to_XYZ
from colour.appearance.ciecam02 import XYZ_to_CIECAM02

def simulate_print_perception(hex_color: str) -> dict:
    # 1) HEX → normalized sRGB
    rgb = [int(hex_color[i : i + 2], 16) / 255.0 for i in (1, 3, 5)]

    # 2) sRGB (D65) → XYZ
    xyz = sRGB_to_XYZ(rgb)

    # 3) Define print-viewing conditions
    XYZ_w = sRGB_to_XYZ([1.0, 1.0, 1.0])  # paper white
    L_A = 318.31                          # ambient light (cd/m²)
    Y_b = 20.0                            # background reflectance

    # 4) Compute CIECAM02 appearance
    cam = XYZ_to_CIECAM02(xyz, XYZ_w, L_A, Y_b)

    return {
        "J": cam.J,   # Lightness
        "C": cam.C,   # Chroma
        "h": cam.h    # Hue angle
    }
