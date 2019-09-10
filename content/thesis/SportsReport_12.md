Title: Sport Analytics Report 12
Slug: sports-report-12
Category: Thesis
Date: 2019-09-10
Modified: 2019-09-10
Authors: Chris Andrew

#### Results from finetuning experiment on YOLOv3

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Architecture</th>
      <th>Finetune data</th>
      <th>Test data</th>
      <th>Freeze backbone</th>
      <th>Multi scale training</th>
      <th>Augmentation</th>
      <th>AP50</th>
      <th>AP75</th>
      <th>AP@[.5:.95]</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-new">YOLOv3</a></td>
      <td>-</td>
      <td>1300 set</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>0.7504</td>
      <td>0.3939</td>
      <td>0.4158</td>
    </tr>
    <tr class="header">
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-300">YOLOv3</a></td>
      <td>300 set</td>
      <td>1300 set</td>
      <td>No</td>
      <td>No</td>
      <td>Yes</td>
      <td>0.3072</td>
      <td>0.0956</td>
      <td>0.1406</td>
    </tr>
    <tr>
      <td colspan="3"><img src='{filename}/images/yolo400_val_loss.png'></td>
      <td colspan="3"><img src='{filename}/images/yolo400_val_acc.png'></td>
      <td colspan="3"><img src='{filename}/images/yolo400_train_loss.png'></td>
    </tr>
    <tr class="header" style="border-bottom: 2px solid #808080;">
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-300-multi">YOLOv3</a></td>
      <td>300 set</td>
      <td>1300 set</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.5062</td>
      <td>0.1596</td>
      <td>0.2291</td>
    </tr>
    <tr>
      <td colspan="3"><img src='{filename}/images/yolo_300_multi_val_loss.png'></td>
      <td colspan="3"><img src='{filename}/images/yolo_300_multi_val_acc.png'></td>
      <td colspan="3"><img src='{filename}/images/yolo_300_multi_train_loss.png'></td>
    </tr>
    <tr class="header" style="border-bottom: 2px solid #808080;">
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-vijay">YOLOv3</a></td>
      <td>Vijay Soccer dataset</td>
      <td>1300 set</td>
      <td>No</td>
      <td>No</td>
      <td>Yes</td>
      <td>0.0242</td>
      <td>0.0169</td>
      <td>0.0158</td>
    </tr>
    <tr>
      <td colspan="3"><img src='{filename}/images/yolovijay_val_loss.png'></td>
      <td colspan="3"><img src='{filename}/images/yolovijay_val_acc.png'></td>
      <td colspan="3"><img src='{filename}/images/yolovijay_train_loss.png'></td>
    </tr>

    <tr class="header">
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo">YOLOv3</a></td>
      <td>-</td>
      <td>300 set</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>0.8151</td>
      <td>0.5693</td>
      <td>0.5364</td>
    </tr>
    <tr class="header" style="border-bottom: 2px solid #808080;">
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-1300-multi">YOLOv3</a></td>
      <td>1300 set</td>
      <td>300 set</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>0.3146</td>
      <td>0.0500</td>
      <td>0.1122</td>
    </tr>
    <tr>
      <td colspan="3"><img src='{filename}/images/yolo_1300_multi_val_loss.png'></td>
      <td colspan="3"><img src='{filename}/images/yolo_1300_multi_val_acc.png'></td>
      <td colspan="3"><img src='{filename}/images/yolo_1300_multi_train_loss.png'></td>
    </tr>

  </tbody>
</table>

-------
### Work to be done
- Discuss further plans for analytics/recognition
