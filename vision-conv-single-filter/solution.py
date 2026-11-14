import numpy as np


def conv2d_single_filter(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    h,w=image.shape
    kh,kw=kernel.shape
    out_h,out_w=h-kh+1,w-kw+1
    output=np.empty((out_h,out_w),dtype=image.dtype)
    for i in range(out_h):
        for j in range(out_w):
            output[i,j]=np.sum(image[i:i+kh,j:j+kw]*kernel)
    return output
