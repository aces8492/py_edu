#read and show information of 24bit bitmap image

import sys
import struct

#file_name = input("please input file name : ")
file_name = "test1.bmp"

#file read by "binary" type
try:
    bitmap_data = open(file_name,"rb").read()
except IOError:
    print("file \"{0}\" is not found".format(file_name)) 
    sys.exit()

print(file_name)
#header_buf = bitmap_data.readline()
# print("file type is {0}".format(hader_buf))
print(bitmap_data)
#print(bitmap_data[:2])
if "BM" == bitmap_data[:2].decode(encoding="utf-8"):
    print("BMP")
else:
    print("not BMP")
