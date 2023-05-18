import os
from datetime import datetime
from functools import cmp_to_key

dateformat = '%y-%m-%d_%H-%M-%S'

def isAfter(a, b):
	a = a.split(".")[1] + "-" + a.split(".")[2]
	b = b.split(".")[1] + "-" + b.split(".")[2]
	aD = datetime.strptime(a, dateformat)
	bD = datetime.strptime(b, dateformat)
	if aD < bD:
		return -1
	elif aD > bD:
		return 1
	else:
		return 0

files = [v for v in os.listdir() if v.endswith(".avi") and len(v.split("."))==4]
files = sorted(files, key=cmp_to_key(isAfter))

path = os.getcwd().replace("/mnt/c/", "C:\\").replace("/", "\\")

content = f"""VirtualDub.video.SetMode(0);
VirtualDub.audio.SetMode(0);\n
VirtualDub.Open(U"{path}\{files[0]}");\n"""

for avi in files[1:]:
	content = content + f"VirtualDub.Append(U\"{path}\{avi}\");\n"

out = input("Name der Datei: ")
if len(out.strip()) == 0:
	out = "out"
content = content + f"\nVirtualDub.SaveAVI(U\"{path}\{out}.avi\");\nVirtualDub.Close();"

with open("script.vcf", "w") as f:
	f.write(content)


