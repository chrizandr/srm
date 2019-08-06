Title: Sport Analytics Report 7
Slug: sports-report-7
Category: Thesis
Date: 2019-08-05
Modified: 2019-08-05
Authors: Chris Andrew

## Detection baselines
Evaluated detection baselines using 4 new models
<img src='{filename}/images/detection-bline.png'>

## Recognition
- Ran Mask RCNN on Vijay's football dataset and extracted segmentation masks.
- Tried to cluster segmentation masks together using HoG and simple descriptors and a BoW model.
- Could not find any similarities in clusters even after clustering.

-------
## Work to be done
- Integrate recognition using segmentation information.
- See how we can create a baseline for recognition.
