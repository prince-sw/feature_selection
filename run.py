from datasets.config import data_files
from feature_classification.classify import classify_dataset
from graphs.accuracy import save_acc_results

if __name__ == "__main__":
    for dataset in data_files:
        # classify_dataset(dataset)
        save_acc_results(dataset)
    print("Exiting...\n")
