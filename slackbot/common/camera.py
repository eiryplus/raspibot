import os
import math
from time import sleep
from datetime import datetime

from picamera import PiCamera

PX_8M = (3264, 2448)
PX_2M = (3264//2, 2448//2)
PX_1M = (int(PX_2M[0]//1.414), int(PX_2M[1]//1.414))

HOME_DIR = r'/home/pi/picture/'


def take_a_photo(resolution=PX_1M, rotation=180):
    file_name = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    file_path = os.path.join(HOME_DIR, file_name)
    with PiCamera() as camera:
        camera.resolution = resolution
        camera.rotation = rotation
        # カメラを起動して2秒間は内部電圧が安定しないらしくスリープさせて電圧が落ち着くのをまつ
        sleep(2)
        camera.capture(file_path)
    return file_path


if __name__ == '__main__':
    take_a_photo()
