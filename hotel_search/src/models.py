# This package include the core methods
# to train the model.
# by Jiecao Chen

import numpy as np

class RandomForest:
    """
        Random Forest model
    """
    def __init__(self, numOfFeatures = 10, numOfTrees = 20):
        self.numOfFeatures = numOfFeatures
        self.numOfTrees = numOfTrees
    
    def fit(self, listOfFeatures, listOfTarget):
        """
            Target should be a float number,
            return a classfier
        """
        return (lambda x: 1)

        
