"""Evaluation interface stub."""
import argparse

def main() -> None:
    """Parse config and evaluate model."""
    parser = argparse.ArgumentParser(); parser.add_argument("--config", required=True); parser.parse_args()
    raise NotImplementedError("TODO: implement evaluation")

if __name__ == "__main__": main()
