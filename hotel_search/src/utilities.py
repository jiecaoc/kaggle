# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:25:54 2013

@author: jiecaoc
"""

def preprocess(trainSample):
    """
        pre-process the trainSample
        given trainSample
        return a list of features
    """
    feature_names = list(trainSample.columns)
    feature_names.remove("click_bool")
    feature_names.remove("booking_bool")
    feature_names.remove("gross_bookings_usd")
    feature_names.remove("date_time")
    feature_names.remove("position")
    return trainSample[feature_names].values
    
def construct_target(trainSamples):
    """
        given trainSamples,
        return a list of targets
    """
    feature_names = ["click_bool", "booking_bool","position"]
    samples = trainSamples[feature_names].values
    def f(vec):
        x, y, z = vec
        return y + 0.2 * x
    return [f(vec) for vec in samples]