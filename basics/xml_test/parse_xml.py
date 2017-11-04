import sys
from glob import glob
import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    print("in parser")
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    print(root.tag,root.attrib)

if sys.argv[1:]:
    for index,arg in enumerate(sys.argv[1:]):
        for filename in glob(arg):
            try:
                parseXML(filename)
                print(filename)
            except Exception as inst:
                print("Can't read input file in {0}".format(filename))


