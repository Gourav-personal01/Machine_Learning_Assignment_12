# # Q1. What is Ridge Regression, and how does it differ from ordinary least squares regression?

# In Ridge regularization, an L2 penalty term is added to the standard linear regression objective function.

# The objective becomes minimizing the sum of squared errors (MSE) plus the L2 penalty term:

# Objective = MSE + λ * Σ(coefficients²)

# The hyperparameter λ (lambda) controls the strength of regularization. A larger λ leads to stronger regularization.

# Ridge regularization encourages the model to have small but non-zero coefficient values for all predictors. It reduces the impact of individual predictors but doesn't force them to be exactly zero.

# difference between Ridge Regression and Ols Regression - 

# OLS regression does not include any regularization. It aims to minimize the sum of squared errors without adding a penalty for coefficient magnitude.

# The objective function in Ridge Regression is to minimize the sum of squared errors plus the L2 penalty term whereas The objective function in OLS regression is simply to minimize the MSE

# Ridge Regression tends to shrink the magnitude of coefficients towards zero. However, it does not force any coefficients to be exactly zero. whereas OLS Regression does not shrink the coefficients. It estimates coefficients without any constraint on their magnitude. 