Title: Sport Analytics Report 40
Slug: sports-report-40
Category: Thesis
Date: 2021-03-08
Modified: 2021-03-08
Authors: Chris Andrew

#### Work done
- Reproduced detection method on third video.
- Started writing paper for detection work and dataset. [https://www.overleaf.com/1883171775tyfnmbckmwgc](https://www.overleaf.com/1883171775tyfnmbckmwgc)


Results of clustering approach for semi supervised learning for 3 videos (France vs Croatia), (France vs Belgium) and (England vs Croatia).

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
  <tbody>
    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>0.461</td>
    <td>0.872</td>
    <td>0.643</td>
    <td>0.571</td>
    <td>0.913</td>
    <td><b>0.714</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection+Upsampling layers</td>
    <td>105 bounding boxes(cluster centers) </td>
    <td>91732 frames (Eng vs Cr)</td>
    <td>0.763</td>
    <td>0.809</td>
    <td>0.786</td>
    <td>0.746</td>
    <td>0.971</td>
    <td><b>0.804</b></td>
    </tr>
  </tbody>
</table>


#### Work to be done
- One more video remaining.
- Finish and share initial version of draft by end of week.
