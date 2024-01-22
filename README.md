# ML-Zoomcamp-Capstone2-BitCoinPricePrediction
## Welcome
So far I have been working in two different projects related to ML, one for engineering application, and other for medical application. In this third project I would like to do something related to financial application. For this the prediction of Bitcoin price will be selected.

This project was devided into the following parts:
1. Why Bitcoin Price Prediction?
2. Dataset Employed
3. Models Differences
4. Local Deployment of the model

## Why Bitcoin Price Prediction?
Finance is a great part of our world, and in the last deacadate a new player has irrupted in the currency escenario: Bitcoin
If the original propurse was intended as a currency, due to the high volatitily, it has not been employed as such. For this reason, having a predictable beheivior of the Bitcoing price would be a great advantage for the development of the currency. 

Of course, I know that this is not possible with simple parameters, but it is an interesting experiment to do for ML.


## Dataset
This project will use a datast downloaded from the cryptodownload page https://www.cryptodatadownload.com/data/bitstamp/. The employed Dataset includes information from the data set include the following elements from 2016 to 2024:

    Unix Timestamp - This is the unix timestamp or also known as "Epoch Time". Use this to convert to your local timezone
    Date - This timestamp is converted to NY EST Standard Time
    Symbol - The symbol for which the timeseries data refers
    Open - This is the opening price of the time period
    High - This is the highest price of the time period
    Low - This is the lowest price of the time period
    Close - This is the closing price of the time period
    Volume (Crypto) - This is the volume in the transacted Ccy. Ie. For BTC/USDT, * this is in BTC amount
    Volume Base Ccy - This is the volume in the base/converted ccy. Ie. For BTC/USDT, this is in USDT amount

## Data Analysis
The Complete Datanalysis can be checkied in the following link: 
[Data Analysis and Engineering for Bitcoin Price](https://github.com/AndresLDF/ML-Zoomcamp-Capstone2-BitCoinPricePrediction/blob/main/Notebooks/Data_Analysis_and_Engineering_for_Bitcoin_Price.ipynb)

Basically to solve the issue of not using a model that takes all a data from recent past,  I have don the following:
* Calculated the slope for the tendency line for 7 days
* Calculated the slope for the tendency line for 30 days
* Calculated the slope for the tendency line for 90 days

## Models tested
 The Following Models where Tested:
*  Regression Tree
* 	Regression Forest
* 	Gradient Boosting
* 	Neural Network Simple Model

The tree based models can be found on the following link:
[Tree Models](https://github.com/AndresLDF/ML-Zoomcamp-Capstone2-BitCoinPricePrediction/blob/main/Notebooks/Tree_Based_Model_Selection_for_BTC_Prediction.ipynb)
The Neural Network model can be found on the following link: [Neural Network Model](https://github.com/AndresLDF/ML-Zoomcamp-Capstone2-BitCoinPricePrediction/blob/main/Notebooks/Neural_Networks_Model_Selection_for_BTC_price_prediction.ipynb)

### Selected Model
The model selected was the Gradien Boosting model. It has the better performance. 
More details on the selection and final training here: [Final Model Selection](https://github.com/AndresLDF/ML-Zoomcamp-Capstone2-BitCoinPricePrediction/blob/main/Notebooks/Final_Model_selection_and_Training.ipynb)

## Run the Python Files for the model in PipEnv
1. Clone this repository into your local machine
2. Open your command shell
4. Go to the directory where the cloned repositore was stored
5. Run the command pipenv install
6. Run this code ```pipenv run waitress-serve --listen=localhost:9696 predict:app```
7. Open a second comand shell in the same folder
8. Run the follwing code: ```python test.py```

## Containerized model test
To work with the selected model, you can use the image prepared to be used with AWS Lambda. To test the image you shoudl follow the follwing steps:
1. Clone this repository into your local machine
2. Open your command shell
3. Go to the directory where the cloned repositore was stored
4. Be sure that Docker is working in your system and type ``` docker build -t btcp:001 . ```
6. Once the build is ready, type   docker run -p 9696:9696  btcp:001 ```
7. Open another terminal on the same folder
8. Now type ``` python test.py ```

You should be able to get the console run following this steps. You can open the file test.py with an editor and chage the information used in line 6 to test different bitcoin prices

