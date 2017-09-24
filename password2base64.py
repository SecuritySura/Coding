# written by SecuritySura 
#To run, Just Simply type : python password2base64.py
# make sure to replace file-with-password-list.txt with your password file name. 
import base64
for line in open("file-with-password-list.txt", "r").readlines():print base64.b64encode(bytes(line).encode("utf-8"))
