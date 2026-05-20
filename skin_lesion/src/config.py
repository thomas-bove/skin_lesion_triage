from pathlib import Path

SEED = 42

_PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR       = _PROJECT_ROOT / "skin_lesion" / "data" / "raw"
PROCESSED_DIR = _PROJECT_ROOT / "skin_lesion" / "data" / "processed"
FIGURES_DIR   = _PROJECT_ROOT / "skin_lesion" / "results" / "figures"
TABLES_DIR    = _PROJECT_ROOT / "skin_lesion" / "results" / "tables"

COST_FN = 5.0
COST_FP = 1.0

HSV_BINS       = (32, 32, 32)
IMAGE_SIZE     = 128   # px — resize before feature extraction so all images contribute equally
MC_DROPOUT_T   = 30    # number of stochastic forward passes for MC Dropout uncertainty estimation
