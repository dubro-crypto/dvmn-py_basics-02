from PIL import Image

image = Image.open("lenna.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.split()
shift = 50
red_left = red.crop((shift, 0, red.width, red.height))
red_middle = red.crop((shift / 2, 0, red.width - shift / 2, red.height))
red_final = Image.blend(red_left, red_middle, 0.5)
blue_right = blue.crop((0, 0, blue.width - shift, blue.height))
blue_middle = blue.crop((shift / 2, 0, blue.width - shift / 2, blue.height))
blue_final = Image.blend(blue_right, blue_middle, 0.5)
green_final = green.crop((shift / 2, 0, green.width - shift / 2, green.height))
final_image = Image.merge("RGB", (red_final, green_final, blue_final))
final_image.save("final_glitch.jpg")
final_image.thumbnail((80, 80))
final_image.save("avatar.jpg")