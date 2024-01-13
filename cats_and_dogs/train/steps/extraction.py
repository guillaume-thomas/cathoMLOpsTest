import json
from typing import Any


def extraction_from_annotation_file(filename: str) -> tuple[dict[Any, Any], set[Any]]:
    extract = {}
    classes = set()
    with open(filename) as file:
        annotations = json.load(file)["annotations"]
        for annotation in annotations:
            label = annotation["annotation"]["label"]
            extract[annotation["fileName"]] = label
            classes.add(label)
    return extract, classes
