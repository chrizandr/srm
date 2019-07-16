Title: Sport Analytics Report 5
Slug: sports-report-5
Category: Thesis
Date: 2019-07-16
Modified: 2019-07-16
Authors: Chris Andrew


## Work done:
- Created compact report of last weeks progress
- Wrote code to generate synthetic data using Google Football environment


-------
## Work from last week

|  |  |
| --- | --- |
| Trained detection model on soccer data. | **Model**: YOLOv3 <br> **Data**: 1500 images, top-zoomed out view, players annotated. Test set of 400 images, different views, jersey colors, teams. <br> **Training**: Augmented images, trained for 300 epochs <br> **Result**: Drop in overall accuracy for test set, accuracy for top-zoomed out view almost doubled.|
| Started implementation of tracking | **Need**: Tracking needed to uniquely identify players positions to help estimate missing detections/registration when not in frame. <br> **Methods**: Explored Centroid based matching, Kalman Filters, Deep SORT tracking. <br> **Implemented**: Finished implementation of Deep SORT.|
| Player Registration | **Finished**: Matching methods to match edge maps. <br> **Unfinished**: Optimisation methods to select the best homography based on the match.|
|Google Football Environment.| **Need**: Lack of football data for tracking, use it to generate synthetic tracking and detection data. <br> **Finished**: Environment setup to generate data.|
|Formulated Ideas for using Sequence modelling to improve detection.| **Need**:  Can be used to estimate missing  detections. Can also be used for registration when player not in frame. <br> **Proposal**: Proposed a three phase pipeline for training and deployment of this model.|


<a href="{filename}/pdfs/report-1.pdf"> Full Report </a>

## Google Football environment
I have finished writing code to capture data for tracking and detection using the Google Football environment.
Bounding boxes are estimated. We have virtual players from top-zoomed out view on the field. Data of all players including those not in the field can be captured.

-------
## Work to be done
- Plan next improvements to be made to pipeline
- Discuss about sequence modelling and tracking
