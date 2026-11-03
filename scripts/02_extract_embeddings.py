"""Embedding extraction interface stub."""
import argparse

def main() -> None:
    """Parse config and extract embeddings."""
    parser = argparse.ArgumentParser(); parser.add_argument("--config", required=True); parser.parse_args()
    raise NotImplementedError("TODO: implement embedding extraction")

if __name__ == "__main__": main()
