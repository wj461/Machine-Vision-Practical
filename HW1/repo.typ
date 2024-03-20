#align(center, text(17pt)[
  *Machine Vision Homework\#1*
])

#align(center, text(12pt)[
  *
  110590017 陳姿安
  *
])


= 1.Image Quantization(binary, gray, index-color)

*1-1. Convert the color image to the grayscale image*
  - Formula: (0.3 x R) + (0.59 x G) + (0.11 x B).
  + let R, G, B be the same value of each channel by formula.
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./results/img1_q1-1.jpg",width: 100%),
  image("./results/img2_q1-1.jpg",width: 100%),
  image("./results/img3_q1-1.jpg",width: 100%),
)

*1-2. Convert the grayscale image to the binary image*
  - Choose a appropriate threshold by yourself.
  - if brightness > 127 then 255 else 0
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./results/img1_q1-2.jpg",width: 100%),
  image("./results/img2_q1-2.jpg",width: 100%),
  image("./results/img3_q1-2.jpg",width: 100%),
)

#pagebreak()

*1-3 Convert the color image to the index-color image*
  - Define your own colormap of 16 type colors.
  - def index_color(img_path) return index_color
    + 先擷取所有出現過得顏色對出現次數進行排序
    + 使用排序後的list針對rgb進行分類
      + r,g,b三群進行分類
      + 透過查看該顏色rgb的最大值進行分類
      + 使用deviation變數將較為相近的顏色去除
      + 若是總數低於16色則降低deviation再進行一次分類
    + 分類後依序在各群取出顏色
    + 取出後回傳最終結果
  - def deaw_by_color(img_path, color, filename)
    + 使用find_colose(color, index_color)選擇原始圖片中最接近index_color的顏色
      + 計算當前顏色與index_color內所有顏色的距離
      + 回傳距離最近的顏色
    + 將原始圖片中的顏色替換成find_colose回傳的結果

#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  image("./img1_index.jpg",width: 100%),
  image("./img2_index.jpg",width: 100%),
  image("./img3_index.jpg",width: 100%),
)
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./results/img1_q1-3.jpg",width: 100%),
  image("./results/img2_q1-3.jpg",width: 100%),
  image("./results/img3_q1-3.jpg",width: 100%),
  )

(b, g, r)\
img1 = [(86, 175, 219), (0, 76, 0), (97, 48, 2), (150, 220, 249), (16, 78, 62), (161, 118, 66), (0, 5, 44), (0, 140, 32), (142, 84, 24), (198, 228, 239), (0, 12, 4), (57, 27, 26), (20, 44, 80), (114, 133, 131), (85, 71, 41), (1, 41, 228)],

img2 = [(195, 210, 226), (48, 79, 78), (53, 83, 100), (22, 30, 29), (120, 134, 153), (88, 114, 113), (90, 104, 123), (131, 162, 193), (166, 180, 199), (5, 32, 52), (85, 125, 154), (0, 3, 14), (43, 51, 68), (171, 184, 234), (113, 125, 188), (77, 90, 169)],

img3 = [(152, 176, 232), (111, 173, 63), (202, 195, 101), (106, 198, 242), (250, 250, 248), (69, 29, 28), (73, 48, 210), (62, 158, 115), (239, 208, 163), (250, 250, 250), (189, 201, 146), (249, 248, 248), (10, 10, 10), (122, 250, 240), (184, 114, 78), (70, 118, 222)]

#pagebreak()

= 2.Resizing Image

*2-1. Resizing image to 1 2 and 2 times without interpolation*
    + 根據ppt給的圖示進行縮放
#grid(
  columns: (auto, auto, auto), 
  gutter: 16pt,
  align: (center + horizon, center + horizon, center + horizon),
  image("./results/img1_q2-1-half.jpg",width: 25%),
  image("./images/img1.png",width: 50%),
  image("./results/img1_q2-1-double.jpg",width: 100%),
  image("./results/img2_q2-1-half.jpg",width: 25%),
  image("./images/img2.png",width: 50%),
  image("./results/img2_q2-1-double.jpg",width: 100%),
  image("./results/img3_q2-1-half.jpg",width: 25%),
  image("./images/img3.png",width: 50%),
  image("./results/img3_q2-1-double.jpg",width: 100%),
)

#pagebreak()

*Resizing image to 1 2 and 2 times with interpolation*
  - You can use bilinear or bicubic interpolation
    + 透過新舊圖片比例計算x_origin, y_origin獲得新圖片在原始圖片中的位置
    + 使用x0,y0,x1,y1定位原始圖片出周圍四點
    + 化簡ppt的公式進行計算
    + 將算出的顏色給當前新圖片
#grid(
  columns: (auto, auto, auto), 
  gutter: 16pt,
  align: (center + horizon, center + horizon, center + horizon),
  image("./results/img1_q2-2-half.jpg",width: 25%),
  image("./images/img1.png",width: 50%),
  image("./results/img1_q2-2-double.jpg",width: 100%),
  image("./results/img2_q2-2-half.jpg",width: 25%),
  image("./images/img2.png",width: 50%),
  image("./results/img2_q2-2-double.jpg",width: 100%),
  image("./results/img3_q2-2-half.jpg",width: 25%),
  image("./images/img3.png",width: 50%),
  image("./results/img3_q2-2-double.jpg",width: 100%),
)