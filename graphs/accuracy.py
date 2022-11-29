import matplotlib.pyplot as plt
import pandas as pd
from datasets.config import data_files

fs_methods = ['corr', 'tree', 'var', 'lrs',
              'rfe', 'bor', 'lass', 'muin', 'chi', 'rfc']

models = ['lr', 'nb', 'knn', 'rf', 'dt']


def save_figs(k, scores, fs_method, name):
    plt.figure(figsize=(14, 5))
    for model in models:
        plt.plot(range(1, k+1), scores[model], label=model)
    plt.title("{}//{}".format(name, fs_method))
    plt.xlabel("No. of features")
    plt.xticks(range(1, k+1))
    plt.ylabel("Accuracy")
    plt.legend(loc='upper right')
    plt.savefig('./plots/{}_{}.png'.format(name, fs_method))
    plt.close()


def save_acc_results(dataset):
    df = pd.read_csv("./results/{}.txt".format(dataset["name"]))
    for fs_method in fs_methods:
        columns = max(df["k"])
        scores = {
            "lr": [],
            "nb": [],
            "knn": [],
            "rf": [],
            "dt": []
        }
        for i in range(1, columns):
            for model in models:
                q = "fs_method=='{}' and model=='{}' and k=={}".format(
                    fs_method, model, i)
                acc = df.query(q)["accuracy"].iloc[0]
                scores[model].append(acc)
        for model in models:
            q = "fs_method=='{}' and model=='{}' and k=={}".format(
                fs_method, model, i)
            acc = df.query(q)["accuracy"].iloc[0]
            scores[model].append(acc)
        save_figs(columns, scores, fs_method, dataset["name"])
