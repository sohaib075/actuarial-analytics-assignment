import warnings
import math
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

np.random.seed(42)

# Load data
url = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv'
df = pd.read_csv(url)

print('✅ Setup successful')
print(f'Dataset shape: {df.shape}')
print(f'Columns: {list(df.columns)}')
print('\nData types:')
print(df.dtypes)

# Verify a few key calculations
print(f'\nSmoker proportion: {(df["smoker"] == "yes").sum() / len(df):.4f}')
print(f'BMI mean: {df["bmi"].mean():.2f}')

# Test the fixed DataFrame creation
lambda_children = df['children'].mean()
comparison_children = []
for k in range(5):
    actual_prop = (df['children'] == k).sum() / len(df)
    predicted_prop = stats.poisson.pmf(k, lambda_children)
    gap = abs(actual_prop - predicted_prop)
    comparison_children.append({
        'children': k,
        'Actual': actual_prop,
        'Predicted': predicted_prop,
        'Gap': gap
    })

comparison_children_df = pd.DataFrame(comparison_children)
print('\nDataFrame created successfully:')
print(comparison_children_df)

print('\n✅ All tests passed - notebook should run without NameError')
