import pandas as pd
from sklearn.manifold import TSNE

def tsne(df):
    tsne = TSNE(n_components=2, random_state=7, perplexity=15)
    embeddings_2d = tsne.fit_transform(df)
    return pd.DataFrame({'X': embeddings_2d[:, 0], 'Y': embeddings_2d[:, 1]})