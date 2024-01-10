import argparse
import os
from asyncio import get_event_loop

from mlopspython_extraction.extraction import extract_images

from ecotag import ApiInformation, Dataset, create_dataset, Project, Label, create_project

parser = argparse.ArgumentParser("labelling")
parser.add_argument("--jwt_token", type=str)
parser.add_argument("--dataset_folder", type=str)
parser.add_argument("--raw_dataset_subfolder", type=str)
parser.add_argument("--postprocess_dataset_subfolder", type=str)

args = parser.parse_args()
jwt_token = args.jwt_token
dataset_folder = args.dataset_folder
raw_dataset_subfolder = args.raw_dataset_subfolder
postprocess_dataset_subfolder = args.postprocess_dataset_subfolder

if __name__ == "__main__":
    # Initialisation du dataset
    raw_folder = dataset_folder + raw_dataset_subfolder
    postprocess_folder = dataset_folder + postprocess_dataset_subfolder
    if not os.path.isdir(postprocess_folder) or not os.listdir(postprocess_folder):
        res = extract_images(raw_folder, postprocess_folder)
        print("files input = " + str(res.number_files_input))
        print("files output = " + str(res.number_images_output))

    # Initialisation du projet ecotag
    api_url = 'http://localhost:5010/api/server'
    api_information = ApiInformation(api_url=api_url, jwt_token=jwt_token)

    dataset = Dataset(dataset_name='cats_dogs_others',
                      dataset_type='Image',
                      team_name='cats_dogs_others',
                      directory=postprocess_folder,
                      classification='Public')
    loop = get_event_loop()
    loop.run_until_complete(create_dataset(dataset, api_information))

    project = Project(project_name='cats_dogs_others',
                      dataset_name=dataset.dataset_name,
                      team_name='cats_dogs_others',
                      annotationType='ImageClassifier',
                      labels=[Label(name='cat', color='#FF0000', id="0"), Label(name='dog', color='#00FF00', id="1"), Label(name='other', color='#0000FF', id="2")])

    loop.run_until_complete(create_project(project, api_information))