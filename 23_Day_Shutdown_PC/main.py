import os 

shutdown = 'y' #input("Shutdown your PC ? (y/n): ")

if shutdown=='n':
    exit()
else:
    os.system("shutdown /s /t 1")
