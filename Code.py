import cv2

# Path to Haar Cascade XML file
harcascade = "model/haarcascade_frontalface_default.xml"

def detect_faces_image(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return
    
    # Load the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(harcascade)
    
    # Ensure the Haar Cascade was loaded correctly
    if face_cascade.empty():
        print(f"Error: Haar cascade file not found at {harcascade}")
        return
    
    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Resize the image for display
    resized_img = cv2.resize(img, (800, 600))
    
    # Display the image with detected faces
    cv2.imshow("Detected Faces", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test the face detection on an image
detect_faces_image(r"C:\Users\aksha\.APersonal\Achivements\Photo.jpg")


# Real-time Face Detection using Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set the video frame width and height
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while True:
    # Read a frame from the webcam
    success, img = cap.read()
    
    if not success:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Load the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(harcascade)
    
    if face_cascade.empty():
        print(f"Error: Haar cascade file not found at {harcascade}")
        break

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the video frame with detected faces
    cv2.imshow("Face Detection", img)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
