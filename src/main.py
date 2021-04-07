import pyimgur, json, sys, pyperclip

from .color import *
from .intro import intro

class Main:
    def app():
        # config
        cfg_path = (r"./config/cfg.json")
        with open(cfg_path) as data:
            a = json.load(data)
        TOKEN = a["client_id"]
        im = pyimgur.Imgur(TOKEN)

        # intro
        sys.stdout.write(intro())
        print('    Github Profile - https://github.com/lemun \n\n\n')

        # program start here
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Drag' + fy + ' & ' + fg +'Drop your image in this terminal and press ' + fr + 'ENTER \n')
        instruction = 'Drop here: '
        img_path = input(instruction) # asks for the img path
        uploaded_image = im.upload_image(img_path, title="Automatically uploaded with PyImgur") # uploads to imgur
        image_link = uploaded_image.link

        pyperclip.copy(image_link) # copies the image link to yours clipboard
        
        print(fg + '\nLINK: ' + fb + sb + image_link + sb + fg + ' ( Automatically added to your clipboard )') # prints the image link and informs you it's in your clipboard