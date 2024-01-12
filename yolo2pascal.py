import os
import xml.etree.cElementTree as ET

def create_xml_file(image_name, objects, folder, path, size, out_dir):
    annotation = ET.Element("annotation")
    ET.SubElement(annotation, "folder").text = folder
    ET.SubElement(annotation, "filename").text = image_name

    source = ET.SubElement(annotation, "source")
    ET.SubElement(source, "database").text = "Unknown"

    size_xml = ET.SubElement(annotation, "size")
    ET.SubElement(size_xml, "width").text = str(size[0])
    ET.SubElement(size_xml, "height").text = str(size[1])
    ET.SubElement(size_xml, "depth").text = str(3)

    ET.SubElement(annotation, "segmented").text = "0"

    for obj in objects:
        object_xml = ET.SubElement(annotation, "object")
        ET.SubElement(object_xml, "name").text = obj["name"]
        ET.SubElement(object_xml, "pose").text = "Unspecified"
        ET.SubElement(object_xml, "truncated").text = str(0)
        ET.SubElement(object_xml, "difficult").text = str(0)
        bndbox = ET.SubElement(object_xml, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(obj["xmin"])
        ET.SubElement(bndbox, "ymin").text = str(obj["ymin"])
        ET.SubElement(bndbox, "xmax").text = str(obj["xmax"])
        ET.SubElement(bndbox, "ymax").text = str(obj["ymax"])

    tree = ET.ElementTree(annotation)
    with open(os.path.join(out_dir, image_name.replace(".png", ".xml")), 'w') as f:
        tree.write(os.path.join(out_dir, image_name.replace(".png", ".xml")))

from PIL import Image
def convert_yolo_to_voc(yolo_path, voc_path, class_mapping):
    for filename in os.listdir(yolo_path):


        if filename.endswith('.txt') and filename != 'classes.txt':
            image_name = filename.split('.')[0] + '.png' 
            image_size = Image.open(os.path.join(yolo_path, image_name)).size
            shutil.copy(os.path.join(yolo_path, image_name), os.path.join(voc_path, image_name))
            with open(os.path.join(yolo_path, filename), 'r') as file:
                lines = file.readlines()
                objects = []
                for line in lines:
                    parts = line.strip().split()
                    class_id = int(parts[0])
                    x_center = float(parts[1]) * image_size[0]
                    y_center = float(parts[2]) * image_size[1]
                    width = float(parts[3]) * image_size[0]
                    height = float(parts[4]) * image_size[1]

                    xmin = int(x_center - width / 2)
                    ymin = int(y_center - height / 2)
                    xmax = int(x_center + width / 2)
                    ymax = int(y_center + height / 2)

                    objects.append({
                        "name": class_mapping[class_id],
                        "xmin": xmin,
                        "ymin": ymin,
                        "xmax": xmax,
                        "ymax": ymax
                    })
        
                image_name = filename.replace(".txt", ".png")  # Assuming JPG images
                create_xml_file(image_name, objects, "folder_name", "path_to_image", image_size, voc_path)

# Class Mapping
class_mapping = {0: 'roi',
 1: 'part1_w11',
 2: 'part1_w10',
 3: 'part1_w26',
 4: 'part1_w2',
 5: 'part1_w8',
 6: 'part1_w14',
 7: 'part1_w15',
 8: 'part1_w16',
 9: 'part1_w17',
 10: 'part1_w30',
 11: 'part1_w12',
 12: 'part1_w13',
 13: 'part1_w28',
 14: 'part1_w_leg_connector',
 15: 'part1_w_leg_bot',
 16: 'part1_w_leg_top',
 17: 'part1_w6',
 18: 'part1_w21',
 19: 'part1_w35',
 20: 'part1_w37',
 21: 'part1_w38',
 22: 'part1_w18',
 23: 'part1_w31',
 24: 'part1_w23',
 25: 'part1_w_start',
 26: 'part1_w36',
 27: 'part1_w7',
 28: 'part1_w34',
 29: 'part1_w29',
 30: 'part1_w22',
 31: 'part1_w4',
 32: 'part1_w1',
 33: 'part1_w9',
 34: 'part1_w3',
 35: 'part1_w19',
 36: 'part1_w24',
 37: 'part1_w32',
 38: 'part1_w25',
 39: 'part1_w27',
 40: 'part1_w33',
 41: 'part1_w5',
 42: 'part1_w20',
 43: 'part2_wa6',
 44: 'part2_wa5',
 45: 'part2_w20',
 46: 'part2_w29',
 47: 'part2_w27',
 48: 'part2_w25',
 49: 'part2_w23',
 50: 'part2_w6',
 51: 'part2_w5',
 52: 'part2_w19',
 53: 'part2_w16',
 54: 'part2_w15',
 55: 'part2_w28',
 56: 'part2_w3',
 57: 'part2_w4',
 58: 'part2_w13',
 59: 'part2_w32',
 60: 'part2_w1',
 61: 'part2_w2',
 62: 'part2_w24',
 63: 'part2_w26',
 64: 'part2_w34',
 65: 'part2_w31',
 66: 'part2_w12',
 67: 'part2_w7',
 68: 'part2_w9',
 69: 'part2_w8',
 70: 'part2_w30',
 71: 'part2_w11',
 72: 'part2_w10',
 73: 'part4_w5',
 74: 'part4_w8',
 75: 'part4_w10',
 76: 'part4_w11',
 77: 'part4_w12',
 78: 'part4_w21',
 79: 'part4_w22',
 80: 'part4_w9',
 81: 'part4_w16',
 82: 'part4_w27',
 83: 'part4_w24',
 84: 'part4_w25',
 85: 'part4_w13',
 86: 'part4_w_start',
 87: 'part4_w26',
 88: 'part4_w19',
 89: 'part4_w_end',
 90: 'part4_w20',
 91: 'part4_w4',
 92: 'part4_w3',
 93: 'part4_w6',
 94: 'part4_w14',
 95: 'pat4_w1',
 96: 'part4_w23',
 97: 'part4_w2',
 98: 'part3_w1',
 99: 'part3_w23',
 100: 'part4_w28',
 101: 'part3_w12',
 102: 'part3_w24',
 103: 'part3_w25',
 104: 'part3_w19',
 105: 'part3_w20',
 106: 'part3_w11',
 107: 'part3_w13',
 108: 'part3_w26',
 109: 'part3_w6',
 110: 'part3_w5',
 111: 'part3_w4',
 112: 'part3_w3',
 113: 'part3_w9',
 114: 'part3_w8',
 115: 'part3_w15',
 116: 'part3_w16',
 117: 'part3_w10',
 118: 'part3_w28',
 119: 'part3_w27',
 120: 'part3_w7'}
# Example usage
yolo_path = '/Users/andriizelenko/qvuer7/projects/adient/v6/f4480748-ef7b-4e1f-84b2-4de9b4d0752d'
voc_path = '/Users/andriizelenko/qvuer7/projects/adient/v6_voc/p4' # Replace with your desired output directory for VOC labels
# Replace with the actual size of your images
if os.path.exists(voc_path) :
    pass 
else:
    os.mkdir(voc_path)
convert_yolo_to_voc(yolo_path, voc_path, class_mapping)