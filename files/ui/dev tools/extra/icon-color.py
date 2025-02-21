import os
from lxml import etree

def change_svg_color(directory, new_color):
    for filename in os.listdir(directory):
        if filename.endswith(".svg"):
            filepath = os.path.join(directory, filename)
            tree = etree.parse(filepath)
            root = tree.getroot()

            for element in root.iter():
                if 'fill' in element.attrib:
                    element.attrib['fill'] = new_color

            tree.write(filepath)
            print(f"Updated color for {filename}")

directory = "C:/Users/prath/Desktop/light"
new_color = '#393939'  # Your new color
change_svg_color(directory, new_color)

print("All SVG files updated successfully!")
