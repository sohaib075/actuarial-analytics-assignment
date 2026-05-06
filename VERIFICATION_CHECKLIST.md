# VERIFICATION CHECKLIST - How to Check If Assignment Is Correct

## 1. QUICK VERIFICATION (5 minutes)

### Check Markdown Interpretations After Every Output
**Do this:** Open notebook in VS Code, scroll through and verify each task code cell is followed by Markdown interpretation.

**Pattern to look for:**
```
CODE CELL (Task 1) - Calculate BMI mean
⬇️
MARKDOWN CELL - "Interpretation (Task 1): The average BMI of 30.66..."
✅ CORRECT

CODE CELL (Task 2) - Output some number
⬇️ 
No Markdown cell?
❌ MISSING - Will lose 50% marks!
```

**Quick check:** Count cells: Should be ~135 cells (65 code + 70 markdown)
```bash
# In terminal:
python -c "import json; cells = json.load(open('notebooks/Actuarial_Analytics_Assignment.ipynb'))['cells']; print(f'Total: {len(cells)}, Code: {sum(1 for c in cells if c[\"cell_type\"]==\"code\")}, Markdown: {sum(1 for c in cells if c[\"cell_type\"]==\"markdown\")}')"
```

---

## 2. CODE QUALITY CHECK (10 minutes)

### Verify Manual Formulas (Task 7 & 12)
**Task 7 - Check for manual Binomial before scipy:**
```python
# SHOULD SEE THIS FIRST:
manual_pmf = math.comb(n_sample, k) * (p ** k) * ((1 - p) ** (n_sample - k))

# THEN scipy verification:
scipy_pmf = stats.binom.pmf(k, n_sample, p)
```

**Task 12 - Check for manual Poisson before scipy:**
```python
# SHOULD SEE THIS FIRST:
manual_poisson = (np.exp(-lambda_param) * (lambda_param ** k)) / math.factorial(k)

# THEN scipy verification:
scipy_poisson = stats.poisson.pmf(k, lambda_param)
```

**How to verify in notebook:**
1. Press `Ctrl+F` → Search "math.comb" → Should find in Task 7
2. Press `Ctrl+F` → Search "math.factorial" → Should find in Task 12
3. Confirm scipy calls come AFTER manual calculations

---

### Verify Statistical Pipelines (Every Hypothesis Test)
**Pattern to look for:**
```python
# Step 1: Levene's test
levene_stat, levene_p = stats.levene(group1, group2)

# Step 2: Choose t-test type
t_stat, t_p = stats.ttest_ind(group1, group2, equal_var=(levene_p > 0.05))

# Step 3: 95% Confidence Interval
ci = stats.t.interval(0.95, df, loc=mean, scale=sem)

# Step 4: Cohen's d
cohens_d = (mean1 - mean2) / pooled_std

# Step 5: Mann-Whitney validation
u_stat, u_p = stats.mannwhitneyu(group1, group2)
```

**Tasks to check:**
- ✅ Task 17: Smoker pricing (should have all 5 steps)
- ✅ Task 24: Sex pricing (should have all 5 steps)
- ✅ Task 32: Bonferroni loop (should use itertools.combinations for 6 pairs)

---

## 3. EXECUTION TEST (30 minutes) - MOST IMPORTANT

### Run Notebook End-to-End

**Step 1: Run in VS Code**
```
Click the "Run All Cells" button (▶️ icon at top of notebook)
OR press Ctrl+Shift+Alt+Enter
```

**Step 2: Watch for errors**
- ❌ RED X = Error (fix before submission)
- ✅ Green checkmark = Success

**Step 3: Expected outputs when running**

| Task | Expected Output | Range |
|------|-----------------|-------|
| Task 1 | BMI Mean | 30-31 |
| Task 2 | P(BMI≤30) | 0.45-0.50 |
| Task 6 | Smoker rate p | 0.20-0.21 |
| Task 7 | Manual PMF matches scipy | Match=True |
| Task 12 | Manual Poisson matches scipy | Match=True |
| Task 15 | Smoker mean charges | $30,000+ |
| Task 15 | Non-smoker mean charges | $8,000-$10,000 |
| Task 17 | T-test p-value | < 0.0001 |
| Task 17 | Cohen's d | 1.5-2.0 |
| Task 24 | Sex t-test p-value | > 0.05 |
| Task 25 | Cohen's d sex | 0.10-0.15 |
| Task 32 | Adjusted p-values | All > 0.05 |

### Common Execution Errors & Fixes

**Error: "No module named 'pandas'"**
```bash
pip install -r requirements.txt
```

**Error: "Could not retrieve data from URL"**
- Check internet connection
- URL in code should be: `https://raw.githubusercontent.com/selva86/datasets/master/insurance.csv`

**Error: "np.random.seed not found"**
- Check line 9 of setup cell has: `np.random.seed(42)`

---

## 4. PLOT VERIFICATION (10 minutes)

### Check all plots have labels and titles

**Look for these in each plot task:**

| Task | Plot Type | Must Have |
|------|-----------|-----------|
| Task 5 | Histogram + PDF | xlabel, ylabel, title, legend |
| Task 10 | Bar chart | xlabel, ylabel, title |
| Task 16 | Boxplot | xlabel, ylabel, title |
| Task 21 | Dual histogram | xlabel, ylabel, title, legend |
| Task 29 | Scatter + regression | xlabel, ylabel, title, legend |
| Task 35 | Error bar | xlabel, ylabel, title |

**How to check:** When notebook runs, each plot should have visible labels. If blank/missing labels = lose marks!

---

## 5. MARKDOWN INTERPRETATION VERIFICATION (15 minutes)

### Verify Each Task Has Business Interpretation

**Checklist - Each markdown should explain:**
✅ What the number/result means  
✅ Why it matters for the insurance company  
✅ What action to take (if applicable)

**Example of GOOD interpretation:**
```markdown
**Interpretation (Task 17):**
The t-test shows t=17.87, p < 0.001, and d=1.88

Smokers pay $20,000+ more than non-smokers on average.
This is HIGHLY SIGNIFICANT and LARGE effect size.

Business decision: MUST implement separate smoker pricing tier.
```

**Example of BAD interpretation (will lose 50% marks):**
```markdown
t = 17.87, p-value = 0.0000001
```
❌ NO business context = HALF MARKS!

**Quick check script:**
```bash
# Count markdown cells with "Interpretation" keyword
grep -c "Interpretation" notebooks/Actuarial_Analytics_Assignment.ipynb
# Should return: 40+ (indicating interpretations for most tasks)
```

---

## 6. GOOGLE COLAB COMPATIBILITY TEST (15 minutes)

### Test on Google Colab

**Step 1: Copy notebook to Google Colab**
- Open https://colab.research.google.com
- Click "Upload" → Select notebook

**Step 2: Run first few cells**
- If they work, Colab compatible ✅
- If error about paths, there's a local path issue ❌

**What should work:**
- Data loading from URL ✅
- All plots display ✅
- No "file not found" errors ✅

---

## 7. FINAL CHECKLIST - Run This Command

Copy and paste this into terminal to auto-verify:

```bash
cd "d:\uni data\semester 8\datascience\Data Science Assignment 03"

# Count total cells
python -c "
import json
nb = json.load(open('notebooks/Actuarial_Analytics_Assignment.ipynb'))
cells = nb['cells']
code_cells = sum(1 for c in cells if c['cell_type']=='code')
md_cells = sum(1 for c in cells if c['cell_type']=='markdown')
interp_count = sum('Interpretation' in ''.join(c['source']) for c in cells if c['cell_type']=='markdown')
manual_comb = sum('math.comb' in ''.join(c['source']) for c in cells if c['cell_type']=='code')
manual_fact = sum('math.factorial' in ''.join(c['source']) for c in cells if c['cell_type']=='code')
levene_tests = sum('levene' in ''.join(c['source']).lower() for c in cells if c['cell_type']=='code')
bonferroni = sum('bonferroni' in ''.join(c['source']).lower() for c in cells if c['cell_type']=='code')

print(f'''
NOTEBOOK VERIFICATION SUMMARY
============================
Total Cells: {len(cells)}
  - Code cells: {code_cells}
  - Markdown cells: {md_cells}

CRITICAL CHECKS:
✅ Markdown interpretations: {interp_count} (Target: 40+)
✅ math.comb (Task 7): {manual_comb} (Target: ≥1)
✅ math.factorial (Task 12): {manual_fact} (Target: ≥1)
✅ Levene's tests: {levene_tests} (Target: ≥5)
✅ Bonferroni correction: {bonferroni} (Target: ≥1)

VERDICT:
''' + (
'PASS ✅' if (interp_count >= 40 and manual_comb >= 1 and manual_fact >= 1) 
else 'NEEDS WORK ⚠️'
))
"
```

---

## 8. MOST COMMON MISTAKES TO AVOID

### ❌ Missing Interpretation Cells
- ✅ Fix: Add Markdown after EVERY code output cell
- 📊 Impact: -50% per missing interpretation

### ❌ Scipy called BEFORE manual formula
- ✅ Fix: math.comb BEFORE scipy.binom.pmf (Task 7)
- 📊 Impact: Zero marks for that task

### ❌ Plot without labels/title
- ✅ Fix: Add `xlabel()`, `ylabel()`, `title()`
- 📊 Impact: -20% per plot

### ❌ P-value reported without business meaning
- ✅ Fix: Always follow p-value with "what this means for insurance"
- 📊 Impact: -50% for that result

### ❌ No Levene's test before t-test
- ✅ Fix: Always run Levene first to check equal_var
- 📊 Impact: Statistically incorrect test

### ❌ Regional pricing "significant" after Bonferroni
- ✅ Fix: Apply correction: p_adjusted = min(p_raw * 6, 1.0)
- 📊 Impact: Wrong business conclusion

---

## 9. PRE-SUBMISSION VERIFICATION (Final 10 min check)

### Checklist Before Submitting

- [ ] Run entire notebook → No errors
- [ ] All 46 tasks produce output
- [ ] Every output has Markdown interpretation
- [ ] Task 7 has manual formula THEN scipy
- [ ] Task 12 has manual formula THEN scipy
- [ ] All plots have titles and labeled axes
- [ ] Levene + t-test + CI + Cohen's d + Mann-Whitney appear in hypothesis test tasks
- [ ] Task 32 shows Bonferroni correction (p_adjusted = min(p*6, 1.0))
- [ ] README.md updated and accurate
- [ ] requirements.txt has all dependencies
- [ ] .gitignore prevents __pycache__ and .venv commits
- [ ] Git has commits from BOTH team members
- [ ] Notebook tested on Google Colab
- [ ] Blog post created and link ready
- [ ] LinkedIn post created and link ready

---

## 10. IF SOMETHING IS WRONG - QUICK FIXES

### Problem: Interpretation cell missing for Task X
**Fix:** 
```bash
Use edit_notebook_file tool to insert Markdown after that code cell
```

### Problem: Plot has no title
**Fix:**
```python
# Add this line after plt.plot():
plt.title('Your Title Here')
```

### Problem: Bonferroni not working
**Fix:**
```python
# Should be:
p_adjusted = min(p_value * num_comparisons, 1.0)
# NOT:
p_adjusted = p_value / num_comparisons  # This is wrong!
```

### Problem: Notebook won't run
**Debug:**
```bash
# Run cell by cell to find which one fails
python -c "import pandas; import numpy; import scipy; print('All imports OK')"
```

---

## SUCCESS CRITERIA

Your assignment is **CORRECT** if ALL of these are TRUE:

✅ 135+ cells total (65 code, 70 markdown)  
✅ Every code cell followed by interpretation Markdown  
✅ Tasks 7 & 12 have manual formula BEFORE scipy  
✅ All hypothesis tests follow: Levene → t-test → CI → Cohen's d → Mann-Whitney  
✅ Bonferroni applied to Task 32 (p_adjusted = min(p*6, 1.0))  
✅ All plots have xlabel, ylabel, title  
✅ Notebook runs end-to-end with no errors  
✅ Outputs match expected ranges (see section 3)  
✅ Works on Google Colab  
✅ Git commits from both team members  

**Expected Grade:** 90-95% if ALL above are true
**Estimated Grade:** 50-60% if interpretation cells missing
**Estimated Grade:** 0% if manual formulas missing from Tasks 7/12
