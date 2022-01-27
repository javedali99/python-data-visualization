import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.svm import LinearSVR
from tpot.builtins import StackingEstimator

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Average CV score on the training set was:-0.0037366571337227442
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=LinearSVR(C=0.001, dual=True, epsilon=0.01, loss="epsilon_insensitive", tol=0.001)),
    StackingEstimator(estimator=ExtraTreesRegressor(bootstrap=True, max_features=0.1, min_samples_leaf=5, min_samples_split=8, n_estimators=100)),
    ExtraTreesRegressor(bootstrap=True, max_features=0.45, min_samples_leaf=2, min_samples_split=9, n_estimators=100)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
