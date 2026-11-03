# Coding agent rules
- Never commit data, embeddings or checkpoints.
- All hyperparameters live in configs/*.yaml, never hard-coded.
- Set seeds via coldstart.seed.set_seed.
- Cold-start test tracks must never appear in training interactions; add a test whenever touching splits.
- Run `make lint test` before finishing any task.
- Prefer small, typed, tested functions; no notebooks in src/.
