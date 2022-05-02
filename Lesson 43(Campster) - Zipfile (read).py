from re import X
import zipfile

exampleZip = zipfile.ZipFile("new_2.zip")
exampleZip.namelist()
exampleZip.close 

print("Who?")
