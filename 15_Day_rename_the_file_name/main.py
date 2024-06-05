import os

files = os.listdir("images")
i = 1
for file in files:
  if file.endswith(".jpg"):
    print(file)
    os.rename(f"images/{file}", f"images/{i}.png")
    i = i + 1



