import requests
import xml.etree.ElementTree as ET
import os

ET.register_namespace('', "http://www.w3.org/2000/svg")

url = "https://skillicons.dev/icons?i=python,c,cpp,js,ts,react,nodejs,express,mongodb,postgresql,aws,docker,git,linux&perline=7"

def generate_animated_svg():
    r = requests.get(url)
    if r.status_code != 200:
        print("Failed to fetch SVG")
        return
        
    svg_content = r.text
    root = ET.fromstring(svg_content)

    # 1. Add CSS animations
    style = ET.Element("style")
    style.text = """
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        .icon-float {
            animation: float 4s ease-in-out infinite;
        }
    """
    root.insert(0, style)

    # 2. Wrap each icon group in an animated group
    # We find all top-level <g> tags
    for i, g in enumerate(root.findall("{http://www.w3.org/2000/svg}g")):
        # create new inner group
        inner_g = ET.Element("g")
        inner_g.attrib["class"] = "icon-float"
        
        # generate staggered delay based on x, y position roughly, or just index
        delay = - (i * 0.3)
        inner_g.attrib["style"] = f"animation-delay: {delay}s;"
        
        # move all children from outer <g> to inner <g>
        for child in list(g):
            inner_g.append(child)
            g.remove(child)
            
        g.append(inner_g)
        
    # Also adjust the SVG height slightly to make room for the float without clipping
    height_str = root.attrib.get('height', '300')
    height = float(height_str.replace('px', ''))
    root.attrib['height'] = str(height + 20)

    # Save the modified SVG
    with open("tech-stack.svg", "wb") as f:
        f.write(ET.tostring(root))

if __name__ == "__main__":
    generate_animated_svg()
