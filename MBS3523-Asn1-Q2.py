
import cv2

capture = cv2.VideoCapture(0)

capture.set(3,640)
capture.set(4,480)

x = 0
dx = 1
y=0
dy = 1
# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()
    cv2.rectangle(img, (x+125, y), (x , y+50), (255, 255, 255), 1)
    ball=dy,dx
    y = y + dy
    x = x + dx
    if y >= 450 or y <= 0:
        dy = dy * (-1)
        dx = dx * (1)
    if x >= 500 or x <= 0:
        dy = dy * (1)
        dx = dx * (-1)



    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()