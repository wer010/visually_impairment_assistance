from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from data_preprocess import MyDataset
import numpy as np

def main():
    d = MyDataset('./data.xls')

    data_x, data_y = d.get_data(op=1, normalization=True)

    print(data_x.shape,data_y.shape)
    clf = LogisticRegression(random_state=0, solver='liblinear', max_iter=500)
    clf.fit(data_x,data_y)
    print(f'The acc of logistic regression model is {clf.score(data_x,data_y)}')
    print(f'The weight of LR model is {clf.coef_}, the bias of LR model is {clf.intercept_}')


    clf = svm.SVC(kernel='linear')
    clf.fit(data_x, data_y)
    print(f'The acc of SVM model with linear kernal is {clf.score(data_x, data_y)}')
    print(f'The weight of SVM model is {clf.coef_}, the bias of SVM model is {clf.intercept_}')

    clf = svm.SVC(kernel='rbf')
    clf.fit(data_x, data_y)
    print(f'The acc of SVM model with rbf kernal is {clf.score(data_x, data_y)}')
    # print(f'The weight of SVM model is {clf.coef_}, the bias of SVM model is {clf.intercept_}')

    clf = AdaBoostClassifier(n_estimators=100, random_state=0)
    clf.fit(data_x, data_y)
    print(f'The acc of Adaboost model is {clf.score(data_x, data_y)}')

    clf = MLPClassifier(alpha=1e-5, hidden_layer_sizes = (100, 50), random_state = 1, max_iter=2000)
    clf.fit(data_x, data_y)
    print(f'The acc of Neural Network model is {clf.score(data_x, data_y)}')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
