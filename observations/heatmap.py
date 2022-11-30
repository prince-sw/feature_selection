from datasets.config import data_files
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fs_methods = ['corr', 'tree', 'var', 'lrs',
              'rfe', 'bor', 'lass', 'muin', 'chi', 'rfc']

models = ['lr', 'nb', 'knn', 'rf', 'dt']


def save_heatmap(dataset, scores, k):
    sns.heatmap(scores, xticklabels=fs_methods,
                yticklabels=models, square=True, cmap=sns.color_palette("Blues", 12))
    plt.title("Accuracy Heatmap for {}, k={}".format(dataset, k))
    plt.savefig('./plots/heatmap/{}.png'.format(dataset))
    plt.close()


def plot_heatmaps():
    df = pd.read_csv("./tables/acc_table.txt")
    for dataset in data_files:
        score_df = pd.read_csv("./results/{}.txt".format(dataset["name"]))
        row = df.query("dataset == '{}'".format(dataset["name"]))
        k = row["k"].iloc[0]
        print("Calculating heatmap for {}, k={}".format(dataset["name"], k))

        heat_scores = []
        for model in models:
            heat_row = []
            for fs_method in fs_methods:
                score_acc = score_df.query("model == '{}' and fs_method == '{}' and k == {}".format(
                    model, fs_method, k))["accuracy"].iloc[0]
                heat_row.append(score_acc)
            heat_scores.append(heat_row)

        print("Plotting heatmap for {}, k={}".format(dataset["name"], k))
        save_heatmap(dataset["name"], heat_scores, k)
