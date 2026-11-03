# Cold-Start Music Recommendation

Research scaffold recommending tracks without interaction history using PANNs audio embeddings and heterogeneous graphs. Music4All is primary; Saraga/raag labels are optional.

```text
Audio -> log-mel -> PANNs CNN14 -> audio embeddings -> audio KNN edges
Metadata/interactions -> Track/Artist/Genre/Tag/Raag/User graph -> R-GCN or HGT
Graph + audio -> user-track prediction -> recommendations
```

## Setup
`python -m venv .venv` then `pip install -e ".[audio,graph,dev]"`.

Put downloads in `data/raw/music4all/` and optional Saraga in `data/raw/saraga/`. Clean tables go in `data/interim/`; embeddings, graph objects, and splits go in `data/processed/`. No data or checkpoints are included.

## Run order
Run scripts `01_prepare_data.py`, `02_extract_embeddings.py`, `03_build_graph.py`, `04_train.py`, `05_evaluate.py`, and `06_longtail_analysis.py` in order, passing each its matching config. These scripts are stubs.

Evaluation holds out cold tracks and removes all their interactions from training. Report Recall@20, NDCG@20, catalogue coverage, tail share at k, and mean popularity. Raag support is optional.

## Status
- [ ] Prepare data
- [ ] Extract log-mel and PANNs embeddings
- [ ] Build heterogeneous graph
- [ ] Train models
- [ ] Evaluate cold-start and long-tail quality
