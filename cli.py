# cli.py

import sys
from compensator.perception import simulate_print_perception
from compensator.optimizer import compensate_hex_for_print

def main():
    if len(sys.argv) != 2:
        print("Usage: python cli.py \"#RRGGBB\"")
        return

    orig_hex = sys.argv[1]
    # 1) Show how original looks in print
    cam = simulate_print_perception(orig_hex)
    print("Original perceived in print:")
    print(f"  J={cam['J']:.2f}, C={cam['C']:.2f}, h={cam['h']:.2f}")

    # 2) Compute compensated HEX
    new_hex = compensate_hex_for_print(orig_hex)
    print(f"\nUse this HEX in your PDF to match on-screen color:")
    print(f"  {new_hex}")

if __name__ == "__main__":
    main()
