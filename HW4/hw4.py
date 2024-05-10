import cv2
import numpy as np
import heapq

img_paths = ["./images/img1.png", "./images/img2.png", "./images/img3.png"]
# img_paths = ["./images/test.png"]
# BGR

label_color = [[
    [0, 0, 255], 
    [0, 255, 0],
    [255, 0, 0],
    [255, 255, 255]],
    [
    [0, 0, 255], 
    [0, 255, 0],
    [255, 0, 0],
    [210, 210, 255],
    [190, 255, 255],
    [255, 255, 0],
    [255, 0, 166],
    [20, 155, 245],
    [255, 0, 255],
    [130, 105, 250],
    [0, 255, 255],
    [220, 255, 235],
    [157, 255, 0],
    [128, 128, 128],
    ],
    [[0, 0, 255], 
    [0, 255, 0],
    [255, 0, 0]]
]

neighbors = []

heapq.heapify(neighbors)

raw_img_g = [
    cv2.imread("./images/img1.png"),
    cv2.imread("./images/img2.png"),
    cv2.imread("./images/img3.png")
]


def legal(x,y,w,h):
    return x >= 0 and x < h and y >= 0 and y < w

def label_img(label_color, img_path, raw_img):
    img = cv2.imread(img_path)
    label_map = np.zeros((len(img), len(img[0])))
    hight, width = len(label_map), len(label_map[0])

    for i in range(hight):
        for j in range(width):
            if img[i][j].tolist() in label_color:
                label_map[i][j] = label_color.index(img[i][j].tolist()) + 1

    edge_label_map = np.copy(label_map)
    for i in range(hight):
        for j in range(width):
            if label_map[i][j] == 0:
                local_neighbors = []

                for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if legal(i+y, j+x, width, hight) and label_map[i+y][j+x] != 0 :
                        local_neighbors.append(label_map[i+y][j+x])

                local_neighbors = set(local_neighbors)
                if len(local_neighbors) > 0:
                    edge_label_map[i][j] = -2
                    heapq.heappush(neighbors, (cal_priority(label_map, i, j, raw_img), (i, j)))

    return edge_label_map

def cal_priority(label_map, i, j, raw_img):
    r = 4
    p = 10
    # p = 700
    dis = 0
    t = 0
    local_neighbors = []
    current = raw_img[i][j]
    # for y in range(-r//2, r//2+1):
    #     for x in range(-r//2, r//2+1):
    for y in range(r):
        for x in range(r):
            if legal(i+y, j+x, len(label_map[0]), len(label_map)):
                local_neighbors.append(raw_img[i+y][j+x])
                # dis += np.sqrt(((raw_img[i,j] - raw_img[i+y,j+x]) **2).sum())
                # print(np.sqrt(((raw_img[i,j] - raw_img[i+y,j+x]) **2).sum()), np.sqrt((int(raw_img[i][j][0])-int(raw_img[i+y,j+x][0])) ** 2 + (int(raw_img[i][j][1])-int(raw_img[i+y,j+x][1])) ** 2 + (int(raw_img[i][j][2])-int(raw_img[i+y,j+x][2])) ** 2))
    # return dis
    # print(local_neighbor
    # t = np.sum(np.var(local_neighbors, axis=0))
    for n in local_neighbors:
        t += np.sqrt((int(raw_img[i][j][0])-int(n[0])) ** 2 + (int(raw_img[i][j][1])-int(n[1])) ** 2 + (int(raw_img[i][j][2])-int(n[2])) ** 2)
        
        temp = n.tolist()
        current_max =  int(max(current.tolist()))
        temp_max = int(max(temp))
        if temp.index(temp_max) == current.tolist().index(current_max)\
            and abs(temp_max - current_max) < 50:
            t -= p
        
        # if np.sum(n) < 100:
        #     t += p

        # if np.sum(n) > (255 -15):
        #     t += p
    # print(dis, t)
    return t

    # temp = []
    # for i in range(len(local_neighbors)):
    #     temp.append(np.sum(local_neighbors[i]))
    
    # min_n = local_neighbors[temp.index(min(temp))].astype('float32')
    # max_n = local_neighbors[temp.index(max(temp))].astype('float32')

    # return (max_n[0] - min_n[0])**2 + (max_n[1] - min_n[1])**2 + (max_n[2] - min_n[2])**2

def push_neighbors(label_map, raw_img, color, img_path):
    hight, width = len(label_map), len(label_map[0])

    count = 0
    while(True):
        try:
            _, (i,j) = heapq.heappop(neighbors)
        except Exception as e:
            print("error", e)
            break

        local_neighbors = []

        for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
            if legal(i+y, j+x, width, hight) and label_map[i+y][j+x] > 0 :
                local_neighbors.append(label_map[i+y][j+x])

        local_neighbors = set(local_neighbors)
        if len(local_neighbors) == 1:# push new edge pixel to queue when -2 mark to label
            label_map[i][j] = max(local_neighbors)
            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                if legal(i+y, j+x, width, hight) and label_map[i+y][j+x] == 0 :
                    label_map[i+y][j+x] = -2
                    heapq.heappush(neighbors, (cal_priority(label_map, i+y, j+x, raw_img), (i+y, j+x)))

        if len(local_neighbors) > 1: # mark edge pixel
            label_map[i][j] = -1

        # if count % 500 == 0:
        #     draw_img(img_path,label_map, f"./test/img{count}", color)
        # count += 1

    return label_map


def draw_img(img_path,label_map, filename, color_map):
    img = cv2.imread(img_path)
    hight, width = len(label_map), len(label_map[0])
    new_img = np.zeros((hight, width, 3))

    for i in range(hight):
        for j in range(width):
            if label_map[i][j] >0:
                new_img[i][j] = color_map[int(label_map[i][j])-1]
            else:
                new_img[i][j] = 0


    img = img.astype('float32')
    new_img = new_img.astype('float32')

    output = cv2.addWeighted(img, 0.5, new_img, 0.3, 50)
    cv2.imwrite(filename + ".png", output) 
    # cv2.imwrite(filename + ".png", new_img) 

def q1():
    for i, img_path in enumerate(img_paths):
        print(f"run init label {img_path}")
        label_map = label_img(label_color[i], img_path, raw_img_g[i])
        print(f"run push {img_path}")
        label_map = push_neighbors(label_map, raw_img_g[i],label_color[i], img_path)
        print(f"run draw {img_path}")
        draw_img(img_path,label_map, f"./result/img{i+1}", label_color[i])
        print(f"done {img_path}")

q1()