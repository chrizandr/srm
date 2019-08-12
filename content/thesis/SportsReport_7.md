Title: Sport Analytics Report 7
Slug: sports-report-7
Category: Thesis
Date: 2019-08-05
Modified: 2019-08-05
Authors: Chris Andrew

### Detection baselines
Evaluated detection baselines using 4 new models
<!-- <img src='{filename}/images/detection-bline.png'> -->
<table class="table table-bordered table-hover">
  <thead>
    <tr>
    <b>
    <th>Architecture</th> <th>Base model</th> <th>Training data</th> <th>AP50</th> <th>AP75</th> <th>AP@[.5:.95]</th>
    </b>
    </tr>
  </thead>
  <tbody>
    <tr class='clickable-row' data-href='url://link-for-first-row/'> <td>Faster RCNN</td> <td>Resnet-101</td> <td>MS COCO</td> <td>0.632</td> <td>0.323</td> <td>0.45</td> <tr>
    <tr> <td>YOLOv3</td> <td>-</td> <td>MS COCO</td> <td>0.508</td> <td>0.157</td> <td>0.217</td> </tr>
    <tr> <td>SSD </td> <td>VGG16</td> <td>Pascal VOC 2007</td> <td>0.223</td> <td>0.092</td> <td>0.125 </td> </tr>
    <tr> <td>Faster RCNN</td> <td> VGG16</td> <td> Pascal VOC 2007</td> <td> 0.343</td> <td> 0.096</td> <td> 0.173 </td></tr>
    <tr> <td>Faster RCNN</td> <td>Resnet-101</td> <td>Pascal VOC 2007</td> <td>0.338</td> <td>0.081</td> <td>0.134 </td></tr>
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
