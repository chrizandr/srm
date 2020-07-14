Title: Sport Analytics Report 29
Slug: sports-report-29
Category: Thesis
Date: 2020-07-13
Modified: 2020-07-13
Authors: Chris Andrew

#### Updates
- Ran Experiments on YOLOv3 with self training on soccer video, mixed with MS Coco data.
- Ran Experiments on YOLOv3 with self training on randomly samples images from multiple videos.
- Modified YOLOv3 architecture to detect one class, got better results with pre-training, was not getting good results with this previously, pre-training improved performance

<br>
<h3> Self training experiments </h3>
<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Model</th>
      <th>Method</th>
      <th>Source data</th>
      <th>Target data</th>
      <th>Test data</th>
      <th>Results</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td>YOLOv3</td>
      <td>Incremental domain adaptation</td>
      <td>MS Coco</td>
      <td>Belgium vs France - video</td>
      <td>Belgium vs France - video</td>
      <td>mAP - 0.857 <br> F1 - 0.673</td>
    </tr>
    <tr class="header">
      <td>YOLOv3</td>
      <td>Incremental domain adaptation</td>
      <td>MS Coco</td>
      <td>Belgium vs France - video</td>
      <td>400 image set</td>
      <td>mAP - 0.701 <br> F1 - 0.512</td>
    </tr>
    <tr class="header">
      <td>YOLOv3</td>
      <td>Incremental domain adaptation</td>
      <td>MS Coco</td>
      <td>Randomly sampled from 4 videos</td>
      <td>Belgium vs France - video</td>
      <td>mAP - 0.763 <br> F1 - 0.619</td>
    </tr>
    <tr class="header">
      <td>YOLOv3</td>
      <td>Incremental domain adaptation</td>
      <td>MS Coco</td>
      <td>Randomly sampled from 4 videos</td>
      <td>400 image set</td>
      <td>mAP - 0.794 <br> F1 - 0.632</td>
    </tr>
  </tbody>
</table>

<br>
<h3> Modified base detection model </h3>
<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Model</th>
      <th>Base Layer weight</th>
      <th>Detection layer weight</th>
      <th>Training detection layer</th>
      <th>Test data</th>
      <th>Results</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td>YOLOv3 - 1 class detection</td>
      <td>MS Coco - pretrained</td>
      <td>Randomly Initialised</td>
      <td>Randomly sampled soccer data</td>
      <td>400 image test set</td>
      <td>mAP - 0.701 <br> F1 - 0.618</td>
    </tr>
    <tr class="header">
      <td>YOLOv3 - 1 class detection</td>
      <td>MS Coco - pretrained</td>
      <td>MS Coco - pretrained</td>
      <td>Randomly sampled soccer data</td>
      <td>400 image test set</td>
      <td>mAP - 0.819 <br> F1 - 0.651</td>
    </tr>
  </tbody>
</table>

-------
### Work to be done.
- Perform self-training experiments with new base detection model.
