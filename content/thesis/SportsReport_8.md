Title: Sport Analytics Report 8
Slug: sports-report-8
Category: Thesis
Date: 2019-08-13
Modified: 2019-08-13
Authors: Chris Andrew

### Detection baselines
Evaluated detection baselines using 4 new models
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
      <td><a href="{filename}/res/det_res101_coco.html">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>MS COCO</td>
      <td>0.55</td>
      <td>0.361</td>
      <td>0.351</td>
    <tr>
    <tr>
      <td><a href="{filename}/res/det_yolo_coco.html">YOLOv3</a></td>
      <td>-</td>
      <td>MS COCO</td>
      <td>0.483</td>
      <td>0.244</td>
      <td>0.259</td>
    </tr>
    <tr>
      <td><a href="{filename}/res/det_ssd_pascal.html">SSD </a></td>
      <td>VGG16</td>
      <td>Pascal VOC 2007</td>
      <td>0.402</td>
      <td>0.21</td>
      <td>0.223 </td>
    </tr>
    <tr>
      <td><a href="{filename}/res/det_vgg_pascal.html">Faster RCNN</a></td>
      <td> VGG16</td>
      <td> Pascal VOC 2007</td>
      <td>0.653</td>
      <td>0.267</td>
      <td>0.315</td>
    </tr>
    <tr>
      <td><a href="{filename}/res/det_res101_pascal.html">Faster RCNN</a></td>
      <td>Resnet-101</td>
      <td>Pascal VOC 2007</td>
      <td>0.612</td>
      <td>0.317</td>
      <td>0.321</td>
    </tr>
  </tbody>
</table>

### Finetuning detection models
- I tried finetuning of Faster RCNN on my dataset of 400 images, which I split as 300 for Training and 100 for Testing. The model started overfitting the training data after only 22 epochs.
- The main reason I think behind it overfitting is that the dataset is very small. I have started training the models instead on Vijays larger dataset of 50k images.

-------
### Work to be done
- Show results after finetuning the data.
- Plan for next steps
