import pandas as pd

df = pd.read_csv('../data/PS_20174392719_1491204439457_log.csv')
# column names ['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig',
# 'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud',
# 'isFlaggedFraud']
print(df.head())
