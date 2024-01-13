import json
from typing import Any

import mlflow


def extraction_from_annotation_file(filename: str) -> tuple[dict[Any, Any], set[Any]]:
    extract = {}
    classes = set()
    with open(filename) as file:
        annotations = json.load(file)["annotations"]
        for annotation in annotations:
            label = annotation["annotation"]["label"]
            extract[annotation["fileName"]] = label
            classes.add(label)
    mlflow.log_dict(extract, "annotations/extract.json")
    return extract, classes
