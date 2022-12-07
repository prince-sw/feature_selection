from feature_selection.supervised import *
from feature_selection.unsupervised import *


def feature_selector(df, label, k):
    features_selected = {}
    print("Selecting Features with correlation")
    features_selected["corr"] = corr_selection(df, label, k)
    print("Selecting Features with tree")
    features_selected["tree"] = treebased_selection(df, label, k)
    print("Selecting Features with variance")
    features_selected["var"] = variance_selection(df, label, k)
    print("Selecting Features with logistic regression")
    features_selected["lrs"] = logistic_regression_selection(df, label, k)
    print("Selecting Features with rfe")
    features_selected["rfe"] = rfe_selection(df, label, k)
    print("Selecting Features with boruta")
    features_selected["bor"] = boruta_selection(df, label, k)
    print("Selecting Features with lasso")
    features_selected["lass"] = Lasso_selection(df, label, k)
    print("Selecting Features with mutual info")
    features_selected["muin"] = Mutualinfo_selection(df, label, k)
    print("Selecting Features with chi test")
    features_selected["chi"] = chitest_selection(df, label, k)
    print("Selecting Features with random forest")
    features_selected["rfc"] = randomforest_Selection(df, label, k)
    print("Selecting with unsupervised methods...\n")
    print("Selecting Features with laplacian")
    features_selected["ulap"] = laplacian_selection(df, k)
    print("Selecting Features with iterative laplacian")
    features_selected["uilap"] = iterlaplacian_selection(df, k)
    print("Selecting Features with cosine similarity")
    features_selected["ucos"] = cosine_selection(df, k)
    print("Selecting Features with pairwise corr")
    features_selected["upcorr"] = pairwise_corr_selection(df, k)
    print("Selecting Features with frufs")
    features_selected["ufrufs"] = frufs_selection(df, k)
    return features_selected
