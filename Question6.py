# # Q6. Can Ridge Regression handle both categorical and continuous independent variables?

# Yes, Ridge Regression can handle both categorical and continuous independent variables (predictors) within the same model

# Categorical variables need to be encoded into numerical form before they can be used in Ridge Regression

# After encoding, it's important to scale the continuous and encoded variables. Scaling ensures that all variables have similar scales, which is crucial for Ridge Regression, as it operates on the assumption that all predictors are on the same scale


# When using Ridge Regression with a combination of categorical and continuous variables, it's essential to select an appropriate value for the regularization parameter (λ or alpha) using techniques like cross-validation
