Title: Sport Analytics Report 23
Slug: sports-report-23
Category: Thesis
Date: 2020-03-02
Modified: 2020-03-02
Authors: Chris Andrew

#### Work done
- Completed automatic annotations for 3 entire matches using YOLOv3 with tracking and FP-pruning [Dataset part of work].
    - France vs Belgium - FIFA 2018 (Semi-final)
    - Brazil vs Belgium - FIFA 2018 (Quarter-final)
    - England vs Belgium - FIFA 2018 (Third place)


- Working on Incremental Domain adaptation to improve detection results. [Algorithm part of work]. [[paper](https://arxiv.org/abs/2001.04129)]

- Got results for Improved Faster RCNN using self-training. Performance still not better than YOLO. Did experiments to show comparison with YOLO.

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Model</th>
      <th>Pre-trained data</th>
      <th>Training data</th>
      <th>Test data</th>
      <th>mAP50</th>
      <th>mAP75</th>
      <th>mAP@[50:95]</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td>Faster RCNN</td>
      <td>MS Coco</td>
      <td>1300 labelled + 10k unlabelled</td>
      <td>400 image test set</td>
      <td>0.8123</td>
      <td>0.591</td>
      <td>0.556</td>
    </tr>
    <tr class="header">
      <td>Faster RCNN</td>
      <td>MS Coco</td>
      <td> - </td>
      <td>400 image test set</td>
      <td>0.7955</td>
      <td>0.5197</td>
      <td>0.5031</td>
    </tr>
    <tr class="header">
      <td>YOLOv3 + FP Pruning</td>
      <td>MS Coco</td>
      <td> - </td>
      <td>400 image test set</td>
      <td>0.8592</td>
      <td>0.5812</td>
      <td>0.5538</td>
    </tr>
  </tbody>
</table>


- Found broadcast recordings of Fox, BBC and ITV broadcasts of all FIFA 2018 matches.
  - Cannot find a legal source for download, not in India atleast.

-------
### Work to be done.
- Annotate two more videos using automatic methods.
- Improve detection algorithms for higher accuracy.
