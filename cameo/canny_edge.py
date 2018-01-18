#!/usr/bin/env python3

import cv2
import numpy as np

def main():
    img = cv2.imread('screenshot.png', 0)
    edges = cv2.Canny(img, 100, 200)
    image = np.vstack((img, edges))
    # cv2.imshow('Original & Edge', np.vstack((img, edges)))
    cv2.imwrite('original_edge.png', image)
    cv2.imshow('Original & Edge', image)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
