"""Training interface stub."""
import argparse

def main() -> None:
    """Parse config and train model."""
    parser = argparse.ArgumentParser(); parser.add_argument("--config", required=True); parser.parse_args()
    raise NotImplementedError("TODO: implement training")

if __name__ == "__main__": main()
