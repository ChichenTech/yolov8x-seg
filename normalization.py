import os
from PIL import Image

img_path = "../datasts/straw/test"
folder_path = "../datasets/straw/labels/train"
label_path = "../datasets/stra/label/train"

def replace_file_path(file_path):
    # 将文件路径分割为目录路径和文件名/扩展名
    dir_path, file_name = os.path.split(file_path)

    # 提取文件名（不带扩展名）和扩展名
    base_name, ext = os.path.splitext(file_name)

    # 将目录路径中的 'labels' 替换为 'images'
    new_dir_path = os.path.join(dir_path.replace('labels', 'images'))

    # 生成新的文件路径
    new_file_path = os.path.join(new_dir_path, f'{base_name}.jpg')

    return new_file_path

def replace_label_path(file_path):
    # 将文件路径分割为目录路径和文件名/扩展名
    dir_path, file_name = os.path.split(file_path)

    # 提取文件名（不带扩展名）和扩展名
    base_name, ext = os.path.splitext(file_name)

    # 将目录路径中的 'labels' 替换为 'images'
    new_dir_path = os.path.join(dir_path.replace('labels', 'label'))

    # 生成新的文件路径
    new_label_path = os.path.join(new_dir_path, f'{base_name}.txt')

    return new_label_path

for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        img_path = replace_file_path(file_path)
        image = Image.open(img_path)
        w,h = image.size
        with open(file_path, 'r') as file:
            line = file.readline()
            while line:
                numbers = [float(num) for num in line.split() if num.replace('.', '', 1).isdigit()]
                for i in range(1,len(numbers)):
                    if i % 2 == 1:
                        numbers[i] /= w
                    else:
                        numbers[i] /= h
                numbers[0] -= 1
                text = ' '.join(map(str,numbers)) + '\n'
                print(text)
                new_label_path = replace_label_path(file_path)
                with open(new_label_path,'a') as new_file:
                    new_file.write(text)
                line = file.readline()
