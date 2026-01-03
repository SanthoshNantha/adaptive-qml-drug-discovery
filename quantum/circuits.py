from qiskit import QuantumCircuit
import numpy as np

def shallow_circuit(n_qubits=4, params=None):
    qc = QuantumCircuit(n_qubits)
    for i in range(n_qubits):
        qc.h(i)
        if params is not None:
            qc.ry(params[i], i)
    qc.measure_all()
    return qc

def deep_circuit(n_qubits=4, params=None, layers=3):
    qc = QuantumCircuit(n_qubits)
    for _ in range(layers):
        for i in range(n_qubits):
            qc.h(i)
            if params is not None:
                qc.ry(params[i], i)
        for i in range(n_qubits - 1):
            qc.cx(i, i + 1)
    qc.measure_all()
    return qc
