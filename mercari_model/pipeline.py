from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

from mercari_model import config

pipeline = Pipeline(
    [
        ("vect", TfidfVectorizer(ngram_range=(1,2), lowercase=True, stop_words={"english"})),
        # ("clf", LogisticRegression(random_state=config.RANDOM_SEED, C=1, max_iter=300)),
        ("clf", LinearSVC(C=1)),
    ]
)
