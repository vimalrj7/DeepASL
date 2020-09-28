# sign-language-cv
 A deep learning project developed using Keras and OpenCV.
 
## Goals
The aim of this project was to train a model to recognize on the Sign Language MNIST dataset and then test the model in a real world Computer Vision problem.

## Outcome
The model produces great results on the test data (99% accuracy, . However, this was to be expected as CNNs perform well on image classification. Moreover, the dataset was simple, and techniques such as data augmentation and a Dropout layer insured optimal performance.

When feeding the model images in real-time through a webcam, the results were not as successful. While the model correctly classified the letter in most cases, it was only after the hand was perfectly aligned or held at the perfect distance.

![](/images/H.png) ![](/images/Y.png) ![](/images/Y_incorrect.png)

*The first two pictures are correctly classified. However, the final picture was incorrectly classified due to my hand being at a different angle.*

## Next Steps
1. Increase the level of data augmentation
2. Build my own dataset to train on 
3. Implement a hand tracker in OpenCV
4. Read about other [image processing tricks](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html) to improve results. Warping may help the alignment issue, and a masking filter will be good for a new dataset.

## Installation and Usage
I would suggest Anaconda if you want to play around with this library. It makes it infinitely easier to use a GPU for training the model. To create a new environment and install the requrements, use the following command:
```
$ conda create --name <env> --file requirements.txt
```
With everything installed, you will be able to run the code with:
```
$ python cv.py
```

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 



 
