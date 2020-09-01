Title: Sport Analytics Report 33
Slug: sports-report-33
Category: Thesis
Date: 2020-08-31
Modified: 2020-08-31
Authors: Chris Andrew

#### Updates
- Results for experiments with using subset of annotated data to train model

#### FP pruning results for France vs Croatia video.
<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Model</th>
      <th>Training data</th>
      <th>Test data</th>
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
    <td>0.14</td>
    <td>0.878</td>
    <td>0.682</td>
    </tr>
    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.184</td>
    <td>0.929</td>
    <td>0.801</td>
    </tr>
    <tr>
      <td colspan="2"><img src='{filename}/images/yolo_100_val_loss.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_100_val_acc.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_100_train_loss.png'></td>
    </tr>
    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>47587 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.183</td>
    <td>0.93</td>
    <td>0.801</td>
    </tr>
    <tr>
      <td colspan="2"><img src='{filename}/images/yolo_50_val_loss.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_50_val_acc.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_50_train_loss.png'></td>
    </tr>
    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>19035 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.182</td>
    <td>0.925</td>
    <td>0.786</td>
    </tr>
    <tr>
      <td colspan="2"><img src='{filename}/images/yolo_20_val_loss.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_20_val_acc.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_20_train_loss.png'></td>
    </tr>
    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>9517 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.182</td>
    <td>0.923</td>
    <td>0.785</td>
    </tr>
    <tr>
      <td colspan="2"><img src='{filename}/images/yolo_10_val_loss.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_10_val_acc.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_10_train_loss.png'></td>
    </tr>
    </tbody>
</table>

-------
### Work to be done.
- Still need to prune out False Positives while training
