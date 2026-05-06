# Actuarial Analytics Assignment - Completion Checklist

## PHASE 1: Project Setup & Planning ✅
- [x] Environment setup (Jupyter/Google Colab)
- [x] Libraries installed (pandas, numpy, matplotlib, seaborn, scipy, math, itertools)
- [x] GitHub repo created with both members as contributors
- [x] Notebook structure planned (6 main sections)

---

## PHASE 2: Notebook Conventions (MUST FOLLOW EVERY TIME)

### Code Quality Standards
- [x] `np.random.seed(42)` set at the very top of notebook
- [x] Code cell → Markdown cell pattern throughout (every computed result followed by interpretation)
- [x] **ALL** plots have title, x-axis label, y-axis label, and legend
- [x] Descriptive variable names used (e.g., `smoker_charges`, not `sc`)
- [x] Comments above major code blocks
- [x] Entire notebook runs reproducibly from scratch

### Statistical Rigor Standards
- [x] Hypotheses stated in Markdown **BEFORE** running tests (H₀ and H₁)
- [x] **EVERY** test includes assumption checking (Levene's, normality, etc.)
- [x] Manual formulas shown **BEFORE** scipy verification
- [x] **EXACT** p-values reported (never just "p < 0.05")
- [x] **ALWAYS** pair statistical significance with practical significance (Cohen's d)
- [x] **95% confidence intervals** for all mean differences
- [x] Effect sizes classified (negligible/small/medium/large)
- [x] Non-parametric validation included where applicable

### Business Communication Standards
- [x] **EVERY** result followed by plain-English interpretation
- [x] No bullet points in interpretations (full sentences for managers)
- [x] **ALL** claims backed by specific numbers (not vague statements)
- [x] Business implications and recommendations provided
- [x] Markdown explains what "95% confidence" means (not misinterpreted as probability)

---

## PHASE 3: Part 1 — Distribution Fitting (14 Tasks) ✅

### 1.1 Normal Distribution - BMI (5 Tasks)
- [x] **Task 1**: μ and σ computed to 4 decimals, printed with interpretation
- [x] **Task 2**: CDF predictions (P(<25), P(25-30), P(≥30)) with business meaning
- [x] **Task 3**: Comparison table (predicted vs actual), error analysis shown
- [x] **Task 4**: Histogram + Normal PDF overlay with:
  - [x] Title: "Histogram of BMI with Fitted Normal Distribution"
  - [x] X-label: "BMI", Y-label: "Density"
  - [x] Legend showing both curves
  - [x] Markdown commentary on fit quality
- [x] **Task 5**: 5th & 95th percentiles compared, errors quantified, business implication

### 1.2 Binomial Distribution - Smoker Rate (5 Tasks)
- [x] **Task 6**: p computed to 4 decimals, interpreted
- [x] **Task 7**: **Manual** PMF using `math.comb`, then **scipy verified**
  - [x] DataFrame showing manual, scipy, and match confirmation
  - [x] All four k values (5, 10, 15, 20) included
- [x] **Task 8**: P(<8) and P(>20) with pricing manager interpretation
- [x] **Task 9**: 10,000 simulation, error < 1% analysis, 2-panel plot with:
  - [x] Histogram of simulated values + mean lines
  - [x] Q-Q plot for normality check
- [x] **Task 10**: Smoker rates by sex, expected counts for n=50

### 1.3 Poisson Distribution - Dependants (4 Tasks)
- [x] **Task 11**: λ, variance, dispersion ratio computed and interpreted
- [x] **Task 12**: **Manual** PMF using `math.factorial` and `math.exp`, **scipy verified**
  - [x] 4-decimal values for k=0-4
- [x] **Task 13**: Comparison table (actual vs Poisson), gap analysis
- [x] **Task 14**: P(≥3) model vs actual, misclassification count, business impact

---

## PHASE 4: Part 2 — Hypothesis Testing (21 Tasks) ✅

### Standard Pipeline for EVERY Test:
1. [x] State hypotheses (H₀ vs H₁) in markdown
2. [x] Descriptive stats (n, mean, median, std)
3. [x] Levene's test (variance equality)
4. [x] t-test (with appropriate variant: Welch's if unequal)
5. [x] 95% confidence interval (mean difference)
6. [x] Cohen's d effect size classification
7. [x] Mann-Whitney U (non-parametric check)
8. [x] Business interpretation (specific numbers, not "significant")

### 2.1 Smoker Pricing (7 Tasks)
- [x] **Task 15**: Descriptive stats by smoker status (n, mean, median, std)
- [x] **Task 16**: Box plot with labels and spread commentary
- [x] **Task 17**: Levene's test (exact p-value reported)
- [x] **Task 18**: t-test chosen variant (Welch's if p<0.05), report t, df, p
- [x] **Task 19**: 95% CI with interpretation ("confident smokers cost between $X and $Y")
- [x] **Task 20**: Cohen's d with classification (e.g., "LARGE effect")
- [x] **Task 21**: Mann-Whitney U confirms conclusion

### 2.2 Sex Pricing (4 Tasks)
- [x] **Task 22**: Descriptive stats by sex
- [x] **Task 23**: Levene's test + appropriate t-test
- [x] **Task 24**: 95% CI (does it include zero?)
- [x] **Task 25**: Cohen's d + pricing recommendation with **specific numbers**

### 2.3 Age & BMI (4 Tasks)
- [x] **Task 26**: Under-40 vs 40+ groups, summary stats
- [x] **Task 27**: Levene's test + t-test variant
- [x] **Task 28**: 95% CI + Cohen's d
- [x] **Task 29**: Pearson r, agreement check with t-test, markdown explanation

### 2.4 Regional Pricing (6 Tasks) — **MOST COMPLEX**
- [x] **Task 30**: Mean charges by region (sorted)
- [x] **Task 31**: All 6 pairwise t-tests using `itertools.combinations`
- [x] **Task 32**: Bonferroni correction (p × 6, cap at 1.0)
  - [x] Before/after comparison shown
- [x] **Task 33**: FWER = 1-(0.95^6) = 26%, **explained for non-statisticians**
- [x] **Task 34**: 95% CI for each region (DataFrame with all 4 regions)
- [x] **Task 35**: Horizontal error bar plot with:
  - [x] Title: "Regional Mean Charges with 95% CIs"
  - [x] X-label: "Mean Annual Charges ($)", Y-label: "Region"
  - [x] Grand mean dashed line reference
  - [x] Markdown identifying overlapping CIs

---

## PHASE 5: Part 3 — Custom Investigation (10 Tasks) ✅

### 3.1 Sex-Stratified Smoking Premium (5 Tasks)
- [x] **Task 36**: Male smokers vs non-smokers full pipeline
  - [x] Levene's test, Welch's t-test, 95% CI, Cohen's d
- [x] **Task 37**: Female smokers vs non-smokers full pipeline
- [x] **Task 38**: Side-by-side comparison DataFrame
- [x] **Task 39**: Bonferroni correction (×2)
- [x] **Task 40**: Manager's paragraph (5-7 sentences with **actual dollar amounts** from CIs)

### 3.2 Your Own Question (5 Tasks)
- [x] **Task 41**: Question and hypotheses (H₀ vs H₁) in markdown
- [x] **Task 42**: Descriptive statistics for groups/variables
- [x] **Task 43**: Appropriate test with assumptions checked
- [x] **Task 44**: 95% confidence interval for quantity of interest
- [x] **Task 45**: Effect size (Cohen's d, Cramér's V, odds ratio, etc.)
- [x] **Task 46**: Markdown conclusion (4+ sentences with business implications)

---

## PHASE 6: Common Mistakes to AVOID

- [x] **NOT** using scipy without showing manual formula first
- [x] **NOT** creating plots without title/labels/legend
- [x] **NOT** saying "significant" without exact p-value and numbers
- [x] **NOT** running Bonferroni wrong (multiply by m, cap at 1.0)
- [x] **NOT** missing markdown interpretations
- [x] **NOT** forgetting to state hypotheses before running tests
- [x] **NOT** reporting only "p < 0.05" (report exact p-value)
- [x] **NOT** skipping effect sizes (Cohen's d or equivalent)
- [x] **NOT** forgetting 95% CIs for mean differences
- [x] **NOT** missing business implications

---

## PHASE 7: GitHub & Deliverables

### GitHub Repository
- [ ] Both members have independent commits (showing individual contribution)
- [ ] README.md explains the project
- [ ] Structure: `/notebook/`, `/data/`, `/README.md`
- [ ] Commit history shows genuine development (not one bulk push)

### Medium Blog Post
- [ ] 800-1200 words
- [ ] Story format (Introduction → Data Overview → Key Findings → Conclusion)
- [ ] Key visualizations included
- [ ] 2-3 surprising findings highlighted

### LinkedIn Post
- [ ] 150-250 words
- [ ] Highlights 2-3 interesting findings
- [ ] Tags university and project
- [ ] Links to Medium and GitHub

---

## FINAL VERIFICATION CHECKLIST

### Notebook Content
- [x] 46 tasks completed and executed
- [x] All cells run from scratch without errors
- [x] Every result has business interpretation
- [x] Random seed set at top (np.random.seed(42))

### Statistical Methods
- [x] Manual formulas before scipy (Tasks 7, 12, etc.)
- [x] Levene's test before every t-test
- [x] Welch's t-test used when variances unequal
- [x] Mann-Whitney U validation included
- [x] Bonferroni correction properly applied
- [x] Exact p-values reported (never just "p<0.05")
- [x] Cohen's d always with classification
- [x] 95% CIs for all mean differences

### Visualization Quality
- [x] All plots have title, x-label, y-label
- [x] All plots have legend
- [x] Proper formatting (figsize, fontsize, tight_layout)
- [x] Grid enabled for clarity
- [x] Markdown describes plot findings

### Business Communication
- [x] No vague statements (all claims have numbers)
- [x] Markdown explains what 95% CI means
- [x] Business recommendations provided
- [x] Hypotheses stated before tests
- [x] Practical vs statistical significance both reported

---

## Sign-Off

**Notebook Status:** ✅ **PRODUCTION READY**

**Ready for:**
- [ ] Pricing committee presentation
- [ ] Model deployment
- [ ] Auditor review
- [ ] Team training

**Last Updated:** [DATE]  
**Reviewed By:** [NAMES]
