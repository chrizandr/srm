Title: Sport Analytics Report 11
Slug: sports-report-11
Category: Thesis
Date: 2019-09-03
Modified: 2019-09-03
Authors: Chris Andrew

#### All results with new 1300 image test set.
<table class="table table-bordered table-hover">
  <thead>
    <tr>
      <th>Architecture</th>
      <th>Base model</th>
      <th>Training data</th>
      <th>Test data</th>
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
      <td>1300 Test set</td>
      <td>0.696</td>
      <td>0.367</td>
      <td>0.384</td>
    </tr>
    <tr style="border-bottom: 2px solid #808080;">
      <td><a href="http://preon.iiit.ac.in:8888/?model=res101_coco_img">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>MS COCO</td>
      <td>400 Test set</td>
      <td>0.7955</td>
      <td>0.5197</td>
      <td>0.5031</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=res101_pascal_new">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>Pascal VOC 2007</td>
      <td>1300 Test set</td>
      <td>0.605</td>
      <td>0.311</td>
      <td>0.318</td>
    </tr>
    <tr style="border-bottom: 2px solid #808080;">
      <td><a href="http://preon.iiit.ac.in:8888/?model=res101_pascal_img">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>Pascal VOC 2007</td>
      <td>400 Test set</td>
      <td>0.6806</td>
      <td>0.3773</td>
      <td>0.3740</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=vgg16_pascal_new">Faster RCNN</a></td>
      <td>VGG16</td>
      <td>Pascal VOC 2007</td>
      <td>1300 Test set</td>
      <td>0.5987</td>
      <td>0.242</td>
      <td>0.285</td>
    </tr>
    <tr style="border-bottom: 2px solid #808080;">
      <td><a href="http://preon.iiit.ac.in:8888/?model=vgg16_pascal_img">Faster RCNN</a></td>
      <td>VGG16</td>
      <td>Pascal VOC 2007</td>
      <td>400 Test set</td>
      <td>0.6615</td>
      <td>0.3171</td>
      <td>0.3431</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-new">YOLOv3</a></td>
      <td>-</td>
      <td>MS COCO</td>
      <td>1300 Test set</td>
      <td>0.5092</td>
    	<td>0.1698</td>
    	<td>0.2276</td>
    </tr>
    <tr style="border-bottom: 2px solid #808080;">
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo">YOLOv3</a></td>
      <td>-</td>
      <td>MS COCO</td>
      <td>400 Test set</td>
      <td>0.4911</td>
      <td>0.2595</td>
      <td>0.2681</td>
    </tr>
  </tbody>
</table>

#### Results from finetuning experiment on YOLOv3
<table class="table table-bordered table-hover">
  <thead>
    <tr>
      <th>Architecture</th>
      <th>Base model</th>
      <th>Training data</th>
      <th>Finetune data</th>
      <th>AP50</th>
      <th>AP75</th>
      <th>AP@[.5:.95]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-new">YOLOv3</a></td>
      <td>-</td>
      <td>MS COCO</td>
      <td>-</td>
      <td>0.5092</td>
      <td>0.1698</td>
      <td>0.2276</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-vijay">YOLOv3</a></td>
      <td>-</td>
      <td>MS COCO</td>
      <td>Vijay Soccer dataset</td>
      <td>0.0242</td>
      <td>0.0169</td>
      <td>0.0158</td>
    </tr>
    <tr>
      <td><a href="http://preon.iiit.ac.in:8888/?model=yolo-300">YOLOv3</a></td>
      <td>-</td>
      <td>MS COCO</td>
      <td>Old test set(300 images)</td>
      <td>0.3072</td>
      <td>0.0956</td>
      <td>0.1406</td>
    </tr>
  </tbody>
</table>
-------
### Work to be done
- Read papers and prepare for next direction(Detection/Analytics)
- Discuss about thesis problem.
