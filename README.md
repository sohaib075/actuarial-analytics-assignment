# Actuarial Analytics Assignment

A comprehensive statistical analysis of insurance pricing factors using 46 advanced data science tasks. This project demonstrates rigorous hypothesis testing, distribution fitting, and multiple comparison correction for actuarial decision-making.

[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/sohaib075/actuarial-analytics-assignment)
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

---

## 📊 Executive Summary

**Statistical Analysis of 1,338 Insurance Policyholders**

| Metric | Value |
|--------|-------|
| Sample Size | 1,338 policyholders |
| Data Completeness | 100% (no missing values) |
| Smokers | 274 (20.48%) |
| Avg Premium | $13,270 |
| Premium Range | $1,121 - $63,770 |

### 🎯 Key Findings

| Factor | Recommendation | Evidence |
|--------|---|---|
| **Smoking** | ✅ Implement separate tier | d=1.88 (large), p<0.001, 95% CI: [$23k-$25k] |
| **Sex** | ❌ Do not implement | d=0.11 (negligible), confounded by smoking |
| **Age & BMI** | ✅ Include in model | r=0.11 (p<0.001), both independent |
| **Region** | ❌ Do not implement | No difference after Bonferroni correction |

---

## 📁 Project Structure

```
actuarial-analytics-assignment/
├── notebooks/
│   └── Actuarial_Analytics_Assignment.ipynb    # Main analysis (31 cells)
├── docs/
│   ├── PHASE_COMPLIANCE_AUDIT.md               # Technical validation
│   ├── COMPLETION_CHECKLIST.md                 # Task tracker (46/46)
│   └── EXECUTIVE_SUMMARY.md                    # Business recommendations
├── data/                                        # Data files (if applicable)
├── .gitignore                                   # Git exclusions
├── requirements.txt                             # Python dependencies
└── README.md                                    # This file
```
---

## 🚀 Quick Start

### 1️⃣ Clone Repository
```bash
git clone https://github.com/sohaib075/actuarial-analytics-assignment.git
cd actuarial-analytics-assignment
```

### 2️⃣ Set Up Environment
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # macOS/Linux

pip install -r requirements.txt
```

### 3️⃣ Run Analysis
```bash
jupyter notebook notebooks/Actuarial_Analytics_Assignment.ipynb
```

### 4️⃣ Review Documentation
- 📄 Start with: `docs/EXECUTIVE_SUMMARY.md` (business findings)
- 🔍 Deep dive: `docs/PHASE_COMPLIANCE_AUDIT.md` (technical details)
- ✓ Verify: `docs/COMPLETION_CHECKLIST.md` (all 46 tasks)

---

## 📊 Analysis Overview

### Part 1: Distribution Fitting (14 Tasks)
**Normal Distribution — BMI**
- Parameters: μ=30.66, σ=6.10
- Model accuracy: 98.51% (error: 1.49%)
- Conclusion: ✅ Normal model suitable for BMI categorization

**Binomial Distribution — Smoker Status**
- Probability: p = 0.2048
- Manual PMF: `math.comb()` implementation verified against scipy
- Most likely: P(X=10 in 50) = 13.93%

**Poisson Distribution — Children Count**
- Rate: λ = 1.0949
- Finding: Data is **bimodal** ("no kids" vs "multiple kids")
- Recommendation: ⚠️ Use empirical counts, not Poisson, for pricing

---

### Part 2: Hypothesis Testing (21 Tasks)

---

### Part 2: Hypothesis Testing (21 Tasks)

#### Smoker Pricing (7 Tasks)
```
Step 1: Descriptive Stats → Smokers: $32,050 | Non-smokers: $8,434
Step 2: Levene's Test     → Use Welch's t-test (variances unequal)
Step 3: Welch's t-test    → t=17.87, df=274.7, p<0.001 ✓ SIGNIFICANT
Step 4: 95% CI            → [$23,195, $24,985] (entire interval positive)
Step 5: Cohen's d         → d=1.88 (LARGE effect, >0.8)
Step 6: Mann-Whitney U    → p<0.001 (non-parametric agreement ✓)
```
**Recommendation:** ✅ **Implement separate smoker tier** (~$24K premium differential)

#### Sex Pricing (4 Tasks)
- Males: $13,956 | Females: $12,569 | Difference: $1,387
- Cohen's d: 0.11 (negligible effect)
- Confounding: Sex difference disappears when controlling for smoking
- **Recommendation:** ❌ **Do NOT implement sex pricing**

#### Age & BMI Correlation (4 Tasks)
- Pearson r: 0.109 (p<0.001) — weak but significant
- Both variables independent (no multicollinearity)
- **Recommendation:** ✅ **Include both in premium model**

#### Regional Pricing with Bonferroni (6 Tasks)
- 6 pairwise t-tests × Bonferroni α: 0.05/6 = **0.00833**
- Unadjusted FWER: 26% | Corrected: 5% ✓
- Result: All regional pairs become non-significant after correction
- **Recommendation:** ❌ **Do NOT implement regional pricing**

---

### Part 3: Custom Investigations (10 Tasks)

---

### Part 3: Custom Investigations (10 Tasks)

**Sex-Stratified Smoking Analysis (5 Tasks)**
- Males: 23.52% smokers | Females: 17.37% smokers
- Sex is a confounding variable, not direct risk factor

**Regional Smoking Chi-Square (5 Tasks)**
- χ² = 3.74, p = 0.29 (non-significant)
- Smoking rates uniform across regions (18-22%)

---

## 🛠️ Technical Specifications

### Statistical Methods Implemented

| Method | Purpose | Status |
|--------|---------|--------|
| **Manual Formulas** | Binomial PMF (math.comb), Poisson PMF (math.factorial) | ✅ |
| **Levene's Test** | Variance equality check before EVERY t-test | ✅ |
| **Welch's t-test** | Unequal variances handling | ✅ |
| **Mann-Whitney U** | Non-parametric validation | ✅ |
| **Bonferroni Correction** | Multiple comparisons FWER control | ✅ |
| **95% Confidence Intervals** | Uncertainty quantification | ✅ |
| **Cohen's d** | Effect size with classification | ✅ |
| **Cramer's V** | Contingency table association | ✅ |

### Dependencies
```
pandas     2.0+    # Data manipulation
numpy      1.24+   # Numerical computing
scipy      1.10+   # Statistical functions
matplotlib 3.7+    # Visualization
seaborn    0.12+   # Statistical graphics
jupyter    1.0+    # Interactive notebooks
```

### Reproducibility
- ✅ Random seed: `np.random.seed(42)`
- ✅ All 31 cells execute sequentially
- ✅ 150+ kernel variables available for inspection
- ✅ No hardcoded magic numbers

---

## 📊 Executive Summary

### Pricing Recommendations

| Factor | Finding | Action |
|--------|---------|--------|
| **Smoking** | Large effect (d=1.88), p<0.001 | ✅ Implement tier |
| **Sex** | Negligible effect (d=0.11), confounded by smoking | ❌ Do not implement |
| **Age & BMI** | Weak correlation (r=0.11), both significant | ✅ Include in model |
| **Region** | No significant difference after Bonferroni | ❌ Do not implement |

### Business Impact
- **Smoker Premium:** +$24,090 justified
- **Potential Revenue:** If 274 smokers reclassified → $6.6M annual revenue correction
- **Risk Mitigation:** Non-smoker tier now fairly priced

---

## 📁 Files Included

- **`Actuarial_Analytics_Assignment.ipynb`** — Main analysis notebook (31 executed cells)
- **`PHASE_COMPLIANCE_AUDIT.md`** — Detailed compliance verification against 8 professional phases
- **`COMPLETION_CHECKLIST.md`** — Task-by-task completion tracker (46/46 ✅)
- **`EXECUTIVE_SUMMARY.md`** — Professional findings for pricing committee
- **`README.md`** — This file

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/sohaib075/actuarial-analytics-assignment.git
cd actuarial-analytics-assignment
```

### 2. Set Up Environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
pip install -r requirements.txt
```

### 3. Run the Analysis
```bash
jupyter notebook Actuarial_Analytics_Assignment.ipynb
```

### 4. Review Documentation
- Read `EXECUTIVE_SUMMARY.md` for key findings
- Check `PHASE_COMPLIANCE_AUDIT.md` for technical validation
- See `COMPLETION_CHECKLIST.md` for task verification

---

## 📦 Dependencies

```
pandas>=2.0
numpy>=1.24
scipy>=1.10
matplotlib>=3.7
seaborn>=0.12
jupyter>=1.0
```

**Python Version:** 3.9+ (tested with 3.11)

---

## 📚 Key Concepts Demonstrated

1. **Parametric Hypothesis Testing** — t-tests with Levene's assumption check
2. **Non-Parametric Alternatives** — Mann-Whitney U validation
3. **Multiple Comparisons** — Bonferroni family-wise error rate correction
4. **Effect Sizes** — Cohen's d, Cramer's V, odds ratios
5. **Confidence Intervals** — 95% CI construction and interpretation
6. **Distribution Fitting** — Normal, Binomial, Poisson with validation
7. **Confounding Analysis** — Stratified tests to identify causal pathways
8. **Data Visualization** — Publication-quality figures with interpretations

---

## 🎓 Learning Outcomes

After reviewing this project, you'll understand:
- ✅ How to structure a professional statistical analysis
- ✅ When to use parametric vs. non-parametric tests
- ✅ How to control error rates in multiple comparisons
- ✅ How to communicate uncertainty (CIs, effect sizes)
- ✅ How to identify and control for confounding
- ✅ How to present technical findings to business stakeholders

---

## 🔍 Validation & Compliance

✅ **PHASE 1:** Setup & Reproducibility (seed=42, clean imports)  
✅ **PHASE 2:** Code & Markdown Conventions (every cell interpreted)  
✅ **PHASE 3:** Statistical Foundation (distribution fitting verified)  
✅ **PHASE 4:** 6-Step Pipelines (Levene → t-test → CI → d → Mann-Whitney)  
✅ **PHASE 5:** Technical Publication (ready for Medium/blog)  
✅ **PHASE 6:** GitHub & Professional Outputs (this README)  
✅ **PHASE 7:** Code Quality (descriptive names, full comments)  
✅ **PHASE 8:** Common Mistakes Avoided (no p-hacking, proper corrections)

---

## 📞 Contact & Questions

For questions about this analysis, open an issue on GitHub or review the detailed documentation files included in the repository.

---

## 📄 License

This project is provided as-is for educational purposes.

---

**Last Updated:** May 6, 2026  
**Status:** ✅ Complete & Production Ready  
**All 46 Tasks:** Implemented & Verified
