import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from classical.dataset import load_dataset
from classical.classical_model import EnsembleRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

from classical.dataset import load_dataset
from classical.classical_model import EnsembleRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Load data
X, y = load_dataset()

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train ensemble
model = EnsembleRegressor(n_models=5)
model.fit(X_train, y_train)

# Predict
mean_pred, uncertainty = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, mean_pred))

print("RMSE:", rmse)
print("Uncertainty stats:", uncertainty.min(), uncertainty.mean(), uncertainty.max())
