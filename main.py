import cv2
import numpy as np
from insightface.app import FaceAnalysis

print("Loading ArcFace model...")

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

known_image = cv2.imread("known_person.jpg")

if known_image is None:
    print("Error: known_person.jpg not found!")
    exit()

known_faces = app.get(known_image)

if len(known_faces) == 0:
    print("No face detected in known_person.jpg")
    exit()

known_embedding = known_faces[0].embedding

print("Known face loaded successfully!")
print("Starting webcam... Press 'q' to quit.")


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not access webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break


    faces = app.get(frame)

    for face in faces:

        embedding = face.embedding


        similarity = np.dot(
            known_embedding,
            embedding
        ) / (
            np.linalg.norm(known_embedding)
            * np.linalg.norm(embedding)
        )


        if similarity > 0.5:
            name = "Joyce"
        else:
            name = "Unknown"


        x1, y1, x2, y2 = map(int, face.bbox)


        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )


        cv2.putText(
            frame,
            f"{name} ({similarity:.2f})",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Detection & Recognition using ArcFace", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
