#align(center, text(17pt)[
  *Machine Vision Homework\#2*
])

#align(center, text(12pt)[
  * 110590017 陳姿安 *
])

#grid(
  columns: (70%, 50%),
  grid(
    text(12pt)[
    = 1.Component Labeling
      - Convert the color image to a binary image.
      - Labeling components using 4-connected and 8-connected.
      - Output color image.
    ]
  ),
  image("./images/repo.png", width: 50%)
)

- origin image
#grid(
  columns: (2fr,2fr,2fr,2fr),
  gutter: 16pt,
  align: (center + horizon, center + horizon, center + horizon),
  image("./images/img1.png",width: 100%),
  image("./images/img2.png",width: 100%),
  image("./images/img3.png",width: 100%),
  image("./images/img4.png",width: 100%),
)
- binary image
#grid(
  columns: (2fr,2fr,2fr,2fr),
  gutter: 16pt,
  align: (center + horizon, center + horizon, center + horizon),
  image("./binary/g_0.png",width: 100%),
  image("./binary/g_1.png",width: 100%),
  image("./binary/g_2.png",width: 100%),
  image("./binary/g_3.png",width: 100%),
)
#pagebreak()

== 4-connect
- 4-connect
  + 使用np.zeros創出一個與原圖相同大小的map,用來儲存label
  + 創建一個dict紀錄label與label之間的關係(Disjoint set)
  + 設定黑色區塊作為物件
    + 對該pixel的左側/上方pixel進行判斷,分成4種狀況
      - 新物件: 左與上皆為空
        + 將label計數+1,填入map內
        + 在dict內紀錄該label的key與value都為label
        + 標記當前pixel為新的物件且不與其他label相鄰
      - 與左側相鄰: 左側不為空,上方為空
      - 與上方相鄰: 上方不為空,左側為空
      - 左側與上方相鄰: 當左側與上方透過該pixel相鄰
        + 則取較為小的label作為該pixel的label
        + 紀錄相鄰的label在dict內
  + 使用map將標記為相同的label填色,顏色由random產生
#grid(
  columns: (2fr,2fr,2fr,2fr),
  gutter: 16pt,
  align: (center + horizon, center + horizon, center + horizon),
  image("./results/img1_4.jpg.png",width: 100%),
  image("./results/img2_4.jpg.png",width: 100%),
  image("./results/img3_4.jpg.png",width: 100%),
  image("./results/img4_4.jpg.png",width: 100%),
)

== 8-connect
- 8-connect
  + 與4-connect類似
  + 對該pixel的左上區塊pixel進行判斷,分成3種狀況
      - 新物件: 皆為空
      - 與一個pixel相鄰
      - 與複數個pixel相鄰
        - 取最小的label
        - 將所有相鄰label的value換成最小的label

#grid(
  columns: (2fr,2fr,2fr,2fr),
  gutter: 16pt,
  align: (center + horizon, center + horizon, center + horizon),
  image("./results/img1_8.jpg.png",width: 100%),
  image("./results/img2_8.jpg.png",width: 100%),
  image("./results/img3_8.jpg.png",width: 100%),
  image("./results/img4_8.jpg.png",width: 100%),
)
