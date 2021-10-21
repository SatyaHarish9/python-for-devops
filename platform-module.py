import os
import platform

if platform.system() == "Linux":
    os.system("ls")
elif platform.system() == "Windows":
    os.system("dir")
else:
    print("Unsupported operating system")