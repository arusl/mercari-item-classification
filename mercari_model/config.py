import mercari_model
import pathlib

PACKAGE_ROOT = pathlib.Path(mercari_model.__file__).resolve().parent

RANDOM_SEED = 0

TRAIN_PATH= PACKAGE_ROOT / "datasets/train.tsv"
TEST_PATH= PACKAGE_ROOT / "datasets/test.tsv"

PIPELINE_NAME= PACKAGE_ROOT / "trained_models/lr_cv_pipeline.pkl"

LABEL_DICT = {'Beauty': 0, 'Handmade': 1, 'Vintage & Collectibles': 2, 'Men': 3, 'Women': 4, 'Kids': 5, 'Electronics': 6, 'Sports & Outdoors': 7, 'Other': 8, 'Home': 9}