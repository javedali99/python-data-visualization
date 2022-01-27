import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import LinearSVR
from tpot.builtins import StackingEstimator
from xgboost import XGBRegressor

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Average CV score on the training set was:-0.0032206897469491008
exported_pipeline = make_pipeline(
    MinMaxScaler(),
    StackingEstimator(estimator=GradientBoostingRegressor(alpha=0.85, learning_rate=0.01, loss="lad", max_depth=2, max_features=0.15000000000000002, min_samples_leaf=7, min_samples_split=7, n_estimators=100, subsample=0.4)),
    StackingEstimator(estimator=XGBRegressor(learning_rate=0.01, max_depth=10, min_child_weight=16, n_estimators=100, nthread=1, subsample=0.7500000000000001)),
    StackingEstimator(estimator=LinearSVR(C=10.0, dual=False, epsilon=0.0001, loss="squared_epsilon_insensitive", tol=0.1)),
    RandomForestRegressor(bootstrap=False, max_features=0.4, min_samples_leaf=6, min_samples_split=14, n_estimators=100)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
