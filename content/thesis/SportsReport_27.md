Title: Sport Analytics Report 27
Slug: sports-report-27
Category: Thesis
Date: 2020-06-09
Modified: 2020-06-09
Authors: Chris Andrew

#### Updates
- Modified model architecture to include instance level domain classifier.
- Got training results for modified YOLOv3 with image level domain adaptation.
- Unable to generalise model on multiple videos.
- Model tends to overfit on video which it is trained on.
- Need to finetune model for every video independently.
- New architecture should help reduce the problem.

<br>

<img src='{filename}/images/model.png' width="80%">

<br>
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
      <td>Image level domain adaptation</td>
      <td>MS Coco</td>
      <td>Belgium vs France - video</td>
      <td>Belgium vs France - video</td>
      <td>mAP - 0.883 <br> F1 - 0.708</td>
    </tr>
    <tr class="header">
      <td>YOLOv3</td>
      <td>Image level domain adaptation</td>
      <td>MS Coco</td>
      <td>Belgium vs France - video</td>
      <td>400 image test set</td>
      <td>mAP - 0.723 <br> F1 - 0.530</td>
    </tr>
  </tbody>
</table>


-------
### Work to be done.
- Complete model implementation and training.
- Add new results and method to paper draft.
