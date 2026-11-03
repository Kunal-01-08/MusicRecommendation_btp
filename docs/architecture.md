# Architecture

```text
Audio -> log-mel -> PANNs CNN14 -> audio embedding -> audio KNN track edges
Interactions + track metadata -> heterogeneous graph (User/Track/Artist/Genre/Tag/Raag)
Heterogeneous graph -> R-GCN or HGT -> user-track scores
Audio representation + graph representation -> fusion -> recommendations
```

Cold tracks are excluded from training interactions. Their audio embeddings can still query warm-track neighbours. Raag nodes are optional.
