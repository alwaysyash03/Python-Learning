from pathlib import Path

# Absolute path
# c:\User\Desktop\
# user/local/bin
# Relative Path

path = Path("package")
print(path.exists())

# path = Path("dummy")
# print(path.mkdir())

# path = Path("dummy")
# print(path.rmdir())

path = Path()
for files in path.glob("*.*"):
    print(files)