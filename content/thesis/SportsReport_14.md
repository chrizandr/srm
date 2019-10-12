Title: Sport Analytics Report 14
Slug: sports-report-14
Category: Thesis
Date: 2019-10-12
Modified: 2019-10-12
Authors: Chris Andrew

#### Results from finetuning experiment on YOLOv3
- Improved classifier for shot classification
<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Model</th>
      <th>Training data</th>
      <th>Features</th>
      <th>Test data</th>
      <th>Accuracy</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td>SVM(linear kernel)</td>
      <td>3000 images</td>
      <td>BoW SIFT with temporal smoothening</td>
      <td>1000 image set</td>
      <td>99.63%</td>
    </tr>
  <tr>
      <td>SVM(linear kernel)</td>
      <td>300 image set</td>
      <td>BoW SIFT</td>
      <td>100 image set</td>
      <td>97.43%</td>
  </tr>
  </tbody>
</table>
- Read paper on self training, no reply from Ishan about the code.
- Started annotation of another match.
- Tried finetuning of YOLOv3 based on shots, no significant improvement seen. Accuracies plateau at 65%-70%.
- Two experiments currently running:
    - Self-learning approach to learn from only confident predictions, will update on any improvement.
    - Shot based YOLO models with modified architecture trained on only confident predictions.
-------
### Work to be done
- Implement self learning paper
- Complete experiments
