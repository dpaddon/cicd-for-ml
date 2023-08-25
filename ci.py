import wandb

wandb_version = wandb.__version__
expected_version = "2.0"

print(f"{wandb_version=}")
assert wandb_version == expected_version, f"expected {expected_version}, got {wandb_version}"
