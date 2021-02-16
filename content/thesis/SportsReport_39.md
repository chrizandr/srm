Title: Sport Analytics Report 39
Slug: sports-report-39
Category: Thesis
Date: 2021-02-15
Modified: 2021-02-15
Authors: Chris Andrew

#### Work done
- Reproduced detection method on second video. Got similar results as the first one. Method seems to be consistent
- Started preparing draft for detection work and dataset. Aiming for CVPR workshop.

Results of clustering approach for semi supervised learning for 2 videos (France vs Croatia) and (France vs Belgium)

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
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>0.441</td>
    <td>0.829</td>
    <td>0.672</td>
    <td>0.602</td>
    <td>0.858</td>
    <td><b>0.763</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection+Upsampling layers</td>
    <td>95 bounding boxes(cluster centers) </td>
    <td>95175 frames (Fr vs Cr)</td>
    <td> 0.739</td>
    <td> 0.863</td>
    <td>0.803</td>
    <td>0.723</td>
    <td>0.851</td>
    <td><b>0.824</b></td>
    </tr>
  </tbody>
  <tbody>
    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>0.435</td>
    <td>0.955</td>
    <td>0.623</td>
    <td>0.550</td>
    <td>0.897</td>
    <td><b>0.721</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection+Upsampling layers</td>
    <td>112 bounding boxes(cluster centers) </td>
    <td>95944 frames (Fr vs Be)</td>
    <td> 0.902</td>
    <td> 0.806</td>
    <td>0.813</td>
    <td>0.605</td>
    <td>0.969</td>
    <td><b>0.821</b></td>
    </tr>
  </tbody>
</table>


#### Work to be done
- Need to reproduce these results for remaining two videos - Croatia vs. England and Belgium vs. England
- Finish and share initial version of draft by end of week.
