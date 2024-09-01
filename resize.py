from PIL import Image

# Load the image
image = Image.open("images/dot.png")

# Resize the image
resized_image = image.resize((40,40))

# Save the resized image
resized_image.save("images/dot.png")