def decide_quantum_level(uncertainty, low=0.005, mid=0.02):
    if uncertainty < low:
        return "classical"
    elif uncertainty < mid:
        return "quantum_shallow"
    else:
        return "quantum_deep"
