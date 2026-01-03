import pandas as pd
import numpy as np

def load_dataset(path=r"processed/labels.csv", feature_dim=64):
    df = pd.read_csv(path)

    # Temporary random features (will be replaced later)
    X = np.random.randn(len(df), feature_dim)
    y = df["binding_affinity_pK"].values

    return X, y
