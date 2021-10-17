import pathlib

path = pathlib.Path("/etc/hosts")
print(str(path.exists()))
print(str(path.is_file()))
print(str(path.is_dir()))