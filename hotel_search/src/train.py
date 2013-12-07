import data_io
from sklearn.ensemble import RandomForestRegressor #, RandomForestClassifier
import utilities as ut



def main():
    print("Reading training data ...")
    train = data_io.read_train()
    train.fillna(0, inplace=True)

    train_sample = train.fillna(value=0)

    features = ut.preprocess(train_sample)
    target = ut.construct_target(train_sample)
    # target = train_sample["booking_bool"].values
    # save the processed data, which may be useful 
    # to test the performance of our model
    print("Saving processed training data ...")
    data_io.save_processed_data([features, target])

    print("Training the Regressor ...")
    regressor = RandomForestRegressor(n_estimators=10, #RandomForestClassifier
                                        verbose=2,
                                        n_jobs=-1,
                                        max_features = "sqrt",
                                        min_samples_split=10,
                                        random_state=1)
    regressor.fit(features, target)
    
    print("Saving the Regressor ...")
    data_io.save_model(regressor)
    
if __name__=="__main__":
    main()
