Title: Sport Analytics Report 38
Slug: sports-report-38
Category: Thesis
Date: 2021-01-10
Modified: 2021-01-10
Authors: Chris Andrew

#### Work done
- Thresolding with confident samples gives better quality bounding boxes that model is able to learn from.
- Evaluated new training mechanism on different subsets of data.


Results of clustering approach for semi supervised learning (France vs Croatia)

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
    <td>95175 frames</td>
    <td> 0.739</td>
    <td> 0.863</td>
    <td>0.803</td>
    <td>0.723</td>
    <td>0.851</td>
    <td><b>0.824</b></td>
    </tr>
  </tbody>
</table>


Anlaysis of how training data changes accuracy (France vs Croatia)

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
    <td>Detection+Upsampling layers</td>
    <td>9517 frames</td>
    <td>95175 frames</td>
    <td> 0.695</td>
    <td> 0.911</td>
    <td>0.852</td>
    <td>0.744</td>
    <td>0.931</td>
    <td><b>0.878</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection+Upsampling layers</td>
    <td>19035 frames</td>
    <td>95175 frames</td>
    <td> 0.714</td>
    <td> 0.923</td>
    <td>0.862</td>
    <td>0.723</td>
    <td>0.929</td>
    <td><b>0.879</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection+Upsampling layers</td>
    <td>28552 frames</td>
    <td>95175 frames</td>
    <td> 0.734</td>
    <td> 0.911</td>
    <td>0.869</td>
    <td>0.723</td>
    <td>0.909</td>
    <td><b>0.889</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection+Upsampling layers</td>
    <td>38070 frames</td>
    <td>95175 frames</td>
    <td> 0.745</td>
    <td> 0.916</td>
    <td>0.872</td>
    <td>0.744</td>
    <td>0.914</td>
    <td><b>0.891</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>Detection+Upsampling layers</td>
    <td>47587 frames</td>
    <td>95175 frames</td>
    <td> 0.754</td>
    <td> 0.918</td>
    <td>0.875</td>
    <td>0.744</td>
    <td>0.905</td>
    <td><b>0.894</b></td>
    </tr>
  </tbody>
</table>


### Ways we might want to move forward:
- Use better re-identification models to get richer features.
- Use the semi-supervised trained model to again do detection and clustering to get better labels
- Get baselines for a second video
