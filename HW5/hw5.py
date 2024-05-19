import cv2
import numpy as np

img_paths = ["./images/img1.jpg", "./images/img2.jpg", "./images/img3.jpg"]

def legal(x,y,w,h):
    return x >= 0 and x < h and y >= 0 and y < w

def mean_filter(img_path, kernel_size, filename):
    print(f"Do {img_path} mean filter with kernel size {kernel_size}")

    img = cv2.imread(img_path)
    height, width = len(img), len(img[0])

    # kernel = np.ones((kernel_size, kernel_size)) * (1/9)
    new_img = np.zeros((height, width, 3))
    for i in range(height):
        for j in range(width):
            local = np.zeros((kernel_size, kernel_size, 1))
            for x in range(-(kernel_size//2), (kernel_size//2)+1):
                for y in range(-(kernel_size//2), (kernel_size//2)+1):
                    if legal(i+x, j+y, width, height):
                        local[x+(kernel_size//2)][y+(kernel_size//2)] = img[i+x][j+y][0]
                
            new_img[i][j] = np.sum(local) * 1/(kernel_size**2)

    cv2.imwrite(filename + ".png", new_img) 

def median_filter(img_path, kernel_size, filename):
    print(f"Do {img_path} median filter with kernel size {kernel_size}")

    img = cv2.imread(img_path)
    height, width = len(img), len(img[0])

    # kernel = np.ones((kernel_size, kernel_size)) * (1/9)
    new_img = np.zeros((height, width, 3))
    for i in range(height):
        for j in range(width):
            local = np.zeros((kernel_size, kernel_size, 1))
            for x in range(-(kernel_size//2), (kernel_size//2)+1):
                for y in range(-(kernel_size//2), (kernel_size//2)+1):
                    if legal(i+x, j+y, width, height):
                        local[x+(kernel_size//2)][y+(kernel_size//2)] = img[i+x][j+y][0]
                
            local = np.sort(local).flatten()
            new_img[i][j] = local[(kernel_size*kernel_size)//2]

    cv2.imwrite(filename + ".png", new_img) 

def gaussian_filter(img_path, kernel_size, filename):
    print(f"Do {img_path} gaussian filter with kernel size {kernel_size}")

    img = cv2.imread(img_path)
    height, width = len(img), len(img[0])

    kernel = gaussian(kernel_size)
    kernel = kernel / np.sum(kernel)

    new_img = np.zeros((height, width, 3))
    for i in range(height):
        for j in range(width):
            local = np.zeros((kernel_size, kernel_size))
            for x in range(-(kernel_size//2), (kernel_size//2)+1):
                for y in range(-(kernel_size//2), (kernel_size//2)+1):
                    if legal(i+x, j+y, width, height):
                        local[x+(kernel_size//2)][y+(kernel_size//2)] = img[i+x][j+y][0]

            new_img[i][j] = np.sum(local * kernel)

    cv2.imwrite(filename + ".png", new_img)

def gaussian(kernel_size):
    sigma = 1
    kernel = np.zeros((kernel_size, kernel_size))
    for i in range(-(kernel_size//2), (kernel_size//2)+1):
        for j in range(-(kernel_size//2), (kernel_size//2)+1):
            kernel[i+(kernel_size//2)][j+kernel_size//2] = 1/(2 * np.pi * sigma**2) * np.exp(-(i**2 + j**2)/(2*sigma**2))

    return kernel

def gaussian_med_filter(img_path, kernel_size, filename):
    print(f"Do {img_path} gaussian and mid filter with kernel size {kernel_size}")

    img = cv2.imread(img_path)
    height, width = len(img), len(img[0])

    kernel = gaussian(kernel_size)
    kernel = kernel / np.sum(kernel)

    new_img = np.zeros((height, width, 3))
    for i in range(height):
        for j in range(width):
            local = np.zeros((kernel_size, kernel_size))
            for x in range(-(kernel_size//2), (kernel_size//2)+1):
                for y in range(-(kernel_size//2), (kernel_size//2)+1):
                    if legal(i+x, j+y, width, height):
                        local[x+(kernel_size//2)][y+(kernel_size//2)] = img[i+x][j+y][0]

            # print(local)
            local = np.sort(local)
            # print(local)
            new_img[i][j] = np.sum(local * kernel)

    cv2.imwrite(filename + ".png", new_img)


def q1():
    for i, img_path in enumerate(img_paths):
        # mean_filter(img_path, 3, f'./result/img{i+1}_q1_3')
        # mean_filter(img_path, 7, f'./result/img{i+1}_q1_7')
        # median_filter(img_path, 3, f'./result/img{i+1}_q2_3')
        # median_filter(img_path, 7, f'./result/img{i+1}_q2_7')
        # gaussian_filter(img_path, 5, f'./result/img{i+1}_q3')
        gaussian_med_filter(img_path, 7, f'./result/img{i+1}_q4_7')
        gaussian_med_filter(img_path, 3, f'./result/img{i+1}_q4_3')
        


q1()

