import cv2

harcascade = 'model/haarcascade_frontalface_default.xml'

def detect_faces_image(image_path):
  
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return
    
    face_cascade = cv2.CascadeClassifier(harcascade)
    
    if face_cascade.empty():
        print(f"Error: Haar cascade file not found at {harcascade}")
        return
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    resized_img = cv2.resize(img, (800, 600))
    
    cv2.imshow("Detected Faces", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_faces_image(r"C:\Users\aksha\.APersonal\Achivements\Photo.jpg")


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

cap.set(3, 640)  
cap.set(4, 480)  

while True:
    success, img = cap.read()
    
    if not success:
        print("Error: Could not read frame.")
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier(harcascade)
    
    if face_cascade.empty():
        print(f"Error: Haar cascade file not found at {harcascade}")
        break

    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("Face Detection", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
