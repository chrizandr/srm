Title: Sport Analytics Report 34
Slug: sports-report-34
Category: Thesis
Date: 2020-09-29
Modified: 2020-09-29
Authors: Chris Andrew

#### Updates
- Recomputed anchor points for YOLO to get better precision with model.
- Re-trained FP Pruning model using 10%, 20%, 50%, 100% of data


#### Results for France vs Croatia video.

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th rowspan="2">Model</th>
      <th rowspan="2">Training data</th>
      <th rowspan="2">Test data</th>
      <th colspan="3">Results</th>
      <th colspan="3">Modified <br> Anchors</th>
      <th colspan="3">FP Pruning</th>
    </tr>
    <tr class="header">
      <th>Precision</th>
      <th>Recall</th>
      <th>mAP</th>
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
    <td>95175 frames(France vs Croatia)</td>
    <td>0.14 </td>
    <td>0.878 </td>
    <td>0.682</td>
    <td>0.441 </td>
    <td>0.829 </td>
    <td>0.672</td>
    <td>0.602 </td>
    <td>0.858 </td>
    <td>0.763</td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>9517 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.182</td>
    <td>0.923</td>
    <td>0.785</td>
    <td>0.522</td>
    <td>0.9</td>
    <td>0.776</td>
    <td>0.552</td>
    <td>0.891</td>
    <td>0.817</td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>19035 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.182</td>
    <td>0.925</td>
    <td>0.786</td>
    <td>0.525</td>
    <td>0.9</td>
    <td>0.776</td>
    <td>0.555</td>
    <td>0.891</td>
    <td>0.818</td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>47587 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.183 </td>
    <td>0.93 </td>
    <td>0.801</td>
    <td>0.521 </td>
    <td>0.9 </td>
    <td>0.796</td>
    <td>0.552 </td>
    <td>0.900 </td>
    <td>0.828</td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.184 </td>
    <td>0.929 </td>
    <td>0.801</td>
    <td>0.53 </td>
    <td>0.9 </td>
    <td>0.795</td>
    <td>0.562 </td>
    <td>0.897 </td>
    <td>0.827</td>
    </tr>

    </tbody>
</table>

-------
### Work to be done.
- Run tracking along with new models to get more reliable results.
