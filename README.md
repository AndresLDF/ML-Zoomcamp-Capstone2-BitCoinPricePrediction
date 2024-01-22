# ML-Zoomcamp-Capstone2-BitCoinPricePrediction
## Welcome
The main goal of this Capstone Project is to make a model for detecting skin cancer and set up the system for using it. I'll be using two pre-trained Keras applications, Xception and EfficientNet, without the top layers, to create three different models. Because of limited time and the limited free computing power available in Colab, I didn't try making more models or systems and I was not able to experiment with the done models as much as I would like. After checking, the best results I got a 0.71 accuracy on the validation dataset. This is far from the standards for detecting skin cancer in the industry, so, the model needs more work to usable in the medical field and only has a educative perspective. I will work beyond this course to make a model that works addecually. 

This project was devided into the following parts:
1. Why Skin Cancer Detection?
2. Dataset Employed
3. Models Differences
4. Models Optimization

## Why Skin Cancer Detection?
Skin cancer emerges as one of the rapidly proliferating diseases worldwide. It involves the uncontrolled development of abnormal skin cells. Detecting and diagnosing the disease early are crucial steps in identifying potential cancer therapies
[1].
The present challenge associated with manual identification performed by skilled medical professionals is its susceptibility to variation based on experience in the field. Even in the case of experts, there is a potential for mislabeling. For instance, the accuracy in diagnosing basal cell carcinoma (BCC), indicated by the higher positive predictive value (PPV), stands at 72.7% [2].
The application of AI models has proven to be an invaluable tool for skin cancer identification. This technology enables individuals with smartphones to achieve accuracies comparable to or surpassing those of trained experts [3].

* [1] Detection of Skin Cancer Based on Skin Lesion Images Using Deep Learning - Healthcare (Basel). 2022 Jul; 10(7): 1183. - 10.3390/healthcare10071183
* [2] Accuracy of clinical diagnosis of skin lesions -  Br J Dermatol. 2008 Sep;159(3):661-8 - 10.1111/j.1365-2133.2008.08715.x 
* [3] Assessment of Accuracy of an Artificial Intelligence Algorithm to Detect Melanoma in Images of Skin Lesions -  JAMA Netw Open. 2019;2(10):e1913436 - 10.1001/jamanetworkopen.2019.13436 


## Datasets
For the present work the Dataset from The International Skin Imaging Collaboration​ (ISIC) 2016 and 2017 challenge datasets were used:
* [Challenge 2016: Training](https://api.isic-archive.com/collections/74/)
* [Challenge 2016: Test](https://api.isic-archive.com/collections/61/)
* [Challenge 2017: Training](https://api.isic-archive.com/collections/60/)
* [Challenge 2017: Test](https://api.isic-archive.com/collections/69/)

The training datatasets were conbined and the test dataset were conbined too. For more details on the available datasets you can consult https://www.isic-archive.com/

## Models Differences
The models were trained using images from the dataset, and three categories were used for classification:
* Melanoma (Malign)
* Nevus
* Seborrheic_keratosis
For this work the following models were tried:
* X1.x Models
  ** Base Model: Xception without the top
  * Inner Layers: Single Dense Layer with Activation
  * Output layer: Single Dense layer with 3  neurons
* X2.x Models
  * Base Model: Xception without the top
  * Inner Layers: Two Dense Layer with Activation and normalization
  *  Output   layer: Single Dense layer with 3  neurons
* X3.x Models
  * Base Model: Xception without the top
  * Inner Layers: Three Dense Layer with Activation and normalization
  * Output layer: Single Dense layer with 3 neurons
* EN.x Models
  * Base Model: EfficientNetV2L without the top
  * Inner Layers: Single Dense Layer with Activation
  * Output layer: Single Dense layer with 3 neurons
 
 
## Models Optimization
In this section, all the models and variations done for optimization will be listed. To see each one on detail, you can open the notebooks for each model version in [here](https://github.com/AndresLDF/ML-Zoomcamp-Capstone1-SkinCancerDetection/tree/main/Models%20Notebooks)
### X1.x Models
The following attempts were made with this model:
* X1.1:
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (150, 150, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.64

*  X1.2:
    *  Difference with previous version:
        * The whole model is trained including the base model
    * Base Model Trainable: True
    * Inner layer size: 100 neurons
    * Input shape: (150, 150, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.2

*  X1.3:
    * Difference with previous version:
        * A higher input resolution of 400x400 is tried. Square images are fed.
        * The base model is not trained, default weights are used  
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (400, 400, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.69

*  X1.4:
    * Difference with previous version:
        * A higher input resolution of 800x800 is tried. Square images are fed.
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (800, 800, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.61

*  X1.5:
    * Difference with previous version:
        * In this version we use a similar resolution that in version 1.3, but instead of using an square relationship between the width and the heigh, we will use a relation af 1.332 that is closer to the original images
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (400, 533, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.71


*  X1.6:
    * Difference with previous version:
        * In this case the effect of data augmentation will be checked
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (400, 533, 3)
    * learning_rate=0.01
    * Drop Out: Tes
    * Image Augmentation: No
    * Final Accuracy: 0.66
 
*  X1.7:
    * Difference with previous version:
        * Data augmentation
        * 15 Epochs
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (400, 533, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: Yes
    * Final Accuracy: 0.69
 
*  X1.8:
    * Difference with previous version:
        * In this case the effect of data augmentation will be checked
        * 20 Epochs
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (400, 533, 3)
    * learning_rate=0.01
    * Drop Out: Yes
    * Image Augmentation: No
    * Final Accuracy: 0.67
 
*  X1.9:
    * Difference with previous version:
        * 20 Epochs
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (400, 533, 3)
    * learning_rate=0.01
    * Drop Out: Yes
    * Image Augmentation: No
    * Final Accuracy: 0.67
 
*  X1.10:
    * Difference with previous version:
        * 1.5 Use as base
        * Higher resolution used (800, 1066)
        * The training was not completed because of the time it took to complete it and limitations.
    * Base Model Trainable: False
    * Inner layer size: 100 neurons
    * Input shape: (800, 1066, 3)
    * learning_rate=0.01
    * Drop Out: Yes
    * Image Augmentation: No
    * Final Accuracy: 0.60
 
### X2.x Models
This model changes from X1 by adding and additional layer
The following attempts were made with this model:
* X2.1:
    * Base Model Trainable: False
    * Inner layer 1 size: 1000 neurons
    * Inner layer 2 size: 100 neurons
    * Normalization layers over the inners layers: No
    * Input shape: (400, 533, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.52
 
  * X2.2:
    * Differences with the previous version: Added Normalization Models
    * Base Model Trainable: False
    * Inner layer 1 size: 1000 neurons
    * Inner layer 2 size: 100 neurons
    * Normalization layers over the inners layers: Yes
    * Input shape: (400, 533, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.52

  * X2.3:
    * Differences with the previous model:
        * Higher learning rate (0.1)
        * Epoch increased to 20
    * Base Model Trainable: False
    * Inner layer 1 size: 1000 neurons
    * Inner layer 2 size: 100 neurons
    * Normalization layers over the inners layers: Yes
    * Input shape: (400, 533, 3)
    * learning_rate=0.1
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.48

### X3.x Models
This model changes from X2 by adding and additional layer, taking the total number of inner layers to 3
The following attempts were made with this model:
 * X3.1:
    * Base Model Trainable: False
    * Inner layer 1 size: 10000 neurons
    * Inner layer 2 size: 1000 neurons
    * Inner layer 3 size: 100 neurons
    * Normalization layers over the inners layers: Yes
    * Input shape: (400, 533, 3)
    * learning_rate=0.001
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.48

 * X3.2:
    * Difference with previous version:
        * The activations methods for each layer were tested: elu, sigmoid, tanh
        * epochs set to 10
    * Base Model Trainable: False
    * Inner layer 1 size: 10000 neurons
    * Inner layer 2 size: 1000 neurons
    * Inner layer 3 size: 100 neurons
    * Normalization layers over the inners layers: Yes
    * Input shape: (400, 533, 3)
    * learning_rate=0.001
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.65

### EN1.x Models
This model is based on EfficientNetV2L. The model had a higher Top-1 Accuracy than Xception and probably I could obtain a higher Accuracy. As the model was too heavy I was not able to complete the

 * EN1.1:
    * Base Model Trainable: False
    * Inner layer 1 size: 300 neurons
    * Normalization layers over the inners layers: No
    * Input shape: (400, 533, 3)
    * learning_rate=0.01
    * Drop Out: No
    * Image Augmentation: No
    * Final Accuracy: 0.62
 
  As this model results were not an improvement from Xception similar model, and as the training time for this model is too high, the model was discarded because of computation limitations at the moment

### Selected Model
The model 1.5 was selected for further work as is the simpliest one with higher accuracy

## Script for using the model
1. Clone this repository into your local machine
2. Install the needed dependencies with  ```!pip install keras-image-helper ``` ``` !pip install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime ```
3. Open your command shell
4. Go to the directory where the cloned repositore was stored
5. Open the folder "Separate Script"
6. Open the file tensorflow_model_cs1.py and change the "url" variable to set it to the URL of the image that you would like to test case save it
7. Run the file using ``` python tensorflow_model_cs1.py ```

## Containerized model for use with AWS Lambda
To work with the selected model, you can use the image prepared to be used with AWS Lambda. To test the image you shoudl follow the follwing steps:
1. Clone this repository into your local machine
2. Open your command shell
3. Go to the directory where the cloned repositore was stored
4. Open the folder "Serverles"
5. Be sure that Docker is working in your system and type ``` docker build -t scd:001 . ```
6. Once the build is ready, type  c docker run -p 8080:8080 scd:001 ```
7. Open another terminal on the folder "Serverles"
8. Now type ``` python test.py ```

You should be able to get the console run following this steps. You can open the file test.py with an editor and chage the URL in line 5 to test differente images

