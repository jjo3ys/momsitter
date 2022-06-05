import warnings
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
warnings.filterwarnings(action='ignore')


last_date = pd.to_datetime('2021-03-24')

df = pd.read_csv('data.csv')

df['applyStatus'] = df['applyStatus'].replace(['decline', 'accept'], [0, 1])
df['userGender'] = df['userGender'].replace(['women', 'man'], [0, 1])
df['updateDate'] = last_date - pd.to_datetime(df['updateDate'])
df['updateDate'] = df['updateDate'].dt.days
# df['viewCount'] = df['viewCount'].apply(lambda x: 1 if x >  df['viewCount'].mean() else 0)

# x = df.drop(['userId', 'applyStatus', 'viewCount'], axis=1)
# y = df['viewCount']
x = df.drop(['userId', 'applyStatus'], axis=1)
y = df['applyStatus']
test_x = x.iloc[8000:]
test_y = y.iloc[8000:]
x = x.iloc[:8000]
y = y.iloc[:8000]

train_x, val_x, train_y, val_y = train_test_split(x, y, test_size=0.2, random_state=42)


eval_set = (val_x, val_y)

def lgbm(train_x, train_y, eval_set, test_x, test_y):
    from lightgbm import plot_importance, plot_metric
    from lightgbm import LGBMClassifier

    lgb = LGBMClassifier(n_estimators=50, max_depth=2)

    lgb.fit(train_x, train_y, eval_set=eval_set, eval_metric='binary', verbose=False)
    pred_y = lgb.predict(test_x)

    for i in range(len(pred_y)):
        if pred_y[i] >= 0.5:
            pred_y[i] = 1
        else:
            pred_y[i] = 0
    accuracy = accuracy_score(test_y, pred_y)
    binary_loss = plot_metric(lgb)
    binary_loss.set(ylabel='binary_logloss')
    binary_loss.figure.savefig("applyStatus_model_lgbm.png")
    print("lightGBM accuracy: {}%".format(round(accuracy, 3)*100))
    # fig, ax = plt.subplots(figsize=(10, 12))

    # impt = plot_importance(lgb, ax=ax)
    # impt.set(title='feature importance',
    #          xlabel='Feature Importance',
    #          ylabel='Features')
    # impt.figure.savefig("apply_status_features.png", dpi=500)

def rdm_forest(train_x, train_y, eval_set, test_x, test_y):
    from sklearn.ensemble import RandomForestClassifier

    rdm_clf = RandomForestClassifier(n_estimators=50, max_depth=2)
    rdm_clf.fit(train_x, train_y)
    pred_y = rdm_clf.predict(test_x)
    accuracy = accuracy_score(test_y, pred_y)
    print("Random Forest accuracy: {}%".format(round(accuracy, 3)*100))

def xgb_boost(train_x, train_y, eval_set, test_x, test_y):
    import xgboost as xgb
    from xgboost import plot_importance

    # params = {'max_depth' : 2,
    #      'objective' : 'binary:logistic',
    #      'eval_metric' : 'binary',
    #      'early_stoppings' : 100 }

    # xgb_train = xgb.DMatrix(data=train_x, label=train_y)
    # xgb_val = xgb.DMatrix(data=val_x, label=val_y)
    # xgb_test = xgb.DMatrix(data=test_x, label=test_y)
    # xgb_model = xgb.train(params=params, dtrain=xgb_train, num_boost_round=50, evals=[(xgb_train, 'train'), (xgb_val, 'eval')])
    # pred = xgb_model.predict(xgb_test)
    loss_func = 'logloss'
    model = xgb.XGBClassifier(n_estimators=50, max_depth=2)
    model.fit(train_x, train_y, eval_set=[(train_x, train_y), (val_x, val_y)], eval_metric=loss_func, verbose=False)
    pred = model.predict(test_x)
    pred = [1 if x>=0.5 else 0 for x in pred]

    accuracy = accuracy_score(test_y, pred)
    print("XGB accuracy: {}%".format(round(accuracy, 3)*100))
    results = model.evals_result()
    x_axis = range(0, len(results['validation_0'][loss_func]))
    fig, ax = plt.subplots()
    ax.plot(x_axis, results['validation_0'][loss_func], label='Train')
    ax.plot(x_axis, results['validation_1'][loss_func], label='val')
    ax.legend()
    plt.savefig("applyStatus_model_xgboost.png")
    # xgb = XGBClassifier(n_estimators=50, max_depth=2)
    # xgb.fit(train_x, train_y, eval_metric='error', eval_set=eval_set)
    # pred_y = xgb.predict(test_x)

    # for i in range(len(pred_y)):
    #     if pred_y[i] >= 0.5:
    #         pred_y[i] = 1
    #     else:
    #         pred_y[i] = 0

rdm_forest(train_x, train_y, eval_set, test_x, test_y)
xgb_boost(train_x, train_y, eval_set, test_x, test_y)
lgbm(train_x, train_y, eval_set, test_x, test_y)