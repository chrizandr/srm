Title: Sport Analytics Report 18
Slug: sports-report-19
Category: Thesis
Date: 2019-12-02
Modified: 2019-12-02
Authors: Chris Andrew

#### Synthetic data experiments
Models trained using synthetic data. Testing on real data.

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Architecture</th>
      <th>Training layers</th>
      <th>Training data</th>
      <th>Test data</th>
      <th>Test mAP</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td>YOLOv3 - 91 classes</td>
      <td>Detection Layers</td>
      <td>30k synthetic dataset</td>
      <td>400 image test set</td>
      <td>0.627</td>
    </tr>
    <tr>
      <td colspan="2"><img src='{filename}/images/yolo_synth_multi_val_loss.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_synth_multi_val_acc.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_synth_multi_train_loss.png'></td>
    </tr>
    <tr class="header">
      <td>YOLOv3 - 1 class</td>
      <td>Detection Layers</td>
      <td>30k synthetic dataset</td>
      <td>400 image test set</td>
      <td>0.647</td>
    </tr>
    <tr>
      <td colspan="2"><img src='{filename}/images/yolo_synth_mod_val_loss.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_synth_mod_val_acc.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_synth_mod_train_loss.png'></td>
    </tr>
  </tbody>
</table>


#### Jersey color based detections
Trained GMM based detectors to use color information from confident detections to detect additional players.

Methodology can be found [here]({filename}/images/colour_detection.png).

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Architecture</th>
      <th>Training data</th>
      <th>Test data</th>
      <th>mAP</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td>YOLOv3 + GMM based detector</td>
      <td>Confident detections from test set</td>
      <td>400 image test set</td>
      <td>0.869</td>
    </tr>
  </tbody>
</table>

#### Papers
- Read "Cats and Dogs" [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6248092)
- Read "The Truth About Cats and Dogs" [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6126398)

-------
### Work to be done.
- Finish with detection thread.
- Plan on next steps.
