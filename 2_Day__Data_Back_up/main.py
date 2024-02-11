import gofile as go


_server = go.getServer()
print(_server)
filename = input("Enter File Name : ")
url = go.uploadFile(filename)
print("Download:", url["downloadPage"])

