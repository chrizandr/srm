Title: Sport Analytics Report 2
Slug: sports-report-2
Category: Thesis
Date: 2019-04-29
Modified: 2019-04-29
Authors: Chris Andrew

## Work done:
- Performed an analysis of how current object detection models perform on sports data(football)
- Evaluated on a small test dataset for player and ball detection
- Tried to identify the possible reasons as to why detection does not work for sports data.
- Listed out possible workarounds.

-------
### Current models for object detection
There are a number of models that are used for object detection. Each model has a different approach to the problem and has its pros and cons. A few well known models used for object detection are:

- R-CNN / Fast R-CNN / Faster R-CNN
- SSD (Single Shot Detectors)
- YOLO

Each model has a number of factors that can be compared. However we are interested in two important parameters for selecting the model: Speed and Accuracy.

Below is a graph showing the performance of each of the models:

**Speed and Accuracy**

<img src='{filename}/images/time.png' width="49%">
<img src='{filename}/images/acc.jpeg' width="49%">


For experimentation purposes, I selected YOLOv3 as the model for evalutation. This is because YOLO gives considerably high accuracy with speed. In case of R-CNN and its variants, the accuracy of detection is extremely high, but this comes at a high computational cost and the model can only process around 17fps, which is not real time as most videos are recorded at 30+fps. SSD and its variants on the other hand have high speed but low accuracy, this is because they use low resolution images to improve computational time but loose essential information in the process.

----
### Player Detection
I used a test dataset of 524 images extracted from the broadcast video of a football match. The frames were annotated with annotations for the players in each frame using bounding boxes.

I ran the YOLOv3 model on each frame and tried to detect players in the images, which is the 'person' label in the MS COCO dataset, since not specific label exists for players. Once the model produced detections, I used IoU(Intersection over Union) to measure the accuracy of the model in detecting the players.
A basic diagram of the testing framework is given below:

<img src='{filename}/images/flow.png' width="100%">

For each prediction made by the model, I find the nearest matching bounding box in the ground truth value and then calculate the IoU with this bounding box. If the IoU is above a specified threshold, the prediction is classified as valid, else it is invalid.

#### Results
I tried seeing how accuracy of predictions change with the IoU threshold.
<img src='{filename}/images/player.png' width="100%">

The results show that with an IoU threshold of around 0.6, we get above 60% accuracy in player detection. I found that the IoU value was low because the annotations done on the dataset had bounding boxes of the same size irrespective of the players pose, whereas the one predicted by the model varied in shape with the pose of the player, which is infact a better prediction.

I tried to categorize predictions as bad/good/great.

- Bad: Less than half of the annotated players are detected
- Good: More than half of the annotated players are detected
- Great: All of the annotated players are detected

The distribution of the predictions are as follows:

<img src='{filename}/images/chart.png' width="50%">

The majority of the predictions fall in the good/great category which seems to imply that the detection performance is exceptional just out of the box. There are still a large number of predictions that are unable to detect all the players in the image. A few reasons why predictions fall in the bad category are:

- Crowding (Lots of players huddled together)
- Distance (Player to far away from the camera to be properly visible)
- Blending with the crowd (Player is treated as part of the audience and one prediction is made)
- Occlusion (Player standing behind the net)

<img src='{filename}/images/player1.jpg' width="30%">
<img src='{filename}/images/player2.jpg' width="30%">
<img src='{filename}/images/player3.jpg' width="30%">

Majority of the predictions are actually very good, specially when a player is in the field and clearly visible.
<video width="320" height="240" controls>
  <source src="{filename}/videos/test.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

----
### Ball Detection
For Soccer ball detection I used a different dataset of 195 images, with the football annotated on each frame using a bounding box. In the MS COCO dataset, the 'sports ball' category is used to detect any type of sports ball including a football. Mutliple different types of sports balls are used to train the model, which also include the soccer ball.

For ball detection, I used the same framework as mentioned above for testing valid/invalid detections. Since there was only one ball in each frame, the predictions are classified as either valid/invalid as well. Below we vary the IoU and see the effects on prediction accuracy:

<img src='{filename}/images/ball.png' width="100%">

It is observed that ball accuracy is extremely low as compared to player accuracy, which is a surprising result since the ball remains relatively the same in each frames, whereas players change there pose/position frequently.

<img src='{filename}/images/detectionvsiou.png' width="100%">


Apart from this there were mutliple frames where no ball was detected, so the three categories are valid, invalid and no detection.
The distribution of the predictions are as follows:

<img src='{filename}/images/chart2.png' width="50%">

In frames where invalid predictions were made, most cases include classifying a players hand or foot as the ball.

<img src='{filename}/images/ball_1.png' width="30%">
<img src='{filename}/images/ball_2.png' width="30%">
<img src='{filename}/images/ball_3.png' width="30%">

Further investigation is needed on frames where no ball was detected as the reason for not being able to detect the ball remains unclear. It is possible that the model being trained on multiple sports balls would not be able to detect soccer balls very accurately since they usually tend to have designs and patterns on them that other sports balls lack.

-------
## Work to be done
- Come up with an effective strategy to improve the current performance of object detection models on football data, without specifically training on such data.
