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
labels文件夹下的txt文件格式如下：
```
class_id x_center y_center width height
```
其中class_id是类别id，从0开始；x_center和y_center是目标中心点相对于图片宽高的比例；width和height是目标的宽高相对于图片宽高的比例。