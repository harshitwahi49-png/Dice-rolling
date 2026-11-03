import numpy as np


def kmeans_assign(input: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    distances=pairwise_distances(centroids,input)
    return np.argmin(distances,axis=1)
    pass
