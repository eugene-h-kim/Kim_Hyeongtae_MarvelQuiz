from components import vars
from PIL import Image


def total(value):
    # do some logic to see which character you selected

    if value == 50:
        vars.character = vars.characters[0]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package

        IronMan = Image.open("iron_man.jpg")
        IronMan.show()


    if value == 100:
        vars.character = vars.characters[1]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package

        DoctorStrange = Image.open("doctor_strange.jpg")
        DoctorStrange.show()
        
    
    if value == 150:
        vars.character = vars.characters[2]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package

        SpiderMan = Image.open("spider_man.jpg")
        SpiderMan.show()
        
    
    if value == 200:
        vars.character = vars.characters[3]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package

        Thor = Image.open("thor.jpg")
        Thor.show()
    