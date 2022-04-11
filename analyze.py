import pandas as pd
import matplotlib.pyplot as plt

from lightgbm import LGBMClassifier, plot_importance, LGBMRanker


def true_or_false(df):
    for i in df:
        if d == 'decline':
            d = 0
        else:
            d = 1

df = pd.read_excel('data.xlsx', index_col='Unnamed: 0')
df['applyStatus'] = df['applyStatus'].replace(['decline', 'accept'], [0, 1])
df['userGender'] = df['userGender'].replace(['women', 'man'], [0, 1])
df['updateDate'] = pd.to_datetime('2021-03-24') - pd.to_datetime(df['updateDate'])
df['updateDate'] = df['updateDate'].dt.days
df['viewCount'] = df['viewCount'].apply(lambda x: 1 if x >  df['viewCount'].mean() else 0)
lgb = LGBMClassifier(n_estimators=400)

x = df.drop(['userId', 'applyStatus', 'viewCount'], axis=1)
y = df['viewCount']

train_x = x.iloc[:-1000]
train_y = y.iloc[:-1000]
val_x = x.iloc[-1000:]
val_y = y.iloc[-1000:]
eval_set = (val_x, val_y)
print(y)
lgb.fit(x, y, early_stopping_rounds=100, eval_set=eval_set, eval_metric='logloss', verbose=True)

fig, ax = plt.subplots(figsize=(10, 12))

impt = plot_importance(lgb, ax=ax)
impt.set(title='feature importance',
         xlabel='Feature Importance',
         ylabel='Features')
impt.figure.savefig("features.png", dpi=300)