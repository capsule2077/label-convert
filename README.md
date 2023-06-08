# label-convert
数据标注的格式转换，比如yolo转coco、voc转coco...
---
# 1.YOLO2COCO

yolo格式的数据应该如下：

```
 └── $ROOT_PATH
        ├── classes.txt
        ├── images
        │    ├── train
        │    │    ├── a.jpg
        │    │    ├── b.jpg
        │    │    └── ...
        │    └── val
        │         ├── a.jpg
        │         ├── b.jpg
        │         └── ...
        ├── labels
        │    ├── train
        │    │    ├── a.txt
        │    │    ├── b.txt
        │    │    └── ...
        │    └── val
        │         ├── a.txt
        │         ├── b.txt
        │         └── ...
        └── ...

```
其中class.txt文件包含所有类别，按序一行一个类别。  
ROOT_PATH下的images和labels文件夹分别存放训练集和验证集的图片和标签，图片和标签的文件名应该一一对应。