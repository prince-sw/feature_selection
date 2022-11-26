import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, make_scorer, f1_score, precision_score, recall_score, roc_auc_score


def get_results(model_name, results):
    ans = "{},{},{},{},{},{}\n".format(model_name,
                                       results["test_accuracy"].mean(),
                                       results["test_fmeasure"].mean(),
                                       results["test_precision"].mean(),
                                       results["test_recall"].mean(),
                                       results["test_roc"].mean(),
                                       )
    return ans


def write_score(f, model, results):
    f.write(get_results(model, results))


if __name__ == "__main__":
    df = pd.read_csv("./datasets/wine.csv", sep=";")
    model1 = LogisticRegression(max_iter=10000)
    model2 = GaussianNB()
    model3 = KNeighborsClassifier()
    model4 = RandomForestClassifier()
    model5 = DecisionTreeClassifier()
    models = {
        "lr": model1,
        "nb": model2,
        "knn": model3,
        "rf": model4,
        "dt": model5,
    }
    scoring = {
        "accuracy": make_scorer(accuracy_score),
        "fmeasure": make_scorer(f1_score, average="weighted", zero_division=0),
        "precision": make_scorer(precision_score, average="weighted", zero_division=0),
        "recall": make_scorer(recall_score, average="weighted", zero_division=0),
        "roc": make_scorer(roc_auc_score, average="weighted", multi_class="ovr", needs_proba=True)
    }
    file = open("results/result.txt", "w")
    file.write("model,accuracy,fmeasure,precision,recall,roc\n")
    for model in models.keys():
        results = cross_validate(estimator=models[model], X=df.drop(
            'quality', axis=1), y=df['quality'], cv=5, scoring=scoring, return_train_score=True, verbose=0)
        print("Done with {}".format(model))
        write_score(file, model, results)
    file.close()
