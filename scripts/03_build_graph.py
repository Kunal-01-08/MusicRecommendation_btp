"""Graph construction interface stub."""
import argparse

def main() -> None:
    """Parse config and build graph."""
    parser = argparse.ArgumentParser(); parser.add_argument("--config", required=True); parser.parse_args()
    raise NotImplementedError("TODO: implement graph construction")

if __name__ == "__main__": main()
