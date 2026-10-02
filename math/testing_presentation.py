# ----------------------
# @Time  : 2026 Oct
# @Author: Ruishen Huang
# ----------------------
import numpy as np
from numpy import ndarray


class PrintUtil:
    BRIEF_HASH_LEN = 4
    BRIEF_NDARRAY_LEN = 4

    @classmethod
    def better_hash(cls, s: str):
        if s is None:
            return "None"
        if len(s) > cls.BRIEF_HASH_LEN:
            return f"{s[:cls.BRIEF_HASH_LEN]}..."
        else:
            return s

    @classmethod
    def better_ndarray(cls, vec: ndarray):
        return f"{np.round(vec[:cls.BRIEF_NDARRAY_LEN], 2)}..."

    @classmethod
    def better_float(cls, f: float):
        return round(f, 4)

    @classmethod
    def better_tensor(cls, x):
        return np.round(x.tolist(), 2).flatten().tolist()
