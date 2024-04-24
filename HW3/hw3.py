import cv2
import numpy as np
from copy import deepcopy

img_paths = ["./images/img1.jpg", "./images/img2.jpg", "./images/img3.jpg", "./images/img4.jpg"]

def binary(img_path, filename):
    img = cv2.imread(img_path)
    print("run binary ", filename)
    distance_map = np.zeros((len(img), len(img[0])))
    for i in range(len(img)):
        for j in range(len(img[0])):
            b, g, r = img[i][j]
            brightness = (0.3 * r) + (0.59 * g) + (0.11 * b)
            # img[i][j] = brightness
            if brightness > 235:
                img[i][j] = 0
            else:
                img[i][j] = 255
                distance_map[i][j] = 1

    cv2.imwrite(filename + ".png", img)
    return img, distance_map

def distance_transform(source_img, distance_map, filename, connect):
    print(f"run {connect} distance_transform, {filename} ")
    max_distance = 0
    while True:
        last_distance_map = deepcopy(distance_map)
        for i in range(len(source_img)):
            for j in range(len(source_img[0])):
                neighbors = add_neighbors_four(distance_map, len(source_img), len(source_img[0]), i, j)

                if distance_map[i][j] != 0:
                    distance_map[i][j] = min(neighbors) + 1
                    if distance_map[i][j] > max_distance:
                        max_distance = distance_map[i][j]
        if np.array_equal(last_distance_map, distance_map):
            break

    draw_distance_map(distance_map, max_distance, filename)
    return distance_map

def draw_distance_map(distance_map, max_distance, filename):
    color = [(i+1) * (255//max_distance) for i in range(int(max_distance))]
    new_img = np.zeros((len(distance_map), len(distance_map[0]), 3))
    for i in range(len(distance_map)):
        for j in range(len(distance_map[0])):
            if distance_map[i][j] != 0:
                new_img[i][j] = color[int(distance_map[i][j])-1]

    cv2.imwrite(filename + ".jpg", new_img) 

def draw_skeleton(distance_map, filename):
    new_img = np.zeros((len(distance_map), len(distance_map[0]), 3))
    for i in range(len(distance_map)):
        for j in range(len(distance_map[0])):
            if distance_map[i][j] != 0:
                new_img[i][j] = 255

    cv2.imwrite(filename + ".jpg", new_img) 

def medial_axis_skeletonization(distance_map, filename):
    print("run medial_axis_skeletonization ", filename)
    rm_map = deepcopy(distance_map)
    hight, width = distance_map.shape[:2]
    for label in range(1, int(np.max(distance_map))+1):
        for i in range(hight):
            for j in range(width):
                if distance_map[i][j] != 0 and distance_map[i][j] == label:
                    neighbors = add_neighbors_eight(distance_map, hight, width, i, j)
                    check_range = np.array([
                        rm_map[i-1][j-1:j+2],
                        rm_map[i][j-1:j+2]])
                    if i < hight-1:
                        check_range = np.vstack([check_range, rm_map[i+1][j-1:j+2]])
                    else:
                        check_range = np.vstack([check_range, [0, 0, 0]])

                    # if keep eight connect after remove the px
                    # and can keep eight connect check local max
                    if (is_connectivity(deepcopy(check_range))) and distance_map[i][j] < max(neighbors):
                        rm_map[i][j] = 0
    
    for i in range(hight):
        for j in range(width):
            if rm_map[i][j] != 0:
                if (j< width-1 and rm_map[i][j] != 0 and rm_map[i][j+1] != 0)\
                or (j > 0 and rm_map[i][j-1] != 0 and rm_map[i][j] != 0):
                    check_range = np.array([
                        rm_map[i-1][j-1:j+2],
                        rm_map[i][j-1:j+2]])
                    if i < hight-1:
                        check_range = np.vstack([check_range, rm_map[i+1][j-1:j+2]])
                    else:
                        check_range = np.vstack([check_range, [0, 0, 0]])

                    if (is_connectivity(check_range)):
                        rm_map[i][j] = 0
                    
    draw_skeleton(rm_map, filename)

def is_connectivity(source_map):
    source_map[source_map > 1] = 1

    source_map[1][1] = 0
    if np.sum(source_map) < 2:
        return True

    if np.sum(source_map[0]) != 0 and np.sum(source_map[2]) != 0  and np.sum(source_map[1]) == 0:
        return False
    if np.sum(source_map[:,0]) != 0 and np.sum(source_map[:,2]) != 0  and np.sum(source_map[:,1]) == 0:
        return False

    for i in range(len(source_map)):
        for j in range(len(source_map[0])):
            neighbors_eight = add_neighbors_eight(source_map, 3, 3, i, j)
            if source_map[i][j] != 0:
                if np.sum(neighbors_eight) == 0:
                    return False
    return True

def add_neighbors_four(source_map, high, width, i, j):
    neighbors = []
    if i > 0 :
        neighbors.append(source_map[i-1][j])
    if j > 0:
        neighbors.append(source_map[i][j-1])
    if j < width-1:
        neighbors.append(source_map[i][j+1])
    if i < high-1:
        neighbors.append(source_map[i+1][j])

    return neighbors
def add_neighbors_eight(source_map, high, width, i, j):
    neighbors = []
    if i > 0 and j > 0:
        neighbors.append(source_map[i-1][j-1])
    if i > 0 :
        neighbors.append(source_map[i-1][j])
    if i > 0 and j < width-1:
        neighbors.append(source_map[i-1][j+1])
    if j > 0:
        neighbors.append(source_map[i][j-1])
    if j < width-1:
        neighbors.append(source_map[i][j+1])
    if i < high-1 and j > 0:
        neighbors.append(source_map[i+1][j-1])
    if i < high-1:
        neighbors.append(source_map[i+1][j])
    if i < high-1 and j < width-1:
        neighbors.append(source_map[i+1][j+1])

    return neighbors

def q1():
    for i, img_path in enumerate(img_paths):
        img,distance_map = binary(img_path,f"./binary/b_{i}")
        distance_transform(img,distance_map, f"./result/img{i+1}_q1-1_8",8)
        distance_map = distance_transform(img,distance_map, f"./result/img{i+1}_q1-1_4",4)
        medial_axis_skeletonization(distance_map, f"./result/img{i+1}_q1-2")

q1()