import cv2
import numpy as np
import random

img_paths = ["./images/img1.png", "./images/img2.png", "./images/img3.png", "./images/img4.png"]
# img_paths = ["./images/test.png"]

def binary(img_path, filename):
    img = cv2.imread(img_path)
    print("run binary q1-2", filename)
    for i in range(len(img)):
        for j in range(len(img[0])):
            b, g, r = img[i][j]
            brightness = (0.3 * r) + (0.59 * g) + (0.11 * b)
            # img[i][j] = brightness
            if brightness > 235:
                img[i][j] = 255
            else:
                img[i][j] = 0

    cv2.imwrite(filename + ".png", img)
    return img

def four_connected(img_path, source_img):
    label_map = np.zeros((len(source_img), len(source_img[0])))
    label = 0

    color_map = {}
    hight, width = source_img.shape[:2]

    print("run four_connected ")
    for i in range(hight):
        for j in range(width):
            if source_img[i][j][0] != 255:
                if label_map[i][j-1] == 0 and label_map[i-1][j] == 0:
                    label += 1
                    label_map[i,j] = label
                    color_map[label] = label
                elif label_map[i][j-1] != 0 and label_map[i-1][j] == 0:
                    label_map[i,j] = label_map[i][j-1]
                elif label_map[i][j-1] == 0 and label_map[i-1][j] != 0:
                    label_map[i,j] = label_map[i-1][j]
                else:
                    current_label = min(label_map[i][j-1], label_map[i-1][j])
                    label_map[i,j] = current_label
                    color_map[find_by_map(
                        color_map, max(label_map[i][j-1], label_map[i-1][j])
                        )] = find_by_map(color_map, current_label)

    return label_map, color_map, label

def draw_label_map(label_map, color_map, source_img, label_counter, filename):
    print("run draw_label_map, filename: ", filename)
    color = [ (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range(0, label_counter+1) ]

    for i in range(len(source_img)):
        for j in range(len(source_img[0])):
            if source_img[i][j][0] != 255:
                current_color = find_by_map(color_map, label_map[i][j])
                source_img[i][j] = color[int(current_color)]

    cv2.imwrite(filename + ".png", source_img) 

def find_by_map(color_map, label):
    if color_map[label] != label:
        color_map[label] = find_by_map(color_map, color_map[label])
        return color_map[label]

    return color_map[label]

def n_4():
    for i, img_path in enumerate(img_paths):
        img = binary(img_path,f"g_{i}")
        label_map, color_map, label_counter = four_connected(img_path, img)
        draw_label_map(label_map, color_map, img, label_counter, f"./results/img{i+1}_q1-4.jpg")

n_4()