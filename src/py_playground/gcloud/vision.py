from google.cloud import vision
from google.cloud.vision import types


def recognize(image_content):
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image_content)
    response = client.annotate_image({
        'image': image,
        'features': [{'type': vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION}]
    })
    return response
