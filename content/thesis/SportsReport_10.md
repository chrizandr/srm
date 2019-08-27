Title: Sport Analytics Report 9
Slug: sports-report-9
Category: Thesis
Date: 2019-08-20
Modified: 2019-08-20
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
      <td><a href="http://preon.iiit.ac.in:8888/?model=res101_coco_img">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>MS COCO</td>
      <td>0.795</td>
      <td>0.519</td>
      <td>0.503</td>
    <tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=vgg16_pascal_img">Faster RCNN</a></td>
      <td> VGG16</td>
      <td> Pascal VOC 2007</td>
      <td>0.5987</td>
      <td>0.242</td>
      <td>0.285</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=res101_pascal_img">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>Pascal VOC 2007</td>
      <td>0.680</td>
      <td>0.377</td>
      <td>0.374</td>
    </tr>
  </tbody>
</table>

-------
### Work to be done
- Create test set of 1000 images
- Train model using 400 image data and test with 1000 test set
