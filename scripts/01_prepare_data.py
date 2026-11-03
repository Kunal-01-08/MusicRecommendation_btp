"""Prepare dataset interface stub."""
import argparse

def main() -> None:
    """Parse config and prepare data."""
    parser = argparse.ArgumentParser(); parser.add_argument("--config", required=True); parser.parse_args()
    raise NotImplementedError("TODO: implement data preparation")

if __name__ == "__main__": main()
