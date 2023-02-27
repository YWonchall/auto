import requests
from picamera import PiCamera


img_path='./test-imgs/send_img.jpg'
camera = PiCamera()
camera.start_preview()
while True:
    camera.capture(img_path,quality=5)
    img = open(img_path,'rb')
    files = {"image":img}
    # 访问服务
    res = requests.post("http://lcfclc.cn:10000/upload",files=files)
    print(res.text)
