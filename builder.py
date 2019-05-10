import xml.etree.ElementTree as xml

def builder():
    filename = './anilistanime.xml'

    root = xml.Element("Users")
    userelement = xml.Element("user")
    root.append(userelement)