from zipfile import ZipFile
import hashlib
import json
import requests


zipObj = ZipFile('test.zip', 'w')
f = open("test.txt", "x")
zipObj.write('test.txt')
zipObj.setpassword(b"shaked")
zipObj.close()

with open("test.txt","rb") as f:
    f_byte= f.read()
    result = hashlib.sha256(f_byte)
    f = open("filehash.txt", "x")
    f.write(result.hexdigest())
    f.close()

zipObj = ZipFile('filehash.zip', 'w')
zipObj.write('filehash.txt')
zipObj.close()


#upload to google.d:

headers = {"Authorization": "Bearer ## my access_token ##"}
para = {
    "name": "test.zip",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./test.zip", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)