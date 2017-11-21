"""
classify.py
"""
import sys
import pickle
import os
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
import pandas as pd

def main():
    f = open('./data/tweets.txt', 'rb')
    tweets = pickle.load(f)
    f2 = open('./data/users.txt', 'rb')
    users = pickle.load(f2)
    user_list = sorted([u['screen_name'] for u in users])
    test_data = []
    for u in user_list:
        for t in tweets[u]:
            test_data.append(t['text'])
    train_data_pd = pd.read_csv('./data/trainData.csv', encoding = "utf8")
    train_labels = train_data_pd['polarity'].tolist()
    train_data = train_data_pd['text'].tolist()
    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)


    # Perform classification with SVM, kernel=rbf
    classifier_rbf = svm.SVC()
    t0 = time.time()
    classifier_rbf.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_rbf = classifier_rbf.predict(test_vectors)
    t2 = time.time()
    time_rbf_train = t1-t0
    time_rbf_predict = t2-t1


    # Perform classification with SVM, kernel=linear
    classifier_linear = svm.SVC(kernel='linear')
    t0 = time.time()
    classifier_linear.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_linear = classifier_linear.predict(test_vectors)
    t2 = time.time()
    time_linear_train = t1-t0
    time_linear_predict = t2-t1


    # Perform classification with SVM, kernel=poly, degree=3
    classifier_poly = svm.SVC(kernel='poly')
    t0 = time.time()
    classifier_poly.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_poly = classifier_poly.predict(test_vectors)
    t2 = time.time()
    time_poly_train = t1-t0
    time_poly_predict = t2-t1

    list_of_summarize = []
    pos = neg = 0

    for r in prediction_linear:
        if r == 4:
            pos += 1
        else:
            neg += 1

    list_of_summarize.append(pos)
    list_of_summarize.append(neg)

    list_of_summarize.append(prediction_linear[0])
    list_of_summarize.append(test_data[0])

    f4 = open('./data/sum.txt','ab')
    pickle.dump(list_of_summarize, f4)
    #print(type(prediction_linear))


    print("Results for SVC(kernel=rbf)")
    print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    # print(classification_report(test_labels, prediction_rbf))
    print(prediction_rbf)
    print("Results for SVC(kernel=linear)")
    print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
    # print(classification_report(test_labels, prediction_linear))
    print(prediction_linear)

    print("Results for SVC(kernel=poly)")
    print("Training time: %fs; Prediction time: %fs" % (time_poly_train, time_poly_predict))
    # print(classification_report(test_labels, prediction_poly))
    print(prediction_poly)

if __name__ == '__main__':
    main()