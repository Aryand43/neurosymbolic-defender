from datasets import load_dataset

SUPPORTED_DATASETS = {
    "gsm8k": "gsm8k",
    "proofwriter": "tau/ProofWriter",
    "clutrr": "clutrr",
    "math": "competition_math",
    "scan": "scan"
}

def load_benchmark(name: str, split: str = "test"):
    if name not in SUPPORTED_DATASETS:
        raise ValueError(f"Unsupported dataset: {name}")
    return load_dataset(SUPPORTED_DATASETS[name], split=split)
