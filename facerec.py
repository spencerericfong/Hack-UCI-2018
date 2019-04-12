# This program will print out the names of anyone it recognizes to the console.

# To run this, you need a Raspberry Pi 2 (or greater) with face_recognition and
# the picamera[array] module installed.
# You can follow this installation instructions to get your RPi set up:
# https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65

import face_recognition
import picamera
import numpy as np
import os
        

def set_familiar_face(name: str, name_of_pic: str) -> None:
    '''If user indicates the stranger is friendly, their face is added to the database'''
    image_encodings[name] = face_recognition.face_encodings(face_recognition.load_image_file("new_face.jpg"))[0]
    os.rename(name_of_pic+".jpg", name+".jpg")
    whitelist[name] = face_recognition.face_encodings(face_recognition.load_image_file(name_of_pic + '.jpg'))[0]     


def send_alert_info(name: str, on_blacklist=True) -> ("path", bool):
    '''If someone is detected on the camera, an alert is sent to the user'''
    if name == '':
        unknown = next(unknown_num)
        os.rename("new_face.jpg", '/home/pi/Desktop/HackUCI/blacklisted/unknown' + str(unknown) + '.jpg')
        blacklist['unknown' + str(unknown)] = face_recognition.face_encodings(face_recognition.load_image_file("/home/pi/Desktop/HackUCI/blacklisted/" + 'unknown' + str(unknown) + '.jpg'))[0]
        return (os.path.abspath('unknown' + str(unknown) + '.jpg'), blacklist)
    else:
        return (os.path.abspath(name + '.jpg'), blacklist)


def unknown_gen() -> int:
    count = 0
    while True:
        yield count
        count += 1
        
    

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

#camera.start_preview()

# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")
whitelist = {}
whitelist_faces = os.listdir("/home/pi/Desktop/HackUCI/whitelisted/")
for face in whitelist_faces:
    whitelist[os.path.splitext(face)[0]] = face_recognition.face_encodings(face_recognition.load_image_file("/home/pi/Desktop/HackUCI/whitelisted/" + face))[0]

blacklist = {}
blacklist_faces = os.listdir("/home/pi/Desktop/HackUCI/blacklisted/")
for face in blacklist_faces:
    blacklist[os.path.splitext(face)[0]] = face_recognition.face_encodings(face_recognition.load_image_file("/home/pi/Desktop/HackUCI/blacklisted/" + face))[0]

# Initialize some variables
face_locations = []
face_encodings = []
unknown_num = unknown_gen()

while True:
    name = ''
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")
    camera.capture("new_face.jpg")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        check_both = True
        # See if the face is a match for the known face(s)
        for person in whitelist.keys():
            match = face_recognition.compare_faces([whitelist[person]], face_encoding)
            if match[0]:   
                name = person
                check_both = False
                send_alert_info(name, False)
                print("Safe! I see someone named {}!".format(name))
        if check_both:
            stranger_danger = True
            for person in blacklist.keys():
                match = face_recognition.compare_faces([blacklist[person]], face_encoding)
                if match[0]:   
                    name = person
                    stranger_danger = False
                    print("Danger! I see someone named {}!".format(name))
                    break
            if stranger_danger:
                print("Danger! I see a stranger!")
            send_alert_info(name)
                
        

#camera.stop_preview()
