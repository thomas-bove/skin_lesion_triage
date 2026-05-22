from pathlib import Path
import numpy as np

SEED = 42

_PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR       = _PROJECT_ROOT / "skin_lesion" / "data" / "raw"
PROCESSED_DIR = _PROJECT_ROOT / "skin_lesion" / "data" / "processed"
FIGURES_DIR   = _PROJECT_ROOT / "skin_lesion" / "results" / "figures"
TABLES_DIR    = _PROJECT_ROOT / "skin_lesion" / "results" / "tables"

COST_FN = 5.0   # λ(predict_benign  | true_melanoma) — missing a melanoma (false negative)
COST_FP = 1.0   # λ(predict_melanoma | true_benign)  — unnecessary biopsy  (false positive)

# 2×2 loss matrix  λ[action, true_class]
# Rows = actions  : 0 = predict benign,   1 = predict melanoma
# Cols = true class: 0 = benign (ω_B),    1 = melanoma (ω_M)
#
#              ω_B   ω_M
#  α_benign  [  0    FN ]
#  α_melanoma[ FP     0 ]
COST_MATRIX = np.array([[0.0,     COST_FN],
                         [COST_FP, 0.0    ]])

HSV_BINS       = (32, 32, 32)
IMAGE_SIZE     = 128   # px — resize before feature extraction so all images contribute equally
MC_DROPOUT_T   = 30    # number of stochastic forward passes for MC Dropout uncertainty estimation
