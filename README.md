# Skin Lesion Triage — Bayesian Decision and Uncertainty

Project for **Automatic Image Analysis**, Topic B: **Bayesian Decision and Uncertainty — Skin Lesion Triage**.

The goal is to compare a transparent classical image-analysis pipeline with a frozen modern CNN representation on the same binary triage task:

- **Class 1:** melanoma
- **Class 0:** benign lesion

The main question is how the classifier decision changes when false negatives are considered much more costly than false positives.

## Dataset

[HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T) 

The dataset is not included in the repository because HAM10000 is large.

Download the HAM10000 / ISIC 2018 dermoscopy dataset and place the files under:

```text
data/raw/
```

The code expects the HAM10000 metadata CSV and the image files to be available somewhere inside `data/raw/`. 

The ideal layout is:

```text
data/raw/
├── HAM10000_metadata.csv
├── HAM10000_images_part_1/
│   ├── ISIC_0024306.jpg
│   └── ...
└── HAM10000_images_part_2/
    ├── ISIC_0034320.jpg
    └── ...
```

---


## Repository Layout

```
skin_lesion_triage/
  skin_lesion/
    data/
      raw/          # original downloaded images (not committed)
      processed/    # pre-processed features
    notebooks/      # exploratory and result notebooks
    src/            # importable Python modules
    results/
      figures/      # plots (ROC, reliability diagrams, etc.)
      tables/       # CSV / result tables
  requirements.txt
  README.md
```


## Reproducible execution order

Run the notebooks in this order:

1. `01_data_inspection.ipynb`  
   Loads the HAM10000 metadata, defines the binary task, creates a balanced subset, and saves sample class figures.

2. `02_feature_extraction.ipynb`  
   Extracts HSV colour histograms from the selected images.

3. `03_split.ipynb`  
   Creates stratified, lesion-group-aware train/validation/test splits.

4. `04_gmm_bic.ipynb`  
   Fits class-conditional Gaussian mixture models and selects the number of components using BIC.

5. `05_bayes_decision.ipynb`  
   Computes Bayesian posteriors and compares MAP and cost-sensitive decisions.

6. `06_evaluation.ipynb`  
   Evaluates the classical GMM pipeline with ROC, reliability diagrams, ECE and temperature scaling.

7. `08_split_with_image_ids.ipynb`  
   Saves split membership with image IDs for the modern image-based pipeline.

8. `09_efficientnet_training.ipynb`  
   Trains a binary classification head on top of a frozen EfficientNet-B0 backbone.

9. `10_efficientnet_evaluation_calibration.ipynb`  
   Evaluates EfficientNet-B0 with ROC, calibration, temperature scaling, cost-sensitive decisions and uncertainty examples.

10. `11_classical_vs_modern_comparison.ipynb`  
    Produces the final classical-vs-modern comparison tables and ROC plot.

---




## Pipelines

### Classical pipeline

The classical method uses:

1. image resizing;
2. HSV conversion;
3. per-channel colour histograms with 32 bins per channel;
4. concatenation into a 96-dimensional feature vector;
5. one Gaussian mixture model per class;
6. BIC-based GMM component selection;
7. Bayes posterior computation using class priors and class-conditional likelihoods;
8. MAP and asymmetric-cost decision rules.

The asymmetric costs are:

- false negative cost: `C_FN = 5`
- false positive cost: `C_FP = 1`

Therefore the cost-sensitive melanoma decision threshold is:

```text
theta = C_FP / (C_FP + C_FN) = 1 / 6 ≈ 0.1667
```

---

### Modern pipeline

The modern method uses:

1. ImageNet-pretrained EfficientNet-B0;
2. frozen pretrained backbone;
3. a trained binary classification head;
4. validation-based early stopping;
5. ROC, reliability diagrams and ECE;
6. temperature scaling fitted only on the validation split;
7. comparison between MAP threshold `0.5` and cost-sensitive threshold `1/6`.

Only the classification head is trained. The pretrained EfficientNet-B0 feature extractor remains frozen.

---


## Main generated outputs

Figures are saved under `results/figures/`

Tables are saved under `results/tables/`
