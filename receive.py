from flask import Flask, request
from PIL import Image
import time
app = Flask(__name__)

img_path = './test-imgs/receive_img.jpg'

@app.route('/upload', methods=['POST'])
def upload_image():
    print("1")
    img = request.files['image']
    img.save(img_path)
    print("2")
    return "sucess!"

if __name__ == '__main__':
    # 将服务器的 IP 地址设置为公网 IP，端口号为 10000
    app.run(host='0.0.0.0', port=10000)
