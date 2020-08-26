## Emotion detection using Image Processing.

## Media contents processing, analysis, extraction, synthesis and representation.

In order to process a media for instance a video to determine or classify emotions. There is need to extract frames from video which further needs to be annotated for usage in classification and detection tasks like object detection or emotion classification.

In next step we need to train a deep learning model in this case, ResNet architecture as it tackles the degradation problem which is commonly seen in deep networks, where the classifier accuracy gets saturated and it degrades rapidly.

For performance measure, confusion matrix can be taken in effect where the diagonal elements represent the number of images or frames for which the predicted label or target is equal to the true label or target, while off-diagonal elements are those that are incorrectly labelled by the classifier.

### Step 1: Convert a video into frames (given frame rate)

   ![How to install](/Images/t1.png)

### Step 2: We need a train.csv or a file that contains name of images generated from video along with annotated target emotion/label.

  An instance of Train.csv https://github.com/abhisheksaxena1998/Emotion-detection-from-video/blob/master/Train.csv is shown here. 

| Frame_ID               | 	Emotion   |
| ---------------------- | ---------- |
| frame0.jpg             | 	happy     |
| frame1.jpg             | 	happy     |
| frame2.jpg             | 	surprised |
| frame3.jpg             | 	surprised |
| frame4.jpg             | 	angry     |
| frame5.jpg             | 	surprised |
| frame6.jpg             | 	surprised |
| frame7.jpg             | 	surprised |
| frame8.jpg             | 	surprised |
| frame9.jpg             | 	angry     |
| frame10.jpg            | 	angry     |
| frame11.jpg            | 	Unknown   |
| frame12.jpg            | 	surprised |
| frame13.jpg            | 	surprised |
| frame14.jpg            | 	happy     |
| frame15.jpg            | 	angry     |
| frame16.jpg            | 	surprised |
| frame17.jpg            | 	happy     |
| frame18.jpg            | 	sad       |
| frame19.jpg            | 	sad       |
| frame20.jpg            | 	angry     |

### Step 3: Reorder images into a folder where happy folder contains images with label happy and angry with images angry and so on.

  ![How to install](/Images/t2.png)

### Step 4: Train the model.

  ![How to install](/Images/t4.png)


### Step 5: Read a test file and store results into it.

  Test.csv consists of frames that were to be annotated after training the model, we will give a label in each row through a trained model.
                
  Instance of https://github.com/abhisheksaxena1998/Emotion-detection-from-video/blob/master/Final%20annotated%20frames.csv is shown here.

| Frame_ID   | 	Emotion   |
| ---------- | ---------- |
| test0.jpg  | 	angry     |
| test1.jpg  | 	angry     |
| test2.jpg  | 	surprised |
| test3.jpg  | 	happy     |
| test4.jpg  | 	angry     |
| test5.jpg  | 	surprised |
| test6.jpg  | 	Unknown   |
| test7.jpg  | 	surprised |
| test8.jpg  | 	sad       |
| test9.jpg  | 	sad       |
| test10.jpg | 	sad       |
| test11.jpg | 	sad       |
| test12.jpg | 	surprised |
| test13.jpg | 	angry     |
| test14.jpg | 	surprised |
| test15.jpg | 	surprised |
| test16.jpg | 	surprised |
| test17.jpg | 	surprised |
| test18.jpg | 	surprised |



