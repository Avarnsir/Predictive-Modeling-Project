import kagglehub
import pandas as pd

# Download latest version
file_path = "/workspaces/Predictive-Modeling-Project/data/"
path = kagglehub.dataset_download("arunjangir245/boston-housing-dataset")

print("Path to dataset files:", file_path)