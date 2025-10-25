# muista asentaa:
# pip install Pillow
# tai käytä graafista asennusta
# koodissa kuitenkin käytetään aina sitten PIL
# HUOM! älä asenna PIL ikinä, vaan aina Pillow!
from PIL import Image, ImageDraw

# luodaan uusi kuva, koko 500 x 300 (sivuttain x pystysuunta)
# color on väriarvo => RGB => Red, Green, Blue
img = Image.new('RGB', (500, 300), (73, 109, 137))

# luodaan piirto-objekti, jonka kautta kuvaan voidaan piirtää lisää asioita
draw = ImageDraw.Draw(img)

# "piirretään" tekstiä kuvaan, kohta on 10, 10 vasemmasta ylänurkasta
# matematiikassa on totuttu että origo 0,0 on vasen alanurkka
# mutta tietokoneissa ja ohjelmoinnisa, 0, 0 on vasen ylärurkka
# eli esim. 100, 200 tarkoittaa kirjaimellisesti:
# 100 pikseliä oikealle ja 200 pikseliä alas
# ks. https://www.plus2net.com/python/images/pil-text-anchor.jpg
draw.text((30, 40), "Hello World!", fill=(255, 255, 0))

# piirretään ympyrä (käyttämällä ellipsityökalua)
# xy = aloituspiste on kohdassa 100,100 => oikea alanurkka on kohdassa 200,200
# tarkoittaa että ellipsin koko on 100 x 100 (eli 200 - 100, 200 - 100)
draw.ellipse((100, 100, 200, 200), fill=(238, 140, 255), outline=(0, 0, 0))

# tallennetaan kuva tiedostoon
img.save("pillow_test.png")