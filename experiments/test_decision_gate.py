import sys
import os

# --- FORCE Python to see project root ---
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from hybrid.decision_gate import decide_quantum_level
import numpy as np

# Test uncertainties
uncertainties = np.array([0.001, 0.01, 0.05])

for u in uncertainties:
    print(u, "→", decide_quantum_level(u))
