from PIL import Image
image = Image.open("lenna.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.split()
shift = 50
red_cropped = red.crop((shift, 0, red.width, red.height))
blue_cropped = blue.crop((0, 0, red.width - shift, red.height))
green_cropped = green.crop((shift / 2, 0, red.width - shift / 2, red.height))
final_image = Image.merge("RGB", (red_cropped, green_cropped, blue_cropped))
final_image.save("final_glitch.jpg")
max_size = (80, 80)
final_image.thumbnail((80, 80))
final_image.save("avatar.jpg")