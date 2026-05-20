# Skin Lesion Triage with Bayesian Decision Theory

**Topic B** — Computer Vision course project.

## Dataset

[HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T) — a class-balanced subset (melanoma vs. benign) is used to avoid majority-class bias.

## Pipelines

### Classical Pipeline

1. **Feature extraction** — HSV colour histograms (bins: 32×32×32) computed per image.
2. **Density estimation** — per-class Gaussian Mixture Models (GMM) fitted on training features.
3. **Bayesian decision** — posterior probabilities combined with an asymmetric cost matrix to produce the final triage decision.

### Modern Pipeline

1. **Backbone** — EfficientNet-B0 pre-trained on ImageNet, weights frozen.
2. **Classification head** — a lightweight trainable head appended to the frozen backbone.
3. **Training** — only the head is trained on the HAM10000 subset.

## Evaluation

| Metric | Description |
|---|---|
| ROC / AUC | Standard discrimination metric |
| Reliability diagram | Visual calibration check (predicted probability vs. fraction of positives) |
| ECE | Expected Calibration Error (scalar summary of calibration) |

## Asymmetric Cost Matrix

Missing a melanoma (false negative) is clinically far more costly than a false alarm (false positive):

```
lambda(FN) = 5 × lambda(FP)
```

The Bayesian decision threshold is shifted accordingly so the classifier errs on the side of caution.

## Repository Layout

```
skin_lesion/
  data/
    raw/          # original downloaded images (not committed)
    processed/    # pre-processed tensors / feature arrays
  notebooks/      # exploratory and result notebooks
  src/            # importable Python modules
  results/
    figures/      # plots (ROC, reliability diagrams, etc.)
    tables/       # CSV / LaTeX result tables
requirements.txt
README.md
```
