import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    mA = np.array(list).reshape(3,3)
    calculations = {
        'mean': [mA.mean(axis=0).tolist(), mA.mean(axis=1).tolist(), mA.flatten().mean()],
        'variance': [mA.var(axis=0).tolist(), mA.var(axis=1.tolist()), mA.flatten().var()],
        'standard deviation': [mA.std(axis=0).tolist(), mA.std(axis=1).tolist(), mA.flatten().std()],
        'max': [mA.max(axis=0).tolist(), mA.max(axis=1).tolist(), mA.flatten().max()],
        'min': [mA.min(axis=0).tolist(), mA.min(axis=1).tolist(), mA.flatten().min()],
        'sum': [mA.sum(axis=0).tolist(), mA.sum(axis=1).tolist(), mA.flatten().sum()]
    }
    return calculations