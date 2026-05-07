# Actuarial Analytics Assignment

## Overview
This repository contains the completed **Actuarial Analytics Assignment** (Data Science Assignment 03). The project simulates working as a junior data analyst on an actuarial team at a health insurance company. The objective is to analyze a dataset of 1,338 policyholders to provide statistically backed answers to several business questions ahead of a pricing review. 

Every claim and pricing recommendation in this analysis is supported by computed probabilities, statistical tests, or confidence intervals, accompanied by plain-English interpretations for management.

## Dataset
**Medical Cost Personal Dataset**
- **Rows:** 1,338 policyholders (no missing values)
- **Columns:**
  - `age`: Policyholder age in years
  - `sex`: Male / Female
  - `bmi`: Body Mass Index (continuous)
  - `children`: Number of dependants covered (0 to 5)
  - `smoker`: Yes / No
  - `region`: Northeast / Northwest / Southeast / Southwest
  - `charges`: Annual insurance charges in USD (the target variable for pricing)

## Project Structure

The analysis is conducted entirely within `notebooks/Actuarial_Analytics_Assignment.ipynb` and is divided into three main phases:

### Part 1: Fitting Distributions to the Data
Before running hypothesis tests, the underlying distributions of the data are modeled:
1. **The Normal Distribution:** Modeling `bmi`. Includes computing analytical probabilities, empirical proportions, and evaluating tail skewness (5th/95th percentiles).
2. **The Binomial Distribution:** Modeling `smoker` rates. Includes calculating empirical probabilities, theoretical PMF/CDF, and simulating 10,000 policyholder groups to verify theoretical variance.
3. **The Poisson Distribution:** Modeling the `children` column (dependants). Includes computing the dispersion ratio to check for overdispersion and comparing the theoretical PMF against actual data to identify zero-inflation.

### Part 2: Hypothesis Testing
A rigorous hypothesis testing pipeline (Levene's test, Welch's t-test, Confidence Intervals, Cohen's d, and Mann-Whitney U checks) applied to core business questions:
1. **Smoker Risk:** Do smokers cost the company significantly more?
2. **Sex-Based Pricing:** Is there a statistically significant difference in charges between males and females?
3. **Age & BMI:** Has BMI increased with age? (T-test accompanied by Pearson's correlation).
4. **Regional Pricing:** Do mean charges differ across the four regions? (Pairwise tests utilizing the Bonferroni correction to control the Family-Wise Error Rate).

### Part 3: Open-Ended Investigation
1. **Manager's Question:** A sex-stratified analysis determining if the smoking premium is consistent across both males and females.
2. **Custom Investigation:** Evaluating whether extreme obesity (top BMI quartile) drives significantly higher medical charges *after entirely excluding the confounding effect of smoking*.

## Requirements
The notebook requires the following standard data science libraries:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`

## Execution
Run all cells in `Actuarial_Analytics_Assignment.ipynb` sequentially. The dataset is fetched automatically from its source URL.
