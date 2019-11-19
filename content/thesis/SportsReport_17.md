Title: Sport Analytics Report 17
Slug: sports-report-17
Category: Thesis
Date: 2019-11-18
Modified: 2019-11-18
Authors: Chris Andrew

#### Experiment
Two models are currently training using synthetic data. Current training results are shown below:

Models **still training**.

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Architecture</th>
      <th>Training layers</th>
      <th>Training data</th>
      <th>Training Loss</th>
      <th>Validation mAP</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td>YOLOv3 - 91 classes</td>
      <td>Detection Layers</td>
      <td>30k synthetic dataset</td>
      <td>0.255</td>
      <td>0.636</td>
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
      <td>0.189</td>
      <td>0.595</td>
    </tr>
    <tr>
      <td colspan="2"><img src='{filename}/images/yolo_synth_mod_val_loss.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_synth_mod_val_acc.png'></td>
      <td colspan="2"><img src='{filename}/images/yolo_synth_mod_train_loss.png'></td>
    </tr>
  </tbody>
</table>


#### Analysis
Main reasons behind low detection accuracy. Ranked in order of high to low frequency.

**No detections(False Negatives):**

- Blurred players. When players are running.
- Clumping of players into one object. Happens when players are to close to each other.
- Occlusion. Players behind goal post or other Players.
- Pose. Players lying on the ground or some other position(falling).
- Truncation. Players not completely in the frame.
- Scale. Players are far away and cannot be seen clearly in the frame.

**Wrong detections(False Positive):**

- Audience, refrees, other people are detected.
- Crowd treated as one detection.

#### Vijay's paper
- Read Vijays paper on using Visual phrases for Exemplar Face Detection.

-------
### Work to be done.
- Try using GRL layers on object detection models to improve detection.
