# ML-Zoomcamp-Capstone2-BitCoinPricePrediction
## Welcome
So far I have been working in two different projects related to ML for the ZoomCamp course, one for engineering application, and other for medical application. In this third project I would like to do something related to financial applications. One of the most exiting fields in the past decadate, for good and for bad, has been the cryptocurrencies, being the most famouns and the one that started this era the Bitcoin. In thirs project I will create a model to for Bitcoin prediction.

This project was divided into the following parts:
1. Why Bitcoin Price Prediction?
2. Dataset
3. Data Analysis
4. Models Tested
5. Train the Selected Model with your Data Set
6. Run the Python Files for the model in PipEnv
7. Containerized model test

## Why Bitcoin Price Prediction?
Finance is a great part of our world, and in the last decade a new player has erupted in the currency escenario: Bitcoin.
In it's origins the propurse was to be a currency of normal use, but due to the high volatility, it has not been employed as such but more as value storage. For this reason, having a predictable behavior of the Bitcoin price would be a great advantage for the development of the currency, and ML could be of help for this task.

I know that this is not possible with simple parameters, and a simple model, to predict a currency price as it is dependand of a lot of factors correlated to other activities and events that are not visible in the price history, but anyway it is an interesting experiment for an ML project.

## Dataset
This project will I have used a dataset downloaded from the following page: https://www.cryptodatadownload.com/data/bitstamp/. The employed Dataset includes information from the data set include the following elements from 2016 to 2024:

    Unix Timestamp - This is the unix timestamp or also known as "Epoch Time". Use this to convert to your local timezone
    Date - This timestamp is converted to NY EST Standard Time
    Symbol - The symbol for which the time series data refers
    Open - This is the opening price of the time period
    High - This is the highest price of the time period
    Low - This is the lowest price of the time period
    Close - This is the closing price of the time period
    Volume (Crypto) - This is the volume in the transacted Ccy. Ie. For BTC/USDT, * this is in BTC amount
    Volume Base Ccy - This is the volume in the base/converted ccy. Ie. For BTC/USDT, this is in USDT amount

## Data Analysis
The Complete Datanalysis can be checkied in the following link: 
[Data Analysis and Engineering for Bitcoin Price](https://github.com/AndresLDF/ML-Zoomcamp-Capstone2-BitCoinPricePrediction/blob/main/Notebooks/Data_Analysis_and_Engineering_for_Bitcoin_Price.ipynb)

Basically to solve the issue of not using a model that takes as feed time serias like Long Short-term Memory model for prediction, and be able to just use simple models, I have calculated the following parameters for each data point using the previous dataset informaiton:
* Slope for the tendency line for 7 days before
* Slope for the tendency line for 30 days before
* Slope for the tendency line for 90 days before

## Models tested
 The Following Models where Tested:
*   Regression Tree
* 	Regression Forest
* 	Gradient Boosting
* 	Neural Network Simple Model

The tree based models can be found on the following link:
[Tree Models](https://github.com/AndresLDF/ML-Zoomcamp-Capstone2-BitCoinPricePrediction/blob/main/Notebooks/Tree_Based_Model_Selection_for_BTC_Prediction.ipynb)
The Neural Network model can be found on the following link: [Neural Network Model](https://github.com/AndresLDF/ML-Zoomcamp-Capstone2-BitCoinPricePrediction/blob/main/Notebooks/Neural_Networks_Model_Selection_for_BTC_price_prediction.ipynb)

### Selected Model
The model selected was the Gradien Boosting model. It was the moderl with better performance. 
More details on the selection and final training here: [Final Model Selection](https://github.com/AndresLDF/ML-Zoomcamp-Capstone2-BitCoinPricePrediction/blob/main/Notebooks/Final_Model_selection_and_Training.ipynb)

## Train the Selected Model with your Data Set
1. Clone this repository into your local machine
2. Delete the Datasets in the Datasets folder
3. Add your Dataset on the folder Datasets and rename it to BTCEUR.csv
4. In the root directory for your cloned project open a terminal
5. Run the command ```python preparation.py```
6. Delete the files in the folder Trained_Models
7. Now run the following command in the previously opened shell ```python train.py```
8. The models will be available in the folder Trained_Models

## Run the Python Files for the model in PipEnv
1. Clone this repository into your local machine
2. Open your command shell
4. Go to the directory where the cloned repository  was stored
5. Run the command pipenv install
6. Run this code ```pipenv run waitress-serve --listen=localhost:9696 predict:app```
7. Open a second command shell in the same folder
8. Run the following code: ```python test.py```

## Containerized model test
To work with a containerized model, you should follow these steps:
1. Clone this repository into your local machine
2. Open your command shell
3. Go to the directory where the cloned repository was stored
4. Be sure that Docker is working in your system and type ``` docker build -t btcp:001 . ```
6. Once the build is ready, type   docker run -p 9696:9696  btcp:001 ```
7. Open another terminal on the same folder
8. Now type ``` python test.py ```

You should be able to get the console run following this steps. You can open the file test.py with an editor and chage the information used in line 6 to test different bitcoin prices

