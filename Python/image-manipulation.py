""" image manipulation into black and white """

from PIL import Image

# Open the image
img = Image.open("image.jpg")

# Convert the image to greyscale
img = img.convert("L")

# Save the converted image
img.save("greyscale_image.jpg")

# Show the converted image
img.show()