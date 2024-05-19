#align(center, text(17pt)[
  *Machine Vision Homework\#5*
])

#align(center, text(12pt)[
  * 110590017 陳姿安 *
])

= Original Image
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./images/img1.jpg",width: 100%),
  image("./images/img2.jpg",width: 100%),
  image("./images/img3.jpg",width: 100%),
)

= 1. Implement Mean Filter with 3*3 and 7*7 mask.
- 指定kernel_size的大小，將範圍內的值全部加總起來，再除以kenel的大小，得到的值就是新的pixel值
- 3x3(kernel_size=3)
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./result/img1_q1_3.png",width: 100%),
  image("./result/img2_q1_3.png",width: 100%),
  image("./result/img3_q1_3.png",width: 100%),
)
- 7x7(kernel_size=7)
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./result/img1_q1_7.png",width: 100%),
  image("./result/img2_q1_7.png",width: 100%),
  image("./result/img3_q1_7.png",width: 100%),
)

#pagebreak()

= 2. Implement Median Filter with 3*3 and 7*7 mask.
- 指定kernel_size的大小，將範圍內的值排序，index在正中間的數值作為新的pixel值
- 3x3
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./result/img1_q2_3.png",width: 100%),
  image("./result/img2_q2_3.png",width: 100%),
  image("./result/img3_q2_3.png",width: 100%),
)
- 7x7
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./result/img1_q2_7.png",width: 100%),
  image("./result/img2_q2_7.png",width: 100%),
  image("./result/img3_q2_7.png",width: 100%),
)
#pagebreak()
= 3. Implement Gaussian 2D Filter with 5*5 mask.
$sigma = 1, $, kernel size = 5x5
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./result/img1_q3.png",width: 100%),
  image("./result/img2_q3.png",width: 100%),
  image("./result/img3_q3.png",width: 100%),
)

#pagebreak()
= DLC
Merge Gaussian and Median Filter
- 3x3
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./result/img1_q4_3.png",width: 100%),
  image("./result/img2_q4_3.png",width: 100%),
  image("./result/img3_q4_3.png",width: 100%),
)
- 5x5
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./result/img1_q4_5.png",width: 100%),
  image("./result/img2_q4_5.png",width: 100%),
  image("./result/img3_q4_5.png",width: 100%),
)
- 7x7
#grid(
  columns: (2fr,2fr,2fr),
  gutter: 16pt,
  align: (center),
  image("./result/img1_q4_7.png",width: 100%),
  image("./result/img2_q4_7.png",width: 100%),
  image("./result/img3_q4_7.png",width: 100%),
)

