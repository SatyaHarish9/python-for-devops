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

Regular expressions:

\d ---> Matches any digit.
. ---> Matches anything except new line.

Character Class [] ---> If you would like to match a specific class
{k} --> exact k number of occurences.

^ - start of line
$ - end of line

\s ---> It points to space.

\w : sequence of word-like characters [a-zA-Z0–9_] that are not space
\d: Any numeric digit[0–9]
\s: whitespace characters(space,newline,tab)
\D: match characters that are NOT numeric digits
\W: match characters that are NOT words,digit or underscore
\S: match characters that are NOT spaces,tab or newline
