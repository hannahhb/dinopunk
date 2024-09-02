from PIL import Image

# Load the image
# image = Image.open("images/dot.png")

# # Resize the image
# resized_image = image.resize((40,40))

# # Save the resized image
# resized_image.save("images/dot.png")

from PIL import Image, ImageOps

def add_padding(image_path, output_path, target_width, target_height):
    # Open the original image
    image = Image.open(image_path)
    original_width, original_height = image.size

    # Calculate padding sizes
    padding_width = (target_width - original_width) // 2
    padding_height = (target_height - original_height) // 2

    # Add padding to the image
    padded_image = ImageOps.expand(image, (padding_width, padding_height, padding_width, padding_height), fill="black")

    # Resize if necessary to meet exact target size
    padded_image = padded_image.resize((target_width, target_height))

    # Save the new image
    padded_image.save(output_path)

# Example usage
add_padding("gui/main_menu.png", "gui/main_menu.png", 1920, 1080)
