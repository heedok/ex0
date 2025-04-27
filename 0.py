import cv2
# Haar Cascade 파일 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

print("dd")

#image1 = cv2.imread('1.png') #나루토 이미지
#image2 = cv2.imread('a.jpg') #사과 이미지
image1 = cv2.imread('winter1.jpg') #윈터 이미지, winter.jpg  winter2.png

#image2_resize = cv2.resize(image2, None,fx=0.5,fy=0.5)

#cv2.imshow('111',image1)
#cv2.imshow('222',image2_resize)


# 이미지를 그레이스케일로 변환 (얼굴 감지 성능 향상)
gray_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# 얼굴 감지
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=5, minSize=(40, 40))
eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), maxSize=(50, 50))

# 감지된 얼굴에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(image1, (x, y), (x + w, y + h), (50, 0, 200), 2)

for (x, y, w, h) in eyes:
    cv2.rectangle(image1, (x, y), (x + w, y + h), (200, 0, 50), 2)

cv2.imshow('Gray image', gray_image)
cv2.imshow('Face Detection', image1)

# 키입력 기다림, 창닫기
cv2.waitKey()
cv2.destroyAllWindows() 