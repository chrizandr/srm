Title: Sport Analytics Report 4
Slug: sports-report-4
Category: Thesis
Date: 2019-07-09
Modified: 2019-07-09
Authors: Chris Andrew


## Work done:
- Trained the detection model on soccer data.
- Evaluated results of newly trained model using diverse test set.
- Started implementation of tracking and registration.
- Implemented Deep SORT tracking algorithm.
- Setup Google Football environment for creating tracking data.
- Formulated Ideas for using Sequence modelling to improve detection.

-------
## Retraining detection model
I retrained the detection model (YOLOv3) using player detection dataset. The dataset contained shots from top zoomed out camera view. The dataset had 1500 images(80:20 validation split), which were further increased using data augmentation. The model was trained for 300 epochs before mAP plateaued.  

For testing the model, I evaluated on my own dataset of 400 images consisting of different views/teams/jersey colors. I evaluated the model with AP50, AP75 and AP@[.5:.95] metrics. Here are the results observed.

### Results for the entire dataset:

<img src='{filename}/images/all-data2.png' width="100%">

The average values of mAP for all classes of the MS COCO dataset for YOLOv3 are AP50 = 0.44, AP75 = 0.19 and AP@[.5:.95] = 0.33.

As compared to the previous results obtained before training on top-view, we observe a loss in general accuracy, this is because the model loses generality but improves its results for a specific view, top-out view in this case.

### Results for different camera views:

<img src='{filename}/images/view-based-before.png' width="100%">
<img src='{filename}/images/view-based-after.png' width="100%">

We see a large jump in top out view accuracy. This is a desirable result for us, since registration can use only top-out views to map players on the field map. We see accuracy almost double for AP50 and AP@[.5:.95], with a significant increase even in AP75.


----------
## Tracking and registration

### Tracking
I feel that there is a need to be individually identify players to be able to do better registration as well as improve detection results. The need for tracking is seen when we want to be able to estimate player positions when detection is unable to identify bounding boxes for a player even if the player is in the frame. We use information from the players previous position and velocity to be able to estimate his current position(bounding box). For this we need to be able to differentiate the bounding boxes for each player, which can be done only with tracking. For tracking I researched various methods that are commonly used for tracking:

- Centroid based matching
- Kalman filter based tracking
- Deep SORT tracking algorithm(State of the art)

I decided to use Deep SORT tracking for tracking player since it uses Deep features to be able to uniquely identify players across frames. Deep SORT can use features from YOLOv3 directly so there is no overhead in processing the deep features, therefore it can be coupled easily with the detector.

I have implemented Deep SORT into the implementation of YOLO I am using to be able to track players. However, it still needs to be evaluated on a sports dataset. There are is also no standard metric to measure the accuracy of tracking methods, so I also need to decide upon the metric that needs to be used.


### Registration
For Implementation of Rahul's paper on registration, I have finished implementing the matching methods to match edge maps. I am right now implementing the optimisation methods to select the best homography based on the match.

----
## Data for tracking
There is a lack of Football data for tracking. To overcome this, I decided to use Google Research Football Environment to genereate synthetic tracking and detection data. I will use this data to evaluate the tracking and detection model combined.

I have setup the environment on my laptop right now as there were some issues installing them on my desktop. I have written the code to generate data. I will use the tracking data for Sequence modelling to improve the detection accuracy.


----
## Sequence modelling
I think that Sequence to Sequence modelling can be used to improve both detection as well as top-view registration. The Sequence model can be used to estimate missing detections. The assumption is that at any given time there are a fixed number(finite) of players in the playing field. We can therefore individually model the movements of each player by finetuning a generic player movement model. This idea basically consists of three parts:

- A generic player movement model: This model learns to estimate missing detections given a series of detections with gaps in between. This will be a standard Sequence to Sequence model with an LSTM/GRU encoder-decode pair. We train this model to learn the relationship between the players past position and velocity to predict future values. This is modeled by sequence of bounding box coordinates(xyxy) given as input with missing detections in between given as a special token. The decoder output would be the correct sequence where the decoder replaces the tokens with the correct bounding box coordinates.

<img src='{filename}/images/seq2seq.png' width="50%">


- Fine tuning generic model: Once we have a generic model that has modeled player movements, we finetune this model for each player in the field in realtime. We use shots that are clearer to be train the model, with fewer misses in detection/tracking. Then use this model to estimate the tracking/detection results for shots that are not as clear.

- Using model for registration: Once a player is out of the camera frame, we do not really know the exact location of the player on the field. Therefore it becomes impossible for us to estimate the player position just from camera views. Movement models that have been finetuned on each players movements can then be used to estimate the movement of each player, when he/she is not present in the frame.

-------
## Work to be done
- Generate tracking data.
- Implement Sequence model to improve tracking.
- Complete registration using top view.
