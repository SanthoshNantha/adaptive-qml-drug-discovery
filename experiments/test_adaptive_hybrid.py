import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from hybrid.adaptive_hybrid import adaptive_quantum_feature
import numpy as np

uncertainties = [0.001, 0.01, 0.05]

for u in uncertainties:
    q_val, decision = adaptive_quantum_feature(u)
    print(f"Uncertainty={u} | Decision={decision} | Quantum value={q_val}")
