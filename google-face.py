import io
import os
 
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Jake\\Documents\\beachhacks2019\\googlecloudapi\\BeachHacks2019-858fb3db009f.json"
# Instantiates a client

def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')
    class moodPoint:
        def __init__(self, anger, joy, surprise):
            self.anger = anger
            self.joy = joy
            self.surprise = surprise

    for face in faces:
        mood = moodPoint(face.anger_likelihood,face.joy_likelihood,face.surprise_likelihood)
    return mood


