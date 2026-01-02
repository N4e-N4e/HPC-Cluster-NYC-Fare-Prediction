##Setup and Execution

#Important links:

GitLab link: https://gitlab.nrp-nautilus.io/N4e-mizzou/final-project-nyc_fare_prediction

Hugging Face Link: https://huggingface.co/datasets/N4e-mizzou/NYC_Taxi_data

Custom Image link: https://gitlab.nrp-nautilus.io/N4e-mizzou/ml_image

---------------------------------------------------------------------------------------------------------------------------------------

Steps:

1)Pull the project repository from the GitLab link provided above.

2)Create the custom image in a separate repository with the files provided in the Image directory. Alternatively, the image paths provided above can also be used.

3)Create a PVC using the persistent_volume.yml file provided in the POD_PVC directory.

4)Create a pod using the pod_pvc.yml file provided in the POD_PVC directory. Using the created pod, access the PVC.

5)Within the /work_env directory of the PVC, create /cleandata, /result, and /Scripts directories.

6)Within the /cleandata directory, pull the dataset from the Hugging Face link provided above.

7)Exit the PVC.

8)Copy the scripts from the /Scripts directory on JupyterHub into the /Scripts directory of the project PVC.

9)Run the Data_split.yaml job. Wait until completion.

10)Run RF.yaml, LR_Lasso.yaml, and XGB.yaml jobs. Wait until completion.

11)Run Test_LR.yaml, Test_RF.yaml, and Test_XGB.yaml jobs. Wait until completion.

12)Use the same pod as before to access the PVC. Within the /work_env/result directory, visuals of performance evaluations on test data can be found.

13)Use the kubectl logs <jobname> command for the jobs created in step 10 to view performance metrics.

14)Additionally, EDA_XGB.yaml, EDA_Test_XGB.yaml jobs can be run one after the other to evaluate the performance of the best performing model on a selected set of features.

#Refer Taxi_EDA.ipynb to know what the selected features are and why they were chosen. 