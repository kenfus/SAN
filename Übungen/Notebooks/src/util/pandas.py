import pandas as pd


def expand_df(df, label, mapping):
    df[label] = pd.Series(mapping)


def set_index_as_label(df):
    df["Label"] = df.index
