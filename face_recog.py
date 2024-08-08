import cv2
import time
import PIL.Image as PIL
def face():
    video=cv2.VideoCapture(0)
    while True:
        s,frame=video.read()
        cv2.imshow("online",frame)
        if cv2.waitKey(5) & 0XFF == ord(" "):
            #cv2.imwrite("bunny_cap.jpg",frame)
            img=frame
            break
    video.release()
    cv2.destroyAllWindows()
    return PIL.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


'''
face_cascade = cv2.CascadeClassifier()
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
'''
