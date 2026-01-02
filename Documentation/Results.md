## Execution time of each model on Nautilus is as follows:

1)Linear Regression:

•Model training: 3 minutes and 23 seconds

•Model evaluation: 24 seconds

2)Random Forest:

•Model training: 13 minutes

•Model evaluation: 43 seconds

3)XGBoost

•Model training: 4 minutes and 52 seconds

•Model evaluation: 38 seconds

All jobs used 4 CPU cores and 16 GB RAM to execute. Initially, 8 GB RAM was used, however, after the 2-minute mark, the jobs would fail due to insufficient memory.

----------------------------------------------------------------------------------------------------------------------------------------

## The performance metrics of each model are as follows:

1)Linear Regression:

•MAE: 1.57

•RMSE: 3.40

•R²: 0.9596

2)Random Forest:

•MAE: 1.33

•RMSE: 2.57

•R²: 0.9770

3)XGBoost:

•MAE: 0.53

•RMSE: 1.51

•R²: 0.9921

Across all three models, training and test performance are consistent, indicating strong generalization and minimal overfitting.
Linear Regression (Lasso) serves as a strong baseline, confirming that NYC taxi trips are driven by features such as distance and time. Random Forest further improves performance by capturing non-linear relationships while also reducing error. XGBoost performs the best overall on both training and testing data, cementing itself as the final model choice.

----------------------------------------------------------------------------------------------------------------------------------------

From EDA, it was found that trip distance and duration, trip type, toll roads used, and pickup/drop-off locations are primary factors influencing fare amounts. To confirm this, XGBoost was trained using only these features, achieving the following performance metrics:

•MAE: 0.57

•RMSE: 1.57

•R²: 0.9914

The performance is remarkably close to the model trained on all features, indicating that the predictors identified during EDA capture most of the information needed for accurately predicting NYC taxi fares.

-------------------------------------------------------------------------------------------------------------------------------------------

## Reproducibility:

All the results are fully reproducible using the provided GitLab repository, Docker image, and job configurations. Within each Python script, a fixed random seed (seed = 42) was set to ensure predictable behavior. Using the same container environment guarantees consistent library versions and executes jobs in an identical environment, preventing variability in results.

# Refer to the Results directory for visuals and logs.