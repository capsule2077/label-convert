import json
import shutil
from pathlib import Path
import cv2
from tqdm import tqdm


# 如果使用jupyter notebook则以下方式导入tqdm
# from tqdm.notebook import tqdm


def get_datasets_path(root_dir):
    dir_list = []
    for t in type_list:
        sublayer = root_dir.joinpath(
            "images", t), root_dir.joinpath("labels", t)
        if sublayer[0].exists():
            dir_list.append(sublayer)
            assert sublayer[1].exists(), f"the path '{sublayer[1]}' is not exists"
    if len(dir_list) == 0:
        raise FileNotFoundError("the path is empty,please check you path")
    with root_dir.joinpath("classes.txt").open() as f:
        classes = f.read().strip().split()

    return dir_list, classes


def move_images(origin_images_dir, filename, path):
    dst = root_dir.joinpath("yolo2coco", f"{path[0].name}2017")
    if not dst.exists():
        dst.mkdir(parents=True)
    dst.joinpath(filename)
    shutil.move(origin_images_dir, dst)


# 参考 https://github.com/Weifeng-Chen/dl_scripts/blob/main/detection/yolo2coco.py
def yolo2coco(dir_list, classes):
    for path in dir_list:
        dataset = {"categories": [], "annotations": [], "images": []}
        for i, cls in enumerate(classes, 0):
            dataset["categories"].append(
                {"id": i, "name": cls, "supercategory": "mark"})

        indexes = list(path[0].iterdir())
        id_count = 0
        bar = tqdm(indexes, unit=" images ")
        for k, index in enumerate(bar):
            info = f" {k + 1} / {len(indexes)}"
            bar.desc = info

            filename = index.name
            label_filename = Path(index.name).with_suffix(".txt")
            origin_labels_dir = path[1].joinpath(label_filename)
            origin_images_dir = path[0].joinpath(index)

            img = cv2.imread(origin_images_dir.as_posix())
            image_height, image_width, _ = img.shape

            dataset["images"].append({"file_name": filename,
                                      "id": k,
                                      "width": image_width,
                                      "height": image_height})
            # 移动图片到coco文件夹
            move_images(origin_images_dir, filename, path)

            if not origin_labels_dir.exists():
                print(f"{origin_images_dir} has not label")
                continue
            with origin_labels_dir.open("r") as f:
                labels = f.readlines()
                for label in labels:
                    label = label.strip().split()
                    x = float(label[1])
                    y = float(label[2])
                    w = float(label[3])
                    h = float(label[4])

                    # convert x,y,w,h to x1,y1,x2,y2
                    # 左上角和宽高
                    x1 = (x - w / 2) * image_width
                    y1 = (y - h / 2) * image_height
                    x2 = (x + w / 2) * image_width
                    y2 = (y + h / 2) * image_height

                    cls_id = int(label[0])
                    width = max(0, x2 - x1)
                    height = max(0, y2 - y1)
                    dataset["annotations"].append({
                        "area": width * height,
                        "bbox": [x1, y1, width, height],
                        "category_id": cls_id,
                        "id": id_count,
                        "image_id": k,
                        "iscrowd": 0,
                        "segmentation": [[x1, y1, x2, y1, x2, y2, x1, y2]]})
                    id_count += 1

        annotations = root_dir.joinpath("yolo2coco", "annotations")
        if not annotations.exists():
            annotations.mkdir()
        save_file = annotations.joinpath(f"instances_{path[0].name}2017.json")
        with save_file.open("w") as f:
            json.dump(dataset, f)
        print("Save annotation to {} successfully!".format(save_file))
        print("Move images of {}_dataset successfully!".format(path[0].name))


if __name__ == "__main__":
    # yolo格式数据根目录
    root_dir = Path("G:\yolo_dataset")
    # 自动区分是否有训练/验证/测试集
    # 所以一般无需更改type_list
    type_list = ["train", "val", "test"]
    dir_list, classes = get_datasets_path(root_dir)
    yolo2coco(dir_list, classes)
