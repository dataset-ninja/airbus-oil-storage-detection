import csv
import os

anns_folder = "./APP_DATA/annotations"
os.makedirs(anns_folder, exist_ok=True)

import ast
import csv

from supervisely.io.fs import get_file_name

# Open the annotations.csv file
with open("./APP_DATA/annotations.csv", "r") as file:
    csvreader = csv.DictReader(file)

    # Create a dictionary to store annotations for each image_id
    annotations = {}

    # Iterate over each row in the CSV file
    for row in csvreader:
        image_id = row["image_id"]
        bounds = ast.literal_eval(row["bounds"])
        class_name = row["class"]

        # Append the class name and geometry to the image's annotations
        if image_id in annotations:
            annotations[image_id].append((class_name, bounds))
        else:
            annotations[image_id] = [(class_name, bounds)]

    # Iterate over the annotations and write them to separate .txt files
    for image_id, class_geometries in annotations.items():
        with open(f"{anns_folder}/{get_file_name(image_id)}.txt", "w") as txtfile:
            for class_name, bounds in class_geometries:
                txtfile.write(f"{class_name}|{bounds}\n")
