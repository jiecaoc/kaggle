
# Project: Personalize Expedia Hotel Searches
**by** [`Qian Zhao`](mailto:zhaox331@umn.edu), [`Jiecao Chen `](jieca001@umn.edu)
## Problem Description [`source`][1]
___
**Expedia** is the world’s largest online travel agency (OTA) and powers search results for millions of travel shoppers every day. In this competitive market matching users to hotel inventory is very important since users easily jump from website to website. As such, having the best ranking of hotels (“sort”) for specific users with the best integration of price competitiveness gives an OTA the best chance of winning the sale.

For this contest, Expedia has provided a dataset that includes shopping and purchase data as well as information on price competitiveness. 
___

## Task and Evaluation

Our mission in this competition is to train models that are able to rank hotels to maximize purchases, and the models will be scored via performance on a hold-out set.

## Tentative Methods
We are planning to divide the project into 5 phrase. A rough schedule  is listed as the following:
### Phase I (Two weeks)
* Gaussian Models(Gaussian Discremant) + Logistic Regression
* Latent Linear Models + Matrix Factorization (SVDFeature, Factorization Machine)



### Phase II (Two weeks)
* Learning to rank (Ranking loss)
* Sparse Linear Models(with L1-norm)

### Phase III (Two weeks)
* Kernel Methods(SVM)
* Adaptive Basis Function Models(GBDT)

### Phase IV (Two weeks)
* Refine the above models
* Try different optimization algorithms (gradient descent, Newton, coordinate descent, etc.)
* Gaussian Processes

## Ref & Keywords
* `libFM`
* `SVDFeature`
* `“Machine Learning: A Probabilistic Perspective” by Murphy (MLAPP)`
* `“Pattern Recognition and Machine Learning” by Bishop (PML)`
* `“Elements of Statistical Learning: Data Mining, Inference and Prediction” by Tibshirani and Friedman (ESL)`




[1]: https://www.kaggle.com/c/expedia-personalized-sort 
