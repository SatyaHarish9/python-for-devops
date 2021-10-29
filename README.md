# python-for-devops


Subprocess Module:

Subprocess module allows to spawn new processes, connect to their input/output/error pipes. This module intends to replace several older modules and functions.

Example: In case of os module, a command output cannot be captured and only returned exit code is captured. By using subprocess module, we can capture the command output.

Syntax: 

sp = subprocess.Popen(command,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

Platform Module:

Platform module can be used to access the underlying data such as operating system interpreter version and the hardware.

getpass Module:

GetPass Module can be used to get information about users and passwords.