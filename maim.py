from PIL import Image
from PIL import ImageFilter

class ImageEditor():
    def __init__(self, filename) :
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не найден!')

    def do_flip(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        rotated.save('rotated.jpg')

my_image = ImageEditor('original.jpg')
my_image.open()
my_image.do_flip()
my_image.changed[0].show()