import sys, os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from hybrid.decision_gate import decide_quantum_level
import numpy as np
import matplotlib.pyplot as plt

# Simulated uncertainty distribution
uncertainties = np.random.choice(
    [0.001, 0.01, 0.05],
    size=1000,
    p=[0.6, 0.25, 0.15]
)

levels = {"classical": 0, "quantum_shallow": 0, "quantum_deep": 0}

for u in uncertainties:
    decision = decide_quantum_level(u)
    levels[decision] += 1

labels = list(levels.keys())
values = [levels[k] for k in labels]

plt.figure()
plt.bar(labels, values)
plt.xlabel("Decision Type")
plt.ylabel("Number of Samples")
plt.title("Adaptive Quantum Usage Distribution")
plt.show()
