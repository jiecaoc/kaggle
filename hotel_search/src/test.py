# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:21:36 2013

@author: jiecaoc
"""

import data_io

def test_trainingData():
    print("Loading processed data ...")
    features, targets = data_io.load_processed_data()
    print("Loading Regressor ... ")
    classifier = data_io.load_model()
    print("Doing prediction ...")
    predictions = classifier.predict(features)
    results = zip(targets[:100], predictions[:100])
    results = sorted(map(lambda x: abs(x[0] - x[1]), results))
    return sum(results) / len(results)

error = test_trainingData()
print "Error rate:", error