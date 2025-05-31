import cv2

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap=cv2.VideoCapture(0)   # actioncam 연결 사용 예제

while True:
    ret,frame=cap.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #얼굴찾기
    faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)
    #얼굴 네모 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 0, 200), 2)
    
    
    # 눈 찾기
    eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50), maxSize=(150, 150))
    #눈 네모 그리기
    roi_color = frame[y:y + h, x:x + w]
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        

    cv2.imshow('Live cam',frame)
    
    if not ret:
        break
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
   
cap.release()
cv2.destroyAllWindows()