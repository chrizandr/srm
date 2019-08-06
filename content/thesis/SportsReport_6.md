Title: Sport Analytics Report 6
Slug: sports-report-6
Category: Thesis
Date: 2019-07-23
Modified: 2019-07-23
Authors: Chris Andrew


## Work done:
- Created compact report of last weeks progress
- Wrote code to generate synthetic data using Google Football environment
- Had discussion with Vijay about his work

-------
## Work from last week

|  |  |
| --- | --- |
| Fine tuned detection model on soccer data. | **Model**: YOLOv3 <br> **Data**: 1500 images, top-zoomed out view, players annotated. Test set of 400 images, different views, jersey colors, teams. <br> **Training**: Augmented images, trained for 300 epochs <br> **Result**: Drop in overall accuracy for test set, accuracy for top-zoomed out view almost doubled. <br> <a href="#results"> More... </a>|
| Started implementation of tracking | **Need**: Tracking needed to uniquely identify players positions to help estimate missing detections/registration when not in frame. <br> **Methods**: Explored Centroid based matching, Kalman Filters, Deep SORT tracking. <br> **Implemented**: Finished implementation of Deep SORT.|
|Google Football Environment.| **Need**: Lack of football data for tracking, use it to generate synthetic tracking and detection data. <br> **Finished**: Environment setup to generate data.|
| Discussions with Vijay | -Talked about his work on Person recognition and Face recognition <br> -Discussed about what I am currently doing. <br> -Took some suggestions from him about one possible direction to proceed. <br> <a href="#discussion"> More... </a>|

<b> <a href="{filename}/pdfs/report-1.pdf"> Compacted report of previous week </a> </b> <br>

--------
<a id="results"></a>
## Results for detection

### YOLOv3 (Before Finetuning)


| |AP50|AP75|AP@[.5:.95]|
|:--:|:--:|:--:|:--:|
| All        | 0.508 | 0.157 | 0.217       |
| top-in     | 0.568 | 0.156 | 0.23        |
| top-out    | 0.486 | 0.215 | 0.25        |
| ground-in  | 0.475 | 0.105 | 0.166       |
| ground-out | 0.501 | 0.152 | 0.22        |
| blue       | 0.525 | 0.17  | 0.227       |
| red        | 0.505 | 0.159 | 0.216       |
| white      | 0.514 | 0.161 | 0.216       |
| green      | 0.487 | 0.138 | 0.207       |
| yellow     | 0.487 | 0.138 | 0.207       |

### YOLOv3 (Finetuned on Top View data)

| | AP50  | AP75  | AP@[.5:.95] |
|:------------:|:-------:|:-------:|:-------------:|
| All        | 0.355 | 0.135 | 0.168       |
| top-in     | 0.118 | 0.026 | 0.051       |
| top-out    | 0.875 | 0.354 | 0.428       |
| ground-in  | 0.119 | 0.076 | 0.066       |
| ground-out | 0.31  | 0.085 | 0.129       |
| blue       | 0.347 | 0.146 | 0.172       |
| red        | 0.368 | 0.153 | 0.182       |
| white      | 0.352 | 0.141 | 0.172       |
| green      | 0.354 | 0.099 | 0.147       |
| yellow     | 0.354 | 0.099 | 0.147       |


<a id="discussion"></a>
## Discussion with Vijay
- Had a general discussion about the approaches he used in his work on Person Recognition. His use of poses to help improve recognition for person.
- Also had a discussion about his work on Face recognition, how he used similarities in a collection and used confident recognitions to propogate in similar frames.
- Mentioned about dataset on soccer images, mostly zoomed in views of players, 50k annotated with tracking.
- Talked about contextual information used in face recognition and how we may be able to use it in detection: confident detections are propogated to similar frames.
- Talked about the use of temporal information for improving detections.


Suggestions given by Vijay:
- Have a basic pipeline ready for detection along with tracking using pretrained models.
- Suggested that we can also use recognition models to help in detections/tracking.
- Improve on this pipeline using temporal/contextual information.
- Once we have confident detections and tracking, then we use the information to draw analytical inferences from the data.

-------
## Work to be done
- Plan next improvements to be made to pipeline
- Discuss about sequence modelling and tracking
