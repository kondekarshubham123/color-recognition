## Welcome color-recognition repo

This model can only recognise the following colours
```
1. Red
2. Blue
3. Orange
4. Green
5. Yellow
6. Indigo
7. Voilet
```



### Problem Statement

```markdown
Interns are expected to create a TensorFlow model for identification of color. 
Your code will be given an image as an input and the code is supposed to categorize 
which RGB clour it matches to. This code is to be done in Python.
```

### Solution

For implemention of this project we need dataset.

So color dataset I have created using numpy and RGB color codes

#### Code for Dataset genrator is located in following directory
```markdown
    color-recognition/Dataset/DatasetGenerator/
```

#### Generation dataset and Model training

To Generate dataset type following command

`python Generate.py`

this ll generate dataset and stored in test dir which is **located in DataGenerator**.

Using generated dataset I have trained a keras-tf model which is located in `src/keras_model.h5`

`keras_model.h5` is the trained model by tensorflow.

### Use

```markdown
To use this model we need to put input image file on src folder

and in `code.py` give input of file name to `line no 17`

Run file


`python code.py`
```

### End

All done !!

Predicted output will be shown to you
