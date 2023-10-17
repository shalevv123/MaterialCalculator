import Material
from io import BytesIO
import sys

def get_image_data(path):
    with open(path, "rb") as image_file:
        image_data = BytesIO(image_file.read())
        return image_data.getvalue()

if __name__ == '__main__':
    with open('images.txt', 'w') as f:
        for material in Material.material_list:
            path = "./images/" + material.names[0].replace(" ", "_") + ".png"
            sys.stdout = f
            print(get_image_data(path))
    sys.stdout = sys.__stdout__

