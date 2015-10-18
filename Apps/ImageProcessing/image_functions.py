import urllib, cStringIO
from PIL import Image

def return_image_dimensions(url):
    url_resource = urllib.urlopen(url).read()
    file = cStringIO.StringIO(url_resource)
    img = Image.open(file)
    (width, height) = img.size
    return dict(width = width, height = height, size = len(url_resource))

