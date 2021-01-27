from sklearn.linear_model import LogisticRegression
from data_preprocess import MyDataset
import numpy as np

def main():
    d = MyDataset('./data.xls')

    data_x, data_y = d.op_1st
    # data_x, data_y = d.op_2nd
    print(np.unique(data_y))
    print(data_x.shape,data_y.shape)
    clf = LogisticRegression(random_state=0).fit(data_x,data_y)
    s = clf.score(data_x,data_y)
    print(f'The acc of logistic regression model is {s}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
