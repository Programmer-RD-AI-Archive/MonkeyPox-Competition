import pandas as pd
import numpy as np
import random
data = pd.read_csv("./owid-monkeypox-data.csv")
countries = dict(data["location"].value_counts())
data_test = []
cases = []
for country in countries:
    random_choice = random.choice(data[data["location"] == country].index.tolist())
    print(random_choice)
    data_t = data[data["location"] == country].iloc[3923]
    cases.append(data_t["new_cases"])
    del data_t["new_cases"]
    data_test.append(data_t)
    if len(data[data["location"] == country]) != 1:
        data = data.drop(index=data.index[data["location"] == country].tolist()[random_choice])
data_test = pd.DataFrame(data_test)
print(data_test.index.tolist())
true_submission = pd.DataFrame({"index": data_test.index.tolist(), "Num of Cases": cases})
true_submission.to_csv("True_Submission.csv")
sample_submission = pd.DataFrame(
    {"index": data_test.index.tolist(), "Num of Cases": np.zeros(len(data_test.index.tolist()))}
)
sample_submission.to_csv("sample_submission.csv", index=False)
data.to_csv("Data.csv")
data.to_json("Data.json")
data_test.to_csv("Test_Data.csv")
data_test.to_json("Test_Data.json")
