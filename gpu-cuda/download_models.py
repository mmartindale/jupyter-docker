from huggingface_hub import snapshot_download

MODELS = [
    "google/gemma-4-12B",
    "google/gemma-4-12B-it",
]

for model_id in MODELS:
    print(f"Downloading {model_id}...")
    path = snapshot_download(
        repo_id=model_id,
        cache_dir="/opt/huggingface/hub",
    )
    print(f"{model_id} cached at {path}")

print("All model snapshots downloaded.")
