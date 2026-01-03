import pandas as pd
import math
import re

def convert_to_pK(affinity_str):
    """
    Converts strings like:
    'Kd=49uM', 'Ki=120nM', 'IC50=3.2uM'
    to pK values
    """
    match = re.search(r'=(\d*\.?\d+)([munp]M)', affinity_str)
    if not match:
        return None

    value = float(match.group(1))
    unit = match.group(2)

    # Unit to molar conversion
    unit_factor = {
        'mM': 1e-3,
        'uM': 1e-6,
        'nM': 1e-9,
        'pM': 1e-12
    }

    molar = value * unit_factor[unit]
    return -math.log10(molar)


data = []

with open(r"data/index/INDEX_general_PL.2020R1.lst") as f:
    for line in f:
        if line.startswith("#") or not line.strip():
            continue

        parts = line.split()
        pdb_id = parts[0]
        affinity_raw = parts[3]

        pK = convert_to_pK(affinity_raw)
        if pK is not None:
            data.append([pdb_id, pK])

df = pd.DataFrame(data, columns=["pdb_id", "binding_affinity_pK"])
df.to_csv("processed/labels.csv", index=False)

print("Extracted samples:", df.shape)
print(df.head())
