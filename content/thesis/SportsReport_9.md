Title: Sport Analytics Report 9
Slug: sports-report-9
Category: Thesis
Date: 2019-08-20
Modified: 2019-08-20
Authors: Chris Andrew

### Detection baselines
Added new visualisation tool and new model
Testing done on recognition set of 400 images
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
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo">YOLOv3</a></td>
      <td>-</td>
      <td>MS COCO</td>
      <td>0.491</td>
      <td>0.259</td>
      <td>0.268</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=ssd">SSD </a></td>
      <td>VGG16</td>
      <td>Pascal VOC 2007</td>
      <td>0.402</td>
      <td>0.21</td>
      <td>0.223 </td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=vgg16_pascal_img">Faster RCNN</a></td>
      <td> VGG16</td>
      <td> Pascal VOC 2007</td>
      <td>0.661</td>
      <td>0.317</td>
      <td>0.343</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=res101_pascal_img">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>Pascal VOC 2007</td>
      <td>0.680</td>
      <td>0.377</td>
      <td>0.374</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-vijay">Faster RCNN</a></td>
      <td>YOLOv3</td>
      <td>Vijay Recognition data</td>
      <td>0.062</td>
      <td>0.021</td>
      <td>0.028</td>
    </tr>
  </tbody>
</table>

-------
### Work to be done
- Create test set of 1000 images
- Train model using 400 image data and test with 1000 test set
