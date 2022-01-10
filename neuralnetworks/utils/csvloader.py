

from io import TextIOWrapper
from typing import Callable, Tuple, List

DataMapper = Callable[[List[str]], Tuple[List[float], List[float]]]


def load_csv(file_path: str, mapper: DataMapper, sep: str = ",") -> List[Tuple[List[float], List[float]]]:
    ret: List[Tuple[List[float], List[float]]] = []
    with open(file_path, mode='tr') as f:
        meta: str = f.readline().strip()
        profile: List[str] = meta.split(sep)
        size = len(profile)
        classifications: int = size - 2

        for line in f.readlines():
            ts_c: list[str] = line.split(sep)

            tags: List[str] = [float(t) for t in ts_c[:-1]]
            classification_index: int = int(ts_c[-1])

            category: List[float] = [0 for i in range(classifications)]
            category[classification_index] = 1

            ret.append((tags, category))

    return ret
