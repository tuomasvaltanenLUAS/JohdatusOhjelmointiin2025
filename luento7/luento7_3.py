# muista asentaa:
# pip install Pillow
# tai käytä graafista asennusta
# koodissa kuitenkin käytetään aina sitten PIL
# HUOM! älä asenna PIL ikinä, vaan aina Pillow!
from PIL import Image, ImageDraw

img = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(img)

draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))

img.save("pillow_test.png")