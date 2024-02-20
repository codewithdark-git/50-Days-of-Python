import pyshorteners

url = input("Enter The URl : ")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(url)

print("The shortener URl : "+ short_url)