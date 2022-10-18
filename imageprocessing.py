import concurrent.futures
import time
from PIL import Image, ImageFilter
from itertools import repeat

press_photos = []


def process_images_sequential(img_names):
    size = (1200, 1200)

    for img_name in img_names:
        img = Image.open(img_name)
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size)
        img.save(f'processed/{img_name}')
        print(f'{img_name} was processed...')


def process_images_parallel(img_names):
    size = (1200, 1200)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names, repeat(size))


def process_image(img_name, size):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


def print_duration(func, *args):
    start = time.time()
    func(*args)
    finish = time.time()
    print(f'Finished in {round(finish-start, 2)} second(s)')


if __name__ == '__main__':
    # print_duration(process_images_sequential, press_photos)
    print_duration(process_images_parallel, press_photos)
