# DSA8420 - Nyc_Taxi - Project



## Project Abstract:
The project focuses on predicting New York City taxi trip fares using publicly available data from the New York City Taxi and Limousine Commission (TLC). Accurate fare estimation is crucial for passengers, taxi operators, and urban planners, requiring analysis of large-scale datasets with temporal, spatial, and trip-specific attributes. Some of the information included in the dataset is trip distance and duration, pricing rates, payment types, surcharges, and fare amounts.

To enhance the quality of the data, extensive preprocessing was performed to remove invalid and noisy records. Precautionary steps were taken to prevent data leakage, either by removing fare-related attributes or replacing them with indicator flags. Additionally, temporal and spatial features were engineered to capture more meaningful travel patterns.

Three machine learning models were used: Linear Regression (Lasso), Random Forest, and XGBoost. These models were trained and then evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the R-squared metric. XGBoost achieved the best overall performance, demonstrating its ability to capture non-linear relationships.

To support scalability and reproducibility, the project was deployed on the Nautilus High-Performance Computing (HPC) cluster using Kubernetes and Docker. This setup allowed for efficient resource utilization, parallel job execution, and reproducible experimentation. Overall, this project showcases the practical benefits of combining large-scale machine learning pipelines with HPC infrastructure.

--------------------------------------------------------------------------------------------------------------------------------------

For this project, the repository is broken into seven main directories to ensure clarity and reproducibility. These directories are as follows:

1)Documentation: Contains Jupyter notebooks for data cleaning, feature engineering, and EDA of the processed data, along with instructions to run and set up the project.

2)Scripts: Contains Python scripts for data splitting, model training, and performance evaluation.

3)Jobs: Contains YAML job files that execute Python scripts on Nautilus using a custom Docker image, with the project PVC (ukgff-finalproj) mounted.

4)Results: Contains evaluation outputs which include PNG visualizations and text performance metrics.

5)POD_PVC: Contains the YAML files used to create the project PVC and a pod to access the PVC.

6)Image: Contains the Docker, YAML, and text files required to build the custom Docker image.

7)Data: Contains raw data files used to construct the final dataset.

-----------------------------------------------------------------------------------------------------------------------------------

The dataset was pulled from my public Hugging Face data repository.

Link: https://huggingface.co/datasets/N4e-mizzou/NYC_Taxi_data

----------------------------------------------------------------------------------------------------------------------------------

The project uses a custom Docker image created in GitLab.

Link: https://gitlab.nrp-nautilus.io/N4e-mizzou/ml_image
