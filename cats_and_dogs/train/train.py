import argparse

import mlflow.keras

from steps.inference import Inference
from steps.extraction import extraction_from_annotation_file
from steps.split import random_split_train_evaluate_test_from_extraction
from steps.test import test_model
from steps.train_and_evaluate import train_and_evaluate_model

parser = argparse.ArgumentParser("training")
parser.add_argument("--split_ratio_train", type=float)
parser.add_argument("--split_ratio_evaluate", type=float)
parser.add_argument("--split_ratio_test", type=float)
parser.add_argument("--batch_size", type=int)
parser.add_argument("--epochs", type=int)
parser.add_argument("--working_dir", type=str)
parser.add_argument("--model_filename", type=str)
parser.add_argument("--model_plot_filename", type=str)

args = parser.parse_args()
split_ratio_train = args.split_ratio_train
split_ratio_evaluate = args.split_ratio_evaluate
split_ratio_test = args.split_ratio_test
batch_size = args.batch_size
epochs = args.epochs
working_dir = args.working_dir
model_filename = args.model_filename
model_plot_filename = args.model_plot_filename

if __name__ == "__main__":
    with mlflow.start_run():
        mlflow.log_param("split_ratio_train", split_ratio_train)
        mlflow.log_param("split_ratio_evaluate", split_ratio_evaluate)
        mlflow.log_param("split_ratio_test", split_ratio_test)
        mlflow.log_param("batch_size", batch_size)
        mlflow.log_param("epochs", epochs)
        mlflow.log_param("working_dir", working_dir)
        mlflow.log_param("model_filename", model_filename)
        mlflow.log_param("model_plot_filename", model_plot_filename)

        # extraction
        extract, classes = extraction_from_annotation_file("./cats_and_dogs/label/output/cats_dogs_others-annotations.json")

        # random split

        train_dir = working_dir + "/train"
        evaluate_dir = working_dir + "/evaluate"
        test_dir = working_dir + "/test"

        random_split_train_evaluate_test_from_extraction(extract, classes, split_ratio_train,
                                                         split_ratio_evaluate, split_ratio_test,
                                                         train_dir, evaluate_dir, test_dir)

        # train & evaluate
        model_dir = working_dir + "/model"
        model_path = model_dir + "/" + model_filename
        plot_filepath = model_dir + "/" + model_plot_filename

        train_and_evaluate_model(train_dir, evaluate_dir, test_dir, model_dir, model_path,
                                 plot_filepath, batch_size, epochs)

        # test the model
        model_inference = Inference(model_path)

        test_model(model_inference, model_dir, test_dir)
