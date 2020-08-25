Title: Sport Analytics Report 31
Slug: sports-report-31
Category: Thesis
Date: 2020-08-10
Modified: 2020-08-10
Authors: Chris Andrew

#### Updates
- Done with writing the method into the paper. [paper](https://www.overleaf.com/project/5eba27e1dc7e6e0001b090ce)
- Still trying to reproduce the results on other videos, have not been able to get similar results yet.
- Results obtained for France vs Croatia match:

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
    <td>Pre-trained model</td>
    <td>MS Coco</td>
    <td>-</td>
    <td>France vs Croatia - video</td>
    <td>mAP - 0.68 <br> F1 - 0.24</td>
    </tr>
    <tr class="header">
      <td>YOLOv3</td>
      <td>Transductive ZSL</td>
      <td>MS Coco</td>
      <td>France vs Croatia - video</td>
      <td>France vs Croatia - video</td>
      <td>mAP - 0.62 <br> F1 - 0.14</td>
    </tr>
  </tbody>
</table>

- Model seems to be learning more from false positives in the second video.

-------
### Work to be done.
- Try and find a way to remove false positives in real-time so model doesn't learn from them.
