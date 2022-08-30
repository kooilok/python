from PIL import Image
from PIL import ImageFilter

#открой файл с оригиналом картинки
with Image.open('original.jpg') as original:
    print('Размер:', original.size)
    print('Формат:', original.format)
    print('Тип:', original.mode)
#сделай оригинал изображения чёрно-белым
    pic_gray = original.convert('L')
    pic_gray.save('gray.jpg')
    print('Размер:', pic_gray.size)
    print('Формат:', pic_gray.format)
    print('Тип', pic_gray.mode)
    pic_gray.show()
#сделай оригинал изображения размытым
    pic_blur = original.filter(ImageFilter.BLUR)
    pic_blur.save('blur.jpg')
    print('Размер:', pic_blur.size)
    print('Формат:', pic_blur.format)
    print('Тип:', pic_blur.mode)
    pic_blur.show()
#поверни оригинал изображения на 180 градусов
    pic_flip = original.transpose(Image.ROTATE_180)
    pic_flip.save('flip.ipg')
    print('Размер:', pic_flip.size)
    print('Формат:', pic_flip.format)
    print('Тип:', pic_flip.mode)
    pic_flip.show