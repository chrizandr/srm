Title: Sport Analytics Report 7
Slug: sports-report-7
Category: Thesis
Date: 2019-08-05
Modified: 2019-08-05
Authors: Chris Andrew

### Detection baselines
Evaluated detection baselines using 4 new models
<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
    <b>
    <th>Architecture</th> <th>Base model</th> <th>Training data</th> <th>AP50</th> <th>AP75</th> <th>AP@[.5:.95]
    </th>
    </b>
    </tr>
  </thead>
  <tbody>
    <tr class="header" class='clickable-row' data-href='url://link-for-first-row/'> <td>Faster RCNN</td> <td>Resnet-101</td> <td>MS COCO</td> <td>0.795</td>
    <td>0.519</td>
    <td>0.503</td></tr>
    <tr class="header"> <td>YOLOv3</td> <td>-</td> <td>MS COCO</td> <td>0.491</td>
    <td>0.259</td>
    <td>0.268</td> </tr>
    <tr class="header"> <td>SSD </td> <td>VGG16</td> <td>Pascal VOC 2007</td> <td>0.402</td> <td>0.21</td> <td>0.223 </td> </tr>
    <tr class="header"> <td>Faster RCNN</td> <td> VGG16</td> <td> Pascal VOC 2007</td> <td>0.661</td>
    <td>0.317</td>
    <td>0.343</td></tr>
    <tr class="header"> <td>Faster RCNN</td> <td>Resnet-101</td> <td>Pascal VOC 2007</td> <td>0.680</td>
    <td>0.377</td>
    <td>0.374</td></tr>
  </tbody>
</table>

### Recognition
- Ran Mask RCNN on my football dataset and extracted segmentation masks.
- Tried to cluster segmentation masks together using HoG and simple descriptors and a BoW model.
- Could not find any similarities in clusters even after clustering.

-------
### Work to be done
- Integrate recognition using segmentation information.
- See how we can create a baseline for recognition.
