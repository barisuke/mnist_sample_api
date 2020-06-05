from sklearn import svm
from sklearn import datasets
import joblib

def main():
    # classifier
    clf = svm.SVC()
    # data(iris)
    iris = datasets.load_iris()
    # Split train_x, train_y
    X, y = iris.data, iris.target
    # train
    clf.fit(X, y)
    # save model
    joblib.dump(clf, './trained-model/sample-model.joblib')

if __name__ == '__main__':
    main()