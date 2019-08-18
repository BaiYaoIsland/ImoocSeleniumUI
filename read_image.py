import pytesseract
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
# image = Image.open("./screenshot/imooc1.png")
# text = pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-4", "100046", "ea216e4d0d65459abced82ac546f65d2")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", './screenshot/test1.png')  # 文件上传时设置
res = r.post()
res.json()['showapi_res_body']['Result']
print(res.text)