.PHONY: setup lint test embeddings graph train eval
setup:
	python -m pip install -e ".[dev]"
lint:
	ruff check .
test:
	pytest -q
embeddings:
	python scripts/02_extract_embeddings.py --config configs/audio.yaml
graph:
	python scripts/03_build_graph.py --config configs/graph.yaml
train:
	python scripts/04_train.py --config configs/train.yaml
eval:
	python scripts/05_evaluate.py --config configs/eval.yaml
