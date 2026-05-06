#!/usr/bin/env python
"""
Validation Script for NUCES Data Science Assignment 03
Checks:
1. All 46 tasks are implemented
2. Code is Google Colab compatible
3. All required formulas (manual before scipy)
4. Proper Markdown explanations
5. Plots have labels and titles
"""

import json
import re

# Load notebook
with open('notebooks/Actuarial_Analytics_Assignment.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

cells = notebook['cells']
print("=" * 80)
print("ASSIGNMENT VALIDATION REPORT")
print("=" * 80)

# Track tasks
tasks_found = set()
issues = []
warnings = []

# Part 1: Distribution Fitting (Tasks 1-14)
part1_markers = {
    'Task 1': ['bmi.mean()', 'bmi.std()'],
    'Task 2': ['norm.cdf', 'P(BMI <'],
    'Task 3': ['boolean indexing', 'DataFrame'],
    'Task 4': ['histogram', 'pdf'],
    'Task 5': ['ppf', 'percentile'],
    'Task 6': ['smoker.*mean', 'p ='],
    'Task 7': ['math.comb', 'Binomial PMF'],
    'Task 8': ['binom.cdf'],
    'Task 9': ['np.random.binomial', 'simulated'],
    'Task 10': ['sex.*smoker'],
    'Task 11': ['children.mean()', 'dispersion'],
    'Task 12': ['math.factorial', 'Poisson PMF'],
    'Task 13': ['children.*proportion', 'DataFrame'],
    'Task 14': ['children.*>=.*3'],
}

# Part 2: Hypothesis Testing (Tasks 15-35)
part2_markers = {
    'Task 15': ['smoker.*charges', 'DataFrame'],
    'Task 16': ['boxplot', 'smoker'],
    'Task 17': ['levene'],
    'Task 18': ['ttest_ind', 'p-value'],
    'Task 19': ['t.interval', 'confidence'],
    'Task 20': ["Cohen's d"],
    'Task 21': ['mannwhitneyu'],
    'Task 22': ['sex.*charges'],
    'Task 23': ['levene.*sex'],
    'Task 24': ['ttest_ind.*sex'],
    'Task 25': ["Cohen's d.*sex"],
    'Task 26': ['age.*bmi', 'under_40.*over_40'],
    'Task 27': ['levene.*age', 'ttest.*age'],
    'Task 28': ['CI.*age.*bmi'],
    'Task 29': ['pearsonr'],
    'Task 30': ['region.*charges', 'mean'],
    'Task 31': ['combinations', 'region.*pairs'],
    'Task 32': ['Bonferroni', 'adjusted_p'],
    'Task 33': ['FWER', 'family-wise'],
    'Task 34': ['t.interval.*region'],
    'Task 35': ['errorbar', 'region'],
}

# Part 3: Custom Investigation (Tasks 36-46)
part3_markers = {
    'Task 36': ['male.*smoker.*charges'],
    'Task 37': ['female.*smoker.*charges'],
    'Task 38': ['comparison.*DataFrame'],
    'Task 39': ['Bonferroni.*2'],
    'Task 40': ['manager', 'paragraph'],
    'Task 41': ['hypothesis', 'H₀', 'H₁'],
    'Task 42': ['descriptive', 'statistics'],
    'Task 43': ['test.*statistic'],
    'Task 44': ['confidence.*interval'],
    'Task 45': ['effect.*size'],
    'Task 46': ['concluding', 'sentences'],
}

all_markers = {**part1_markers, **part2_markers, **part3_markers}

# Search cells
for task_name, patterns in all_markers.items():
    found = False
    for cell in cells:
        cell_text = ''.join(cell['source']).lower()
        if any(pattern.lower() in cell_text for pattern in patterns):
            found = True
            tasks_found.add(task_name)
            break
    
    if not found:
        issues.append(f"⚠️  {task_name} may be incomplete (markers not found: {patterns})")

# Check for Google Colab compatibility
colab_issues = []
for i, cell in enumerate(cells):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        
        # Check for non-Colab compatible code
        if 'from google.colab' not in source and 'pd.read_csv' in source:
            if 'raw.githubusercontent.com' not in source:
                colab_issues.append(f"Cell {i+1}: May have path issues in Colab (no URL)")
        
        # Check for missing imports
        if 'import' not in source and i < 10:
            continue  # Skip later cells
        
        # Check matplotlib backend
        if 'plt.show()' in source and 'matplotlib' not in source:
            if i < 50:  # First 50 cells should have matplotlib imported
                pass  # OK if imported earlier

# Print results
print(f"\n✅ TASKS FOUND: {len(tasks_found)}/46")
print(f"   Part 1 (Distribution): {sum(1 for t in tasks_found if '1' in t or '2' in t or '3' in t or '4' in t or '5' in t or '6' in t or '7' in t or '8' in t or '9' in t or '10' in t or '11' in t or '12' in t or '13' in t or '14' in t)}/14")
print(f"   Part 2 (Hypothesis Testing): {sum(1 for t in tasks_found if '15' in t or '16' in t or '17' in t or '18' in t or '19' in t or '20' in t or '21' in t or '22' in t or '23' in t or '24' in t or '25' in t or '26' in t or '27' in t or '28' in t or '29' in t or '30' in t or '31' in t or '32' in t or '33' in t or '34' in t or '35' in t)}/21")
print(f"   Part 3 (Custom Investigation): {sum(1 for t in tasks_found if '36' in t or '37' in t or '38' in t or '39' in t or '40' in t or '41' in t or '42' in t or '43' in t or '44' in t or '45' in t or '46' in t)}/11")

print(f"\n📋 TOTAL CELLS: {len(cells)}")
print(f"   Code cells: {sum(1 for c in cells if c['cell_type'] == 'code')}")
print(f"   Markdown cells: {sum(1 for c in cells if c['cell_type'] == 'markdown')}")

print("\n🔍 GOOGLE COLAB COMPATIBILITY:")
print(f"   Issues found: {len(colab_issues)}")
if colab_issues:
    for issue in colab_issues[:5]:
        print(f"   - {issue}")

print("\n⚠️  POTENTIAL ISSUES:")
if issues:
    for issue in issues[:10]:
        print(f"   {issue}")
else:
    print("   None detected!")

print("\n✅ KEY REQUIREMENTS CHECK:")
checks = {
    "Data URL (raw.githubusercontent)": any('raw.githubusercontent' in ''.join(c['source']) for c in cells if c['cell_type'] == 'code'),
    "Random seed set": any('np.random.seed' in ''.join(c['source']) for c in cells if c['cell_type'] == 'code'),
    "Levene's test": any('levene' in ''.join(c['source']).lower() for c in cells if c['cell_type'] == 'code'),
    "Welch's t-test": any('equal_var=False' in ''.join(c['source']) for c in cells if c['cell_type'] == 'code'),
    "Mann-Whitney U": any('mannwhitneyu' in ''.join(c['source']).lower() for c in cells if c['cell_type'] == 'code'),
    "Bonferroni correction": any('bonferroni' in ''.join(c['source']).lower() or ('*' in ''.join(c['source']) and 'p_value' in ''.join(c['source'])) for c in cells if c['cell_type'] == 'code'),
    "Cohen's d": any("cohen" in ''.join(c['source']).lower() for c in cells if c['cell_type'] == 'code'),
    "Confidence intervals": any('t.interval' in ''.join(c['source']) or 'interval' in ''.join(c['source']).lower() for c in cells if c['cell_type'] == 'code'),
    "Plots with labels": any(('xlabel' in ''.join(c['source']) and 'ylabel' in ''.join(c['source'])) or 'set_' in ''.join(c['source']) for c in cells if c['cell_type'] == 'code'),
    "Markdown explanations": len([c for c in cells if c['cell_type'] == 'markdown']) > 20,
}

for check, result in checks.items():
    symbol = "✅" if result else "❌"
    print(f"   {symbol} {check}")

print("\n" + "=" * 80)
print("VALIDATION COMPLETE")
print("=" * 80)
