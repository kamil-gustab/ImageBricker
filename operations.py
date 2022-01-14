import config
from PIL import Image

def rotate_image(angle):
    file_name = config.image_path
    try:
        with Image.open(file_name) as img:
            img = img.rotate(angle)
            extension = file_name.split(".",-1)
            config.temp_image_path = f"imgs/temp/temp_image.{extension[-1]}"
            img.save(config.temp_image_path)
    except IOError:
        pass

def return_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            sizes = img.size
            return sizes
    except IOError:
        pass

def scale_image(image_path, target_width):
    try:
        with Image.open(image_path) as img:
            width_percent = (target_width / float(img.size[0]))
            target_height = int((float(img.size[1]) * float(width_percent)))
            img = img.resize((target_width, target_height), Image.LANCZOS)
            extension = image_path.split(".", -1)
            config.temp_image_path = f"imgs/temp/temp_image.{extension[-1]}"
            img.save(config.temp_image_path)
    except IOError:
        pass

def open_full_image(image_path):
    try:
        with Image.open(image_path) as img:
            img.show()
    except IOError:
        pass

def apply_brick_effect(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = return_image_size(image_path)
            if height <= 16:
                brick_file_path = "imgs/16x16.png"
            elif height <= 32:
                brick_file_path = "imgs/32x32.png"
            elif height <= 64:
                brick_file_path = "imgs/64x64.png"
            elif height <= 128:
                brick_file_path = "imgs/128x128.png"
            elif height <= 256:
                brick_file_path = "imgs/256x256.png"
            else:
                brick_file_path = "imgs/512x512.png.png"
            img = img.resize((width*25, height*25), Image.NEAREST)  # resizing to apply effect
            with Image.open(brick_file_path) as brick_image:
                img.paste(brick_image, (0, 0), mask=brick_image)
                img.save(config.temp_image_path)
    except IOError:
        pass

def save_photo(source_path, target_path):
    try:
        with Image.open(source_path) as img:
            if target_path != "imgs/default.png":
                img.save(target_path)
    except IOError:
        pass
