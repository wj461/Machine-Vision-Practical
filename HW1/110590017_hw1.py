import cv2
import numpy as np
from collections import Counter
import math

img_paths = ["./images/img1.png", "./images/img2.png", "./images/img3.png"]
test_img = "./images/block.png"

def index_color(img_path):
    img = cv2.imread(img_path)
    colors = []
    index_color = []
    deviation = 36
    for i in range(len(img)):
        for j in range(len(img[0])):
            b, g, r = img[i, j]
            colors.append((b, g, r))
    count_dict = Counter(colors)
    sorted_count = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    r_channel = []
    g_channel = []
    b_channel = []

    while len(r_channel)+len(g_channel)+len(b_channel) < 16:
        r_channel = []
        g_channel = []
        b_channel = []
        for key, value in sorted_count:
            b, g, r = key
            if max(key) == r:
                if len(r_channel) != 0:
                    close_color = find_close(key, r_channel)
                    b_c, g_c, r_c = close_color
                    if (abs(int(r_c) - int(r)) > deviation) or (abs(int(g_c) - int(g)) > deviation) or (abs(int(b_c) - int(b)) > deviation):
                        r_channel.append(key)
                else:
                    r_channel.append(key)
            elif max(key) == g:
                if len(g_channel) != 0:
                    close_color = find_close(key, g_channel)
                    b_c, g_c, r_c = close_color
                    if (abs(int(r_c) - int(r)) > deviation) or (abs(int(g_c) - int(g)) > deviation) or (abs(int(b_c) - int(b)) > deviation):
                        g_channel.append(key)
                else:
                    g_channel.append(key)
            else:
                if len(b_channel) != 0:
                    close_color = find_close(key, b_channel)
                    b_c, g_c, r_c = close_color
                    if (abs(int(r_c) - int(r)) > deviation) or (abs(int(g_c) - int(g)) > deviation) or (abs(int(b_c) - int(b)) > deviation):
                        b_channel.append(key)
                else:
                    b_channel.append(key)
        deviation -= 1
    
    for i in range(16):
        try:
            index_color.append(r_channel[i])
        except:
            pass
        try:
            index_color.append(g_channel[i])
        except:
            pass
        try:
            index_color.append(b_channel[i])
        except:
            pass
    
    index_color = index_color[:16]
    print(index_color)
    return index_color

def draw_by_color(img_path, color, filename):
    img = cv2.imread(img_path)
    for i in range(len(img)):
        for j in range(len(img[0])):
            img[i][j] = find_close(img[i][j], color)

    cv2.imwrite(filename, img)

def find_close(color, index_color):
    counter_list = []
    b, g, r = color
    for i in index_color:
        i_b, i_g, i_r = i
        counter_list.append(math.sqrt( pow(int(i_r) - int(r),2) + pow(int(i_g) - int(g),2) + pow(int(i_b) - int(b),2)))
    
    return index_color[counter_list.index(min(counter_list))]


def grayscale(img_path, filename):
    img = cv2.imread(img_path)
    print("run geayscale q1-1", filename)
    for i in range(len(img)):
        for j in range(len(img[0])):
            b, g, r = img[i][j]
            img[i][j] = (0.3 * r) + (0.59 * g) + (0.11 * b)
    cv2.imwrite(filename, img)

def binary(img_path, filename):
    img = cv2.imread(img_path)
    print("run binary q1-2", filename)
    for i in range(len(img)):
        for j in range(len(img[0])):
            b, g, r = img[i][j]
            brightness = (int(r) + int(g) + int(b))/ 3.0
            if brightness > 127:
                img[i][j] = 255
            else:
                img[i][j] = 0

    cv2.imwrite(filename, img)

def resize_double_interpolation(img_path, filename):
    img = cv2.imread(img_path)
    new_img = np.zeros((img.shape[0]*2, img.shape[1]*2, 3), dtype=np.uint8)
    print("run resize_interpolation q2-1", filename)

    for i in range(len(img)):
        for j in range(len(img[0])):
            new_img[i*2][j*2] = img[i][j]
            new_img[i*2][j*2+1] = img[i][j]
            new_img[i*2+1][j*2] = img[i][j]
            new_img[i*2+1][j*2+1] = img[i][j]

    cv2.imwrite(filename, new_img)

def resize_half_interpolation(img_path, filename):
    img = cv2.imread(img_path)
    new_img = np.zeros((img.shape[0]//2, img.shape[1]//2, 3), dtype=np.uint8)
    print("run resize_interpolation q2-1", filename)

    for i in range(len(new_img)):
        for j in range(len(new_img[0])):
            new_img[i][j] = img[i*2][j*2]

    cv2.imwrite(filename, new_img)

def resize_bilinear(img_path, filename, times):
    print("run resize_interpolation q2-2", filename)
    img = cv2.imread(img_path)
    new_img = np.zeros((int(float(img.shape[0])*times), int(float(img.shape[1])*times), 3), dtype=np.uint8)

    new_height, new_width, _ = new_img.shape
    height, width, _ = img.shape

    for y in range(new_height):
        for x in range(new_width):
            x_original = (x + 0.5) * (width / new_width) - 0.5
            y_original = (y + 0.5) * (height / new_height) - 0.5

            x0 = int(np.floor(x_original))
            y0 = int(np.floor(y_original))
            x1 = min(x0 + 1, width - 1)
            y1 = min(y0 + 1, height - 1)


            dx = x_original - x0
            dy = y_original - y0
            interpolated_pixel = (1 - dx) * (1 - dy) * img[y0, x0] + \
                                  dx * (1 - dy) * img[y0, x1] + \
                                  (1 - dx) * dy * img[y1, x0] + \
                                  dx * dy * img[y1, x1]

            new_img[y, x] = interpolated_pixel

    cv2.imwrite(filename, new_img)



def q1_1():
    for i, img_path in enumerate(img_paths):
        grayscale(img_path, f"./results/img{i+1}_q1-1.jpg")

def q1_2():
    for i, img_path in enumerate(img_paths):
        binary(img_path, f"./results/img{i+1}_q1-2.jpg")

def q1_3():
    for i, img_path in enumerate(img_paths):
        indexed_color = index_color(img_path)
        draw_by_color(img_path, indexed_color, f"./results/img{i+1}_q1-3.jpg")

def q2_1():
    for i, img_path in enumerate(img_paths):
        resize_double_interpolation(img_path, f"./results/img{i+1}_q2-1-double.jpg")
        resize_half_interpolation(img_path, f"./results/img{i+1}_q2-1-half.jpg")

def q2_2():
    for i, img_path in enumerate(img_paths):
        resize_bilinear(img_path, f"./results/img{i+1}_q2-2-double.jpg",2)
        resize_bilinear(img_path, f"./results/img{i+1}_q2-2-half.jpg", 0.5)

q1_3()



