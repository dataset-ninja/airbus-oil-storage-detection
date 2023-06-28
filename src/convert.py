# https://www.kaggle.com/datasets/teddevrieslentsch/morado-5may

import ast
import csv
import os
import xml.etree.ElementTree as ET

import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "Airbus Aircraft Detection"
dataset_path = "./APP_DATA"
batch_size = 30
ds_names = ["images", "extras"]

# images_folder = "images"
annotations_folder = "annotations"
ann_ext = ".txt"


def create_ann(image_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_width = image_np.shape[1]

    file_name = get_file_name(image_path)

    ann_path = os.path.join(anns_path, file_name + ann_ext)

    if file_exists(ann_path):
        with open(ann_path) as f:
            content = f.read().split("\n")

            for curr_data in content:
                if len(curr_data) != 0:
                    line = curr_data.split("|")

                    obj_class = name2objclass[line.pop(0)]

                    # curr_data = ast.literal_eval(line[0])

                    # curr_data = list(map(float, line))

                    x1, y1, x2, y2 = ast.literal_eval(line[0])

                    left = min(x1, x2)
                    right = max(x1, x2)
                    top = min(y1, y2)
                    bottom = max(y1, y2)

                    rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                    label = sly.Label(rectangle, obj_class)
                    labels.append(label)

    return sly.Annotation(img_size=(img_height, img_width), labels=labels)


obj_classes = [
    sly.ObjClass("oil-storage-tank", sly.Rectangle),
    # sly.ObjClass("Truncated_airplane", sly.Polygon),
]


name2objclass = {
    "oil-storage-tank": sly.ObjClass("oil-storage-tank", sly.Rectangle),
    # "Truncated_airplane": sly.ObjClass("Truncated_airplane", sly.Polygon),
}


# images_path = os.path.join(dataset_path, images_folder)
anns_path = os.path.join(dataset_path, annotations_folder)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_classes)
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in ds_names:
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        images_path = os.path.join(dataset_path, ds_name)
        images_names = os.listdir(images_path)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for images_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [
                os.path.join(images_path, image_name) for image_name in images_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)

            if ds_name == "images":
                img_ids = [im_info.id for im_info in img_infos]

                anns = [create_ann(image_path) for image_path in img_pathes_batch]
                api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))

    return project
