import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def draw_scatterplot(df, x="X", y="Y", hue=None, label=None):
    sns.scatterplot(data=df, x=x, y=y, hue=hue)

    def label_point(x, y, val, ax):
        a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
        for i, point in a.iterrows():
            ax.text(point['x'] + .03, point['y'], str(point['val']))

    if label is not None:
        label_point(df[x], df[y], df[label], plt.gca())
