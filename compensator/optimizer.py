# compensator/optimizer.py

from scipy.optimize import minimize
from compensator.perception import simulate_print_perception
from compensator.utils import hex_to_rgb, rgb_to_hex

def compensate_hex_for_print(original_hex: str) -> str:
    """Find a new HEX that, when printed, appears like original_hex on-screen."""
    # 1) Get the target appearance under print conditions
    target = simulate_print_perception(original_hex)

    # 2) Define the objective: squared difference in J, C, and hue
    def objective(rgb):
        # Clip rgb to [0,1]
        rgb = [max(0, min(1.0, c)) for c in rgb]
        candidate_hex = rgb_to_hex(rgb)
        cam = simulate_print_perception(candidate_hex)

        dJ = cam["J"] - target["J"]
        dC = cam["C"] - target["C"]
        dh = abs(cam["h"] - target["h"])
        dh = min(dh, 360 - dh) / 180  # normalize hue error

        return dJ**2 + dC**2 + dh**2

    # 3) Initial guess: lighten original by 20%
    orig_rgb = hex_to_rgb(original_hex)
    x0 = [min(1.0, c * 1.2) for c in orig_rgb]

    # 4) Bounds for each channel
    bounds = [(0.0, 1.0)] * 3

    # 5) Run the optimizer
    result = minimize(objective, x0, bounds=bounds, method="L-BFGS-B")

    # 6) Convert result back to HEX
    best_rgb = result.x.tolist()
    return rgb_to_hex(best_rgb)
