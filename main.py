import cv2 as cv
#Loading an image
#cv.imread("download.png")
#cv.imshow("Image", cv.imread("download.png"))
#cv.waitKey(0)


capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()
