# # Q5. How does the Ridge Regression model perform in the presence of multicollinearity?

# # By reducing the sensitivity of coefficients to multicollinearity, Ridge Regression can provide more stable and reliable
# # coefficient estimates. This can help identify which predictors have consistent and meaningful relationships with the target variable.

# Ridge Regression does not eliminate predictors from the model entirely, even when multicollinearity is strong. It shrinks the coefficients toward zero, but it rarely forces any of them to be exactly zero. Therefore, all predictors remain in the model to some extent.

# Ridge Regression does not significantly affect the fit of the model in terms of the goodness of fit statistics (e.g., R-squared). It can maintain or slightly improve model fit, especially when multicollinearity is impacting the stability and reliability of OLS regression coefficients.