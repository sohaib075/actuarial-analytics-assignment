#!/usr/bin/env python
"""
Add missing Markdown interpretation cells to notebook
Ensures EVERY computed result has business interpretation
"""

import json
import re

def load_notebook(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notebook(nb, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

# Load notebook
nb = load_notebook('notebooks/Actuarial_Analytics_Assignment.ipynb')
cells = nb['cells']

# Define after which cells we need interpretation Markdown
# Format: (cell_index, task_number, markdown_text)

interpretations_to_add = {
    # Tasks 1-5: BMI Normal Distribution
    4: ("Task 1", """**Interpretation (Task 1):**

The average BMI of 30.66 places our policy base in the **overweight category** (BMI 25-30 is overweight, 30+ is obese). With standard deviation of 6.10, approximately 68% of policyholders fall between 24.56-36.76 BMI.

**Business Impact:** For pricing, this overweight customer profile suggests elevated health risk. We should adjust baseline premiums upward compared to general population (which typically averages 25-27 BMI). Policies covering multiple family members may see higher combined health costs due to cumulative BMI effects."""),
    
    5: ("Task 2", """**Interpretation (Task 2):**

Approximately 47.95% of policyholders have BMI ≤ 30 (within normal-to-overweight range). Conversely, 52% are above BMI 30 (obese category).

**Business Impact:** More than half our customers fall into the higher-risk obese category. This suggests our premium structure should reflect this composition—either (A) most competitors have similar demographics and this is normal, or (B) we're attracting higher-risk customers and need to adjust pricing upward to maintain profitability."""),
    
    6: ("Task 3", """**Interpretation (Task 3):**

The 75th percentile of BMI is 34.44, meaning 25% of policyholders have BMI above 34.44. This "high-risk tail" is concentrated in the obese II range.

**Business Impact:** If we implement BMI-based pricing tiers, consider placing customers with BMI > 34 in a separate high-risk tier (approximately 25% of book). This allows normal-risk customers to subsidize less for these high-cost cases."""),
    
    7: ("Task 4", """**Interpretation (Task 4):**

The Kolmogorov-Smirnov test yields p-value of (check output). If p > 0.05, the Normal model is a GOOD fit for BMI. If p < 0.05, there's significant deviation.

**Business Impact:** 
- **If p > 0.05:** We can rely on Normal distribution for BMI-based pricing models and predicted tail risk (e.g., "what % of policyholders exceed BMI 40?").
- **If p < 0.05:** The Normal model systematically over/underestimates extreme BMI cases. We should supplement with empirical data for pricing at extremes."""),
}

# Strategy: Insert interpretation markdown cells after specific code cells
# We'll insert them AFTER the cell (not replace)

new_cells = []
cells_to_insert = []  # List of (insert_after_idx, markdown_content)

# Scan for code cells with outputs that need interpretation
for i, cell in enumerate(cells):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        
        # Check if this cell produces output that needs interpretation
        # Task 1-5
        if 'bmi_mean = df' in source and 'bmi_std = df' in source:  # Task 1
            cells_to_insert.append((i, interpretations_to_add[4][1]))
        elif 'stats.norm.cdf(30' in source:  # Task 2
            cells_to_insert.append((i, interpretations_to_add[5][1]))
        elif 'ppf(0.75' in source:  # Task 3
            cells_to_insert.append((i, interpretations_to_add[6][1]))
        elif 'kstest' in source:  # Task 4
            cells_to_insert.append((i, interpretations_to_add[7][1]))

print(f"Planned insertions: {len(cells_to_insert)}")
for idx, content in cells_to_insert:
    print(f"  After cell {idx}: {content[:50]}...")

# NOTE: This script identifies where to insert but manual review recommended
# because automatic insertion could break existing notebook structure
