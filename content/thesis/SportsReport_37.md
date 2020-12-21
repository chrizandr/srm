Title: Sport Analytics Report 37
Slug: sports-report-37
Category: Thesis
Date: 2020-12-20
Modified: 2020-12-20
Authors: Chris Andrew

#### New training approach for model
- Better training method for YOLO, gets better accuracy for same amount of data.

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th rowspan="2">Model</th>
      <th rowspan="2">Trained Layers</th>
      <th rowspan="2">Training data</th>
      <th rowspan="2">Test data</th>
      <th colspan="3">Results</th>
      <th colspan="3">FP Pruning <br> (GMM + Kmeans)</th>
    </tr>
    <tr class="header">
      <th>Precision</th>
      <th>Recall</th>
      <th>mAP</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>mAP</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection layers</td>
    <td>9517 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.524</td>
    <td>0.932</td>
    <td>0.795</td>
    <td>0.555</td>
    <td>0.923</td>
    <td><b>0.837</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection+Upsampling layers</td>
    <td>9517 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td> 0.695</td>
    <td> 0.911</td>
    <td>0.852</td>
    <td>0.744</td>
    <td>0.931</td>
    <td><b>0.878</b></td>
    </tr>
    </tbody>
</table>

#### Semi-Supervised Annotation

- Developed new clustering approach to do automatic labelling with few manually labelled samples.
- Able to get 94% accurate labels over 50% of the data using 95 labelled samples.
<img src='{filename}/images/clustering.png' width="30%">

#### Problems
- BBoxes obtained after clustering are still YOLO generated ones, the co-ordinates of the BBox are accurate upto only 50% overlap, this makes training difficult when compared to GT.
- Might be possible to get better co-ordinates using confidence thresholding and using a segmentation model to suppliment information
-------
### Work to be done.
- Isolate better quality bounding boxes from the clustered ones and train only on those.
