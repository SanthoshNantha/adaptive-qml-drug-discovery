from qiskit import transpile
from qiskit_aer import Aer
import numpy as np
from quantum.circuits import shallow_circuit, deep_circuit

backend = Aer.get_backend("qasm_simulator")

def run_quantum(level="shallow"):
    params = np.random.rand(4) * np.pi

    if level == "quantum_shallow":
        qc = shallow_circuit(params=params)
    elif level == "quantum_deep":
        qc = deep_circuit(params=params)
    else:
        return None

    qc_t = transpile(qc, backend)
    job = backend.run(qc_t, shots=512)
    result = job.result()
    counts = result.get_counts()

    # Simple quantum feature: normalized expectation proxy
    value = sum(int(k, 2) * v for k, v in counts.items()) / 512
    return value
