import cv2 as cv
import numpy as np


def big_binary_demo(image) :
    cw = 256
    ch = 256
    h , w = image.shape[: 2]
    gray = cv.cvtColor(image , cv.COLOR_BGR2GRAY)
    for row in range(0 , h , ch) :
        for col in range(0 , w , cw) :
            roi = gray[row : row + ch , col : col + cw]
            dev = np.std(roi)
            '''
            if dev < 21 :
                gray[row : row + ch , col : col + cw] = 255
            else :
                ret , dst = cv.threshold(roi , 0 , 255 ,
                                         cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row : row + ch , col : cw + col] = dst
                print(np.std(dst) , np.mean(dst))
            '''
            dst = cv.adaptiveThreshold(roi , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C ,
                                      cv.THRESH_BINARY , 127 , 20)
            #ret , dst = cv.threshold(roi , 0 , 255 , cv.THRESH_BINARY | cv.THRESH_OTSU)
            gray[row : row + ch , col : col + cw] = dst


    cv.imshow("big_binary_demo" , gray)


src = cv.imread("D:/data/sudoku.png")
cv.namedWindow("input image" , cv.WINDOW_AUTOSIZE)
cv.imshow("input image" , src)
big_binary_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()