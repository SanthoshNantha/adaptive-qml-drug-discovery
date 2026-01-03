import sys
import os

# Force project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from hybrid.adaptive_hybrid import adaptive_quantum_feature
from evaluation.quantum_cost import quantum_cost
import numpy as np

print(">>> Evaluation started")

# Simulated uncertainty distribution
uncertainties = np.random.choice(
    [0.001, 0.01, 0.05],
    size=1000,
    p=[0.6, 0.25, 0.15]
)

adaptive_cost = 0
static_cost = 0

for u in uncertainties:
    _, decision = adaptive_quantum_feature(u)
    adaptive_cost += quantum_cost(decision)
    static_cost += 3  # static hybrid always deep

print(">>> Evaluation finished")

print("Adaptive quantum cost:", adaptive_cost)
print("Static quantum cost:", static_cost)

reduction = 100 * (1 - adaptive_cost / static_cost)
print("Cost reduction (%):", round(reduction, 2))
