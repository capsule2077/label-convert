# label-convert
数据标注的格式转换，比如yolo转coco、voc转coco...
---
# 1.YOLO2COCO
yolo格式的数据应该如下：

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


