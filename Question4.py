# Q4. Can Ridge Regression be used for feature selection? If yes, how?

# Yes we can use the Can Ridge Regression as it encourages the model to have small but non-zero coefficient values
# for all predictors. It reduces the impact of individual predictors but doesn't force them to be exactly zero.
# It highly suggested that to lasso over ridge for feature selection but sometimes Ridge Regression has a greater impact on predictors 
# that have lower importance or less influence on the target variable. It tends to assign smaller coefficients to less relevant predictors.