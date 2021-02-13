import sys
import os
from PIL import Image

# Getting args from command line
print(sys.argv)
image_folder, output_folder = sys.argv[1], sys.argv[2]

# Checking Whether New exists or not
if not os.path.exists(output_folder):
    os.mkdir(output_folder)


# Looping Through Pokedex and Converting

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print("ALL DONE!!")