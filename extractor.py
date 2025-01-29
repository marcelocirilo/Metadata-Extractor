from PIL import Image
from PIL.ExifTags import TAGS

class Extractor:
    
    def __init__(self,image_path):
        self.image_path=image_path

    def exif(self):
        try:
            image = Image.open(self.image_path)
            data = image.getexif()
            
            if data:
                for tagid in data:
                    tagname = TAGS.get(tagid, tagid)
                    value = data.get(tagid)
                    print(f"{tagname}: {value}")
            else:
                print("No EXIF data found.")
        except Exception as e:
            print(f"Error reading EXIF data: {e}")