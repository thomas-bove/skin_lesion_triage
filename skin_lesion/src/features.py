import cv2
import numpy as np


def hsv_histogram(img_bgr: np.ndarray, bins: tuple = (32, 32, 32)) -> np.ndarray:
    """Return an L1-normalised HSV histogram feature vector for one image.

    Args:
        img_bgr: BGR uint8 image as read by cv2.imread.
        bins: number of bins for (H, S, V) channels.

    Returns:
        1-D float32 array of length sum(bins), summing to 1.
    """
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    h_hist = cv2.calcHist([hsv], [0], None, [bins[0]], [0, 180]).ravel()
    s_hist = cv2.calcHist([hsv], [1], None, [bins[1]], [0, 256]).ravel()
    v_hist = cv2.calcHist([hsv], [2], None, [bins[2]], [0, 256]).ravel()

    feat = np.concatenate([h_hist, s_hist, v_hist]).astype(np.float32)

    norm = feat.sum()
    if norm > 0:
        feat /= norm

    return feat
