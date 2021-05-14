import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib

from mercari_model import config
from mercari_model import pipeline


def run_training():
    # read training data
    df = pd.read_csv(config.TRAIN_PATH, sep="\t")

   # split categories into 5 column
    df[['cat1', 'cat2', 'cat3', 'cat4', 'cat5']] = df.category_name.str.split("/", expand=True)

    # concat name and desc into one column
    df['name_desc'] = df['name'] + " " + df['item_description']

    # filter data so that it only contains two columns: name_desc, first category
    df = df[['name_desc', 'cat1']]

    # drop rows with uncategorized items
    df = df.dropna(subset=['cat1'])

    # downsample the dataset based on the label with the least number of items
    min_sample = df['cat1'].value_counts().min()
    women = df.loc[df.cat1 == "Women"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    men = df.loc[df.cat1 == "Men"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    beauty = df.loc[df.cat1 == "Beauty"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    kids = df.loc[df.cat1 == "Kids"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    elec = df.loc[df.cat1 == "Electronics"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    home = df.loc[df.cat1 == "Home"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    vintage = df.loc[df.cat1 == "Vintage & Collectibles"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    other = df.loc[df.cat1 == "Other"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    handmade = df.loc[df.cat1 == "Handmade"].sample(n=min_sample, random_state=config.RANDOM_SEED)
    df = pd.concat([women, men, beauty, kids, elec, home, vintage, other, handmade, df.loc[df.cat1 == "Sports & Outdoors"]])
    df= df.reset_index(drop=True)
    print(df.cat1.value_counts())

    # sample so we use only 40% of the downsampled dataset
    df = df.sample(frac=0.4, random_state=config.RANDOM_SEED).reset_index(drop=True)

    # enumerate labels and create a new column
    possible_labels = df.cat1.unique()
    label_dict = {}
    for index, possible_label in enumerate(possible_labels):
        label_dict[possible_label] = index
    df['label'] = df.cat1.replace(label_dict)
    print(df.cat1.value_counts())

    # split the dataset for training and evaluation
    X_train, X_test, y_train, y_test = train_test_split(df['name_desc'], df['cat1'], random_state=config.RANDOM_SEED)

    # train and evaluate on training set
    predicted = pipeline.lr_tfidf_pipeline.fit(X_train, y_train).predict(X_train)
    print(metrics.classification_report(
        y_train, predicted, target_names=df['cat1'].unique()))

    joblib.dump(pipeline.lr_tfidf_pipeline, config.PIPELINE_NAME)


if __name__ == "__main__":
    run_training()
