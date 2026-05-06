# NUCES CS4048 Data Science Assignment 03 - Compliance Checklist

## CRITICAL REQUIREMENT: Markdown Interpretation Cells

**ASSIGNMENT SPECIFICATION**: "Every computed result must be followed by a Markdown cell explaining what the number means in the context of the insurance company. A p-value or probability with no interpretation receives half marks."

### Status: ⚠️  NEEDS VERIFICATION & LIKELY INCOMPLETE

For each task, after the code cell that produces output, there MUST be a Markdown cell that explains:
- What the number means
- Business context for insurance company
- Why it matters for decision-making

#### Example Good Format:
```python
# Code cell
bmi_mean = df['bmi'].mean()
print(f"Mean BMI: {bmi_mean:.2f}")
```
**Then immediately followed by Markdown cell:**
```markdown
**Interpretation (Task 1):**
The average BMI of policyholders is 30.66. This is slightly above the overweight 
threshold (BMI=30), indicating our customer base has higher health risk on average. 
For pricing, this suggests we should adjust premiums slightly upward to account for 
elevated health costs associated with overweight status.
```

---

## All 46 Tasks Compliance Status

### PART 1: Distribution Fitting (14 Tasks)

- [ ] **Task 1**: BMI Mean & Std Dev (4 decimals) + Markdown interpretation
- [ ] **Task 2**: Normal CDF P(BMI ≤ 30) + Markdown interpretation
- [ ] **Task 3**: Actual vs Predicted 75th percentile comparison + Markdown
- [ ] **Task 4**: KS test & histogram with PDF overlay + Markdown (assess fit)
- [ ] **Task 5**: 5th & 95th percentile comparison + Markdown
- [ ] **Task 6**: Smoker proportion p (4 decimals) + Markdown
- [ ] **Task 7**: Manual Binomial PMF k=5,10,15,20 using math.comb + SciPy check + Markdown
- [ ] **Task 8**: Binomial CDF as percentages + plain English + Markdown
- [ ] **Task 9**: Simulation vs Theoretical comparison + Markdown
- [ ] **Task 10**: Male/Female smoker breakdown (count & pct) + Markdown
- [ ] **Task 11**: Children mean & interpretation + Markdown
- [ ] **Task 12**: Manual Poisson PMF using math.factorial + SciPy check + Markdown
- [ ] **Task 13**: Children proportion ≥3 as DataFrame + Markdown
- [ ] **Task 14**: Binomial test specific probabilities + Markdown

### PART 2: Hypothesis Testing (21 Tasks)

- [ ] **Task 15**: Smoker vs charges grouped DataFrame + Markdown
- [ ] **Task 16**: Box plot (labeled axes) + Markdown
- [ ] **Task 17**: Levene's test decision (equal variances?) + Markdown
- [ ] **Task 18**: Welch's t-test (if unequal) + p-value + Markdown interpretation
- [ ] **Task 19**: 95% CI with t-distribution + Markdown interpretation
- [ ] **Task 20**: Cohen's d effect size + classification + Markdown
- [ ] **Task 21**: Mann-Whitney U validation + Markdown
- [ ] **Task 22**: Sex vs charges grouped DataFrame + Markdown
- [ ] **Task 23**: Levene's test for sex groups + Markdown
- [ ] **Task 24**: t-test for sex + p-value + Markdown
- [ ] **Task 25**: Cohen's d for sex + Markdown (should be negligible ≈0.11)
- [ ] **Task 26**: Age groups (under 40 vs 40+) vs BMI + Markdown
- [ ] **Task 27**: Levene + t-test for age groups + Markdown
- [ ] **Task 28**: 95% CI for age groups + Markdown
- [ ] **Task 29**: Pearson correlation age-BMI + interpretation + Markdown
- [ ] **Task 30**: Regional mean charges + DataFrame + Markdown
- [ ] **Task 31**: Pairwise regional comparisons (6 pairs) using itertools.combinations + Markdown
- [ ] **Task 32**: Bonferroni correction (α_adjusted = α/6 = 0.00833) + significant before/after + Markdown
- [ ] **Task 33**: FWER explanation + Markdown
- [ ] **Task 34**: 95% CI for each region + Markdown
- [ ] **Task 35**: Error bar plot with regions (labeled) + Markdown

### PART 3: Custom Investigation (11 Tasks)

- [ ] **Task 36**: Male smokers vs charges + Markdown
- [ ] **Task 37**: Female smokers vs charges + Markdown
- [ ] **Task 38**: Comparison table (male vs female smoking impact) + Markdown
- [ ] **Task 39**: Bonferroni for 2 groups (male/female) + Markdown
- [ ] **Task 40**: Manager summary paragraph (business recommendation) + Markdown
- [ ] **Task 41**: Null & Alt hypotheses (H₀, H₁) written + Markdown
- [ ] **Task 42**: Descriptive statistics (mean, median, std, quartiles) + Markdown
- [ ] **Task 43**: Test statistic value + interpretation + Markdown
- [ ] **Task 44**: Confidence interval + practical meaning + Markdown
- [ ] **Task 45**: Effect size value + magnitude classification + Markdown
- [ ] **Task 46**: Concluding sentences with business recommendation + Markdown

---

## Code Quality Checklist

### Manual Formula Implementation (CRITICAL)
For tasks specifying "compute manually first":
- [ ] Task 7: Manual Binomial PMF using `math.comb(n, k) * p^k * (1-p)^(n-k)` appears BEFORE `scipy.stats.binom.pmf()`
- [ ] Task 12: Manual Poisson PMF using `(λ^k * e^(-λ)) / k!` appears BEFORE `scipy.stats.poisson.pmf()`

### All Plots Must Have Labels
- [ ] Task 4: Histogram - xlabel, ylabel, title, legend
- [ ] Task 5: Histogram - xlabel, ylabel, title, legend  
- [ ] Task 16: Box plot - xlabel, ylabel, title
- [ ] Task 35: Error bar plot - xlabel, ylabel, title, error bars visible

### Statistical Sequences (Every hypothesis test must follow)
- [ ] Levene's test → reports equal_var decision
- [ ] Choose t-test: Student (equal_var=True) vs Welch (equal_var=False)
- [ ] Report t-statistic, p-value, degrees of freedom
- [ ] 95% CI using t.interval()
- [ ] Cohen's d with threshold classification
- [ ] Mann-Whitney U for non-parametric validation
- [ ] All with Markdown interpretation

### Reproducibility
- [ ] `np.random.seed(42)` in setup cell (executed first)
- [ ] Data loaded from URL (not local file)
- [ ] All paths relative or URL-based (Google Colab compatible)
- [ ] No hardcoded values; all calculated from data

### Markdown Explanation Cells
- [ ] At least one Markdown cell after each code output cell
- [ ] Each Markdown explains: what number means + business context + why it matters
- [ ] No "just numbers" without business interpretation
- [ ] Context-specific language (insurance company premium adjustments, risk assessment, etc.)

---

## Google Colab Compatibility

- [ ] All imports at top of notebook
- [ ] Data URL-based (not local paths)
- [ ] No `%matplotlib notebook` (use `%matplotlib inline`)
- [ ] No Linux-specific commands
- [ ] No GPU/TPU specific code (unless needed)
- [ ] All file operations use URLs or Colab mount points
- [ ] Can run top-to-bottom without errors
- [ ] All cells have been executed in sequence

---

## Delivery Requirements

- [ ] Notebook runs without errors on Google Colab
- [ ] All 46 tasks produce output
- [ ] Every output has Markdown interpretation
- [ ] Manual formulas before scipy for Tasks 7 & 12
- [ ] All plots have labeled axes and titles
- [ ] Random seed set and reproducible
- [ ] Git commits from both team members (currently: check git log)
- [ ] Medium blog post created and link submitted
- [ ] LinkedIn post created and link submitted
- [ ] Frontend developed (requirements unclear - needs specification)

---

## Grading Notes (From Assignment Spec)

> "Every computed result must be followed by a Markdown cell explaining what the number means in the context of the insurance company. A p-value or probability with no interpretation receives half marks."

> "For questions that say 'compute manually first' - write the formula in code using numpy/math before calling scipy. Using only scipy for those steps gets zero marks."

> "Code must be clean, well-commented, reproducible with set random seeds"

> "Submission carries no marks; marks awarded based on viva"

---

## Next Steps

1. **Run notebook end-to-end** to verify all cells execute
2. **Audit Markdown cells** - add interpretation after each output
3. **Verify Task 7 & 12** - ensure manual formulas visible in code
4. **Check all plots** - verify titles and axis labels  
5. **Test on Google Colab** - copy to Colab and run
6. **Add commits** from second team member
7. **Create blog post** - link to submit
8. **Create LinkedIn post** - link to submit

---

Created: 2025
Assignment: NUCES CS4048 Data Science, Spring 2026
Students: [Names]
