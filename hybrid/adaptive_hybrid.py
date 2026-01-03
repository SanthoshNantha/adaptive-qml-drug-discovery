from hybrid.decision_gate import decide_quantum_level
from quantum.quantum_model import run_quantum

def adaptive_quantum_feature(uncertainty):
    decision = decide_quantum_level(uncertainty)

    if decision == "classical":
        return None, decision

    q_value = run_quantum(decision)
    return q_value, decision
