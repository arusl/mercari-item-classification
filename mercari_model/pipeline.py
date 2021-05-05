from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from mercari_model import config

lr__cv_pipeline = Pipeline(
    [
        ("cvect", CountVectorizer(lowercase=True, stop_words={"english"})),
        ("clf", LogisticRegression(random_state=config.RANDOM_SEED)),
    ]
)
