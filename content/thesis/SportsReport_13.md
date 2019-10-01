Title: Sport Analytics Report 13
Slug: sports-report-13
Category: Thesis
Date: 2019-09-29
Modified: 2019-09-29
Authors: Chris Andrew

#### Results from finetuning experiment on YOLOv3
- Created a classifier to differentiate between players and other detections
<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Model</th>
      <th>YOLO training data</th>
      <th>Pruning model data</th>
      <th>Pruning model features</th>
      <th>Test data</th>
      <th>AP50</th>
      <th>AP75</th>
      <th>AP@[.5:.95]</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo">YOLOv3 + False positive pruning(SVM)</a></td>
      <td>MS Coco</td>
      <td>1300 set</td>
      <td>BoW SIFT features</td>
      <td>300 set</td>
      <td>0.8592</td>
      <td>0.5812</td>
      <td>0.5538</td>
    </tr>
  </tbody>
</table>
- Annotated one full 2 hour football match completely, still need to annotate 2 more matches.
- Created a classifier for classifying the view in a frame.
    - Used a BoW model with SIFT features and temporal smoothening to classify a given frame.
    - Predicts one of five views: [top zoomed-in, top zoomed-out, ground zoomed-in, ground zoomed-out, others]
    - Training: 1300 images set. Test: 400 images set.
    - Acheived 97.43% accuracy in classification for 5 views.
-------
### Work to be done
- Implement self-training paper, CVPR 2015 [paper](http://openaccess.thecvf.com/content_cvpr_2015/html/Misra_Watch_and_Learn_2015_CVPR_paper.html).
- Train separate models for different views.
- Complete annotations for other 2 videos.
