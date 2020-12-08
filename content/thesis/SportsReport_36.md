Title: Sport Analytics Report 36
Slug: sports-report-36
Category: Thesis
Date: 2020-12-07
Modified: 2020-12-07
Authors: Chris Andrew

#### Updates
- Developed new clustering approach to do automatic labelling with few confident samples.
- Able to get 94% accurate labels over 50% of the data using 95 labelled samples.
- Model to be trained now on automatic generated samples.
- All experiments are being done on a new video

<img src='{filename}/images/clustering.png' width="80%">


#### Breakdown for France vs Belgium video.

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Stage</th>
      <th>Input</th>
      <th>Output</th>
      <th>Results</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
    <td>Initial detection (YOLOv3)</td>
    <td>95000 frames from video</td>
    <td>900k bounding boxes</td>
    <td>mAP - 0.73626</td>
    </tr>
    <tr class="header">
    <td>Multi-model clustering</td>
    <td>900k bounding boxes</td>
    <td>987 clusters</td>
    <td> - </td>
    </tr>
    <tr class="header">
    <td>Thresholding</td>
    <td>987 clusters</td>
    <td>95 clusters</td>
    <td> - </td>
    </tr>
    <tr class="header">
    <td>Representative sample</td>
    <td>95 clusters</td>
    <td>95 Representative samples</td>
    <td> - </td>
    </tr>
    <tr class="header">
    <td>Cluster labelling</td>
    <td>95 clusters</td>
    <td>500k labelled bboxes</td>
    <td> <b>mAP - 0.943 </b></td>
    </tr>
</table>

-------
### Work to be done.
- Train model on auto-annotated data and see performance
