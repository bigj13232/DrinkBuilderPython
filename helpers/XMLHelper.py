import xml.etree.ElementTree as gfg 
from xml.etree import ElementTree

class XMLHelper():
    @staticmethod
    def createXML(directions):
        drinkDirectionsXML = None

        root = gfg.Element('Directions')

        loopCount = 1
        for direction in directions:
            step = gfg.Element("Step" + str(loopCount))
            step.text = direction
            root.append(step)
            loopCount+=1
        
        tree = gfg.ElementTree(root)

        drinkDirectionsXML = ElementTree.tostring(root, encoding='unicode')

        return drinkDirectionsXML

    @staticmethod
    def readXML(xml):
        xmlToDirections = None

        tree = gfg.fromstring(xml)
        root = tree.getroot()
        
        for child in root:
            print(child.tag, child.attrib)



