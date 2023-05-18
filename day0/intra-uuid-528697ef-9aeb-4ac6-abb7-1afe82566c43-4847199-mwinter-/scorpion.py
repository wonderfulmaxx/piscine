import sys
from PIL import Image
from PIL.ExifTags import TAGS

def parse_image_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if exif_data is not None:
            print("Metadata for image:", image_path)
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
        else:
            print("No metadata found for image:", image_path)
            
    except Exception as e:
        print("Error:", str(e))


nb_args = len(sys.argv)

if nb_args < 2:
    print("Too few args")
    sys.exit(1)

counter = 1

while counter < nb_args:
	print()
	print("--------------------------------",sys.argv[counter],"--------------------------------")
	parse_image_metadata(sys.argv[counter])
	counter += 1
	if counter < nb_args:
		print()
		print()
		print()





   