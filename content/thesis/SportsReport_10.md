Title: Sport Analytics Report 10
Slug: sports-report-10
Category: Thesis
Date: 2019-08-27
Modified: 2019-08-27
Authors: Chris Andrew

### Detection baselines
Added results using new test set of 1000 images
Generated visualisation of results using new test set
<table class="table table-bordered table-hover">
  <thead>
    <tr>
      <th>Architecture</th>
      <th>Base model</th>
      <th>Training data</th>
      <th>AP50</th>
      <th>AP75</th>
      <th>AP@[.5:.95]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=res101_coco_new">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>MS COCO</td>
      <td>0.696</td>
      <td>0.367</td>
      <td>0.384</td>
    <tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=vgg16_pascal_new">Faster RCNN</a></td>
      <td> VGG16</td>
      <td> Pascal VOC 2007</td>
      <td>0.5987</td>
      <td>0.242</td>
      <td>0.285</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=res101_pascal_new">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>Pascal VOC 2007</td>
      <td>0.605</td>
      <td>0.311</td>
      <td>0.318</td>
    </tr>
  </tbody>
</table>

-------
### Work to be done
- Discuss plan for further
