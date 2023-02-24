import requests

img_path='./test-imgs/send_img.jpg'
img = open(img_path,'rb')
files = {"image":img}
#访问服务
res = requests.post("http://lcfclc.cn:10000/upload",files=files)
print(res.text)
