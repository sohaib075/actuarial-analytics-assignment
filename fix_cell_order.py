import json

with open('notebooks/Actuarial_Analytics_Assignment.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

# New Cell 38 code - combines DataFrame creation + visualization
new_cell_38_code = """# Task 13 (Part 1): Create comparison DataFrame
comparison_children = []
for k in range(5):
    # Actual proportion from data
    actual_prop = (df['children'] == k).sum() / len(df)
    
    # Predicted proportion from Poisson
    predicted_prop = stats.poisson.pmf(k, lambda_children)
    
    # Gap
    gap = abs(actual_prop - predicted_prop)
    gap_pct = gap / actual_prop * 100 if actual_prop > 0 else 0
    
    comparison_children.append({
        'children': k,
        'Actual Proportion': actual_prop,
        'Poisson Predicted': predicted_prop,
        'Absolute Gap': gap,
        'Gap %': gap_pct
    })

comparison_children_df = pd.DataFrame(comparison_children)

# Visualization: Poisson vs Actual distribution
fig, ax = plt.subplots(figsize=(10, 6))

k_vals = comparison_children_df['children'].values
actual_props = comparison_children_df['Actual Proportion'].values
predicted_props = comparison_children_df['Poisson Predicted'].values

x = np.arange(len(k_vals))
width = 0.35

bars1 = ax.bar(x - width/2, actual_props, width, label='Actual Data', alpha=0.8, color='steelblue', edgecolor='black')
bars2 = ax.bar(x + width/2, predicted_props, width, label='Poisson Model', alpha=0.8, color='coral', edgecolor='black')

ax.set_xlabel('Number of Dependants (k)', fontsize=12)
ax.set_ylabel('Proportion', fontsize=12)
ax.set_title('Poisson Model Fit: Predicted vs Actual Distribution of Dependants', fontsize=13, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(k_vals)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

print("\\nVisualization: Comparison of Poisson predictions vs actual proportions")
"""

# Update Cell 38
lines = new_cell_38_code.strip().split('\n')
nb['cells'][38]['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]

# Now update Cell 40 - keep the interpretation part, remove the DataFrame creation
new_cell_40_code = """# Task 13 (Part 2): Analyze and interpret the comparison
print("\\n" + "="*60)
print("TASK 13: POISSON PREDICTION vs ACTUAL PROPORTIONS")
print("="*60)
print(comparison_children_df.to_string(index=False))

# Find largest gap
largest_gap_idx = comparison_children_df['Absolute Gap'].idxmax()
print(f"\\nLargest gap: k={comparison_children_df.loc[largest_gap_idx, 'children']} "
      f"with absolute difference of {comparison_children_df.loc[largest_gap_idx, 'Absolute Gap']:.4f}")

print("\\nInterpretation:")
print("Where is the Poisson model weak?")
for idx, row in comparison_children_df.iterrows():
    if row['Gap %'] > 10:
        print(f"  k={row['children']}: Gap of {row['Gap %']:.2f}% - POOR FIT")
    elif row['Gap %'] > 5:
        print(f"  k={row['children']}: Gap of {row['Gap %']:.2f}% - MODERATE FIT")
    else:
        print(f"  k={row['children']}: Gap of {row['Gap %']:.2f}% - GOOD FIT")
"""

lines = new_cell_40_code.strip().split('\n')
nb['cells'][40]['source'] = [line + '\n' for line in lines[:-1]] + [lines[-1]]

# Save updated notebook
with open('notebooks/Actuarial_Analytics_Assignment.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("✅ Fixed: Moved DataFrame creation to Cell 38 before visualization")
print("✅ Cell 38 now includes: DataFrame creation → Visualization")
print("✅ Cell 40 now includes: Only interpretation/printing")
