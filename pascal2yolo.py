import os
import xml.etree.ElementTree as ET

def convert_coordinates(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_voc_to_yolo(voc_path, yolo_path, class_mapping):
    for file in os.listdir(voc_path):
        if file.endswith('.xml'):
            tree = ET.parse(os.path.join(voc_path, file))
            root = tree.getroot()
            size = root.find('size')
            width = int(size.find('width').text)
            height = int(size.find('height').text)

            txt_file = open(os.path.join(yolo_path, file.replace('.xml', '.txt')), 'w')
            shutil.copy(os.path.join(voc_path, file.replace('.xml', '.png')), os.path.join(yolo_path, file.replace('.xml', '.png')))
            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls not in class_mapping:
                    continue
                cls_id = class_mapping[cls]
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), 
                     float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                bb = convert_coordinates((width, height), b)
                txt_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

            txt_file.close()

    # Write the class names to classes.txt in the order of their IDs
    with open(os.path.join(yolo_path, 'classes.txt'), 'w') as classes_file:
        for cls_name in sorted(class_mapping, key=class_mapping.get):
            classes_file.write(cls_name + '\n')


# Example usage
voc_path = '/Users/andriizelenko/qvuer7/projects/adient/v6_voc/p4'  
yolo_path = '/Users/andriizelenko/qvuer7/projects/adient/v6_yolo/p4'
if os.path.exists(yolo_path):
    pass
else:
    os.mkdir(yolo_path)
class_mapping = {'roi': 0,
 'part1_w11': 1,
 'part1_w10': 2,
 'part1_w26': 3,
 'part1_w2': 4,
 'part1_w8': 5,
 'part1_w14': 6,
 'part1_w15': 7,
 'part1_w16': 8,
 'part1_w17': 9,
 'part1_w30': 10,
 'part1_w12': 11,
 'part1_w13': 12,
 'part1_w28': 13,
 'part1_w_leg_connector': 14,
 'part1_w_leg_bot': 15,
 'part1_w_leg_top': 16,
 'part1_w6': 17,
 'part1_w21': 18,
 'part1_w35': 19,
 'part1_w37': 20,
 'part1_w38': 21,
 'part1_w18': 22,
 'part1_w31': 23,
 'part1_w23': 24,
 'part1_w_start': 25,
 'part1_w36': 26,
 'part1_w7': 27,
 'part1_w34': 28,
 'part1_w29': 29,
 'part1_w22': 30,
 'part1_w4': 31,
 'part1_w1': 32,
 'part1_w9': 33,
 'part1_w3': 34,
 'part1_w19': 35,
 'part1_w24': 36,
 'part1_w32': 37,
 'part1_w25': 38,
 'part1_w27': 39,
 'part1_w33': 40,
 'part1_w5': 41,
 'part1_w20': 42,
 'part2_wa6': 43,
 'part2_wa5': 44,
 'part2_w20': 45,
 'part2_w29': 46,
 'part2_w27': 47,
 'part2_w25': 48,
 'part2_w23': 49,
 'part2_w6': 50,
 'part2_w5': 51,
 'part2_w19': 52,
 'part2_w16': 53,
 'part2_w15': 54,
 'part2_w28': 55,
 'part2_w3': 56,
 'part2_w4': 57,
 'part2_w13': 58,
 'part2_w32': 59,
 'part2_w1': 60,
 'part2_w2': 61,
 'part2_w24': 62,
 'part2_w26': 63,
 'part2_w34': 64,
 'part2_w31': 65,
 'part2_w12': 66,
 'part2_w7': 67,
 'part2_w9': 68,
 'part2_w8': 69,
 'part2_w30': 70,
 'part2_w11': 71,
 'part2_w10': 72,
 'part4_w5': 73,
 'part4_w8': 74,
 'part4_w10': 75,
 'part4_w11': 76,
 'part4_w12': 77,
 'part4_w21': 78,
 'part4_w22': 79,
 'part4_w9': 80,
 'part4_w16': 81,
 'part4_w27': 82,
 'part4_w24': 83,
 'part4_w25': 84,
 'part4_w13': 85,
 'part4_w_start': 86,
 'part4_w26': 87,
 'part4_w19': 88,
 'part4_w_end': 89,
 'part4_w20': 90,
 'part4_w4': 91,
 'part4_w3': 92,
 'part4_w6': 93,
 'part4_w14': 94,
 'pat4_w1': 95,
 'part4_w23': 96,
 'part4_w2': 97,
 'part3_w1': 98,
 'part3_w23': 99,
 'part4_w28': 100,
 'part3_w12': 101,
 'part3_w24': 102,
 'part3_w25': 103,
 'part3_w19': 104,
 'part3_w20': 105,
 'part3_w11': 106,
 'part3_w13': 107,
 'part3_w26': 108,
 'part3_w6': 109,
 'part3_w5': 110,
 'part3_w4': 111,
 'part3_w3': 112,
 'part3_w9': 113,
 'part3_w8': 114,
 'part3_w15': 115,
 'part3_w16': 116,
 'part3_w10': 117,
 'part3_w28': 118,
 'part3_w27': 119,
 'part3_w7': 120,
 'outside_weld' : 121}

convert_voc_to_yolo(voc_path, yolo_path, class_mapping)