import subprocess
cmd="echo $HOME"
# To create new processes, we can use library functions such as subprocess.Popen().

#  universal_newlines=True flag will give the output in the form of a string.
# In case of your command depend upon the environment variable of the operating system, then only in those cases take shell=True
# In case if your command doesn’t need a new shell, use shell=False.

sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True)
rt = sp.wait()
out,err=sp.communicate()
print(out)

