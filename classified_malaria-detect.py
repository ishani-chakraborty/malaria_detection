import pandas as pd
import sklearn.model_selection import train_test_split
import sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import sklearn import metrics
import joblib

## load dataset.csv
dataframe = pd.read_csv("csv/dataset.csv")
print(dataframe.head())

#Split into training and test data
 data_x = dataframe.drop(["Label"], axis=1)
 data_y = dataframe["Label"]
 trained_x, test_x, trained_y, test_y = train_test_split(data_x, data_y, test_size=0.2, random_state-4)

 ## Build the model
 model = RandomForestClassifier(num_estimators=100, max_depth=5)
 model.fit(trained_x,trained_y)
 joblib.dump(model, "rf_malaria_100_5")

 # Create and build predictions and get classification report on the trained data
 predictions = model.predict(test_x)
 print(metrics.classification_report(predictions, test_y ))
 