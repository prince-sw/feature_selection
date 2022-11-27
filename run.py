from datasets.config import data_files
from feature_classification.classify import classify_dataset

if __name__ == "__main__":
    for dataset in data_files:
        classify_dataset(dataset)
    print("Exiting...\n")
