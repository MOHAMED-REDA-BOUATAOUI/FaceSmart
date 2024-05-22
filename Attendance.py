import time

import face_recognition
import cv2
import numpy as np
import datetime
import database

# Définition de la fonction pour enregistrer l'horaire de l'employé dans la base de données
def record_attendance(employee_name):
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    database.insert_attendance(employee_name, current_time)

video_capture = cv2.VideoCapture(0)

# Chargement des visages connus et de leurs noms
known_face_encodings = []
known_face_names = []

# Ajoutez les visages et noms connus
reda_image = face_recognition.load_image_file("C:\\Users\\pc\\Desktop\\PFA\\images\\reda.jpg")
reda_face_encoding = face_recognition.face_encodings(reda_image)[0]
known_face_encodings.append(reda_face_encoding)
known_face_names.append("Mohamed Reda Bouataoui")

hamza_image = face_recognition.load_image_file("C:\\Users\\pc\\Desktop\\PFA\\images\\hamza.jpg")
hamza_face_encoding = face_recognition.face_encodings(hamza_image)[0]
known_face_encodings.append(hamza_face_encoding)
known_face_names.append("Hamza Elaatifi")
face_locations = []
face_encodings = []
face_names = []

process_this_frame = True

while True :
    ret, frame = video_capture.read()

    if process_this_frame:
        # Réduire la taille du cadre pour améliorer les performances
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

        # Trouver les emplacements et les encodages des visages dans le cadre actuel
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # Initialisez la liste des noms de visage pour ce cadre
        face_names = []
        for face_encoding in face_encodings:
            # Comparer les visages avec les visages connus
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Si un visage connu est trouvé, enregistrez l'horaire de l'employé
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                # Enregistrez l'horaire de l'employé dans la base de données
                record_attendance(name)


            face_names.append(name)

    process_this_frame = not process_this_frame

    # Affichez les résultats
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Redimensionnez les emplacements de visage pour le cadre complet
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 10), font, 0.8, (255, 255, 255), 1)

    cv2.imshow('FACESMART', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()