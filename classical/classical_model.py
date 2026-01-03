import numpy as np
from sklearn.ensemble import RandomForestRegressor

class EnsembleRegressor:
    def __init__(self, n_models=5):
        self.models = [
            RandomForestRegressor(
                n_estimators=200,
                random_state=i,
                n_jobs=-1
            )
            for i in range(n_models)
        ]

    def fit(self, X, y):
        for model in self.models:
            model.fit(X, y)

    def predict(self, X):
        preds = np.array([m.predict(X) for m in self.models])
        mean = preds.mean(axis=0)
        var = preds.var(axis=0)
        return mean, var
