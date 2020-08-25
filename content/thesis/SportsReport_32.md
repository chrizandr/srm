Title: Sport Analytics Report 32
Slug: sports-report-32
Category: Thesis
Date: 2020-08-24
Modified: 2020-08-24
Authors: Chris Andrew

#### Updates
- Analysed the main reasons for False Positives
- Worked on new unsupervised learning + re-indentification based false positive pruning method. Able to remove FP with 96% accuracy.
- FP Pruning results obtained for France vs Croatia match, best improvement becuase of pruning yet.


#### Main causes for False Positives in broadcast video.
<table width="500" border="0" cellpadding="5">
<tr>
<td align="center" valign="center">
<img src='{filename}/images/snap1.png'>
<br/>
Audience members in background.
</td>
<td align="center" valign="center">
<img src='{filename}/images/snap2.png'>
<br/>
Camera crew and other support staff.
</td>
<td align="center" valign="center">
<img src='{filename}/images/snap3.png'>
<br/>
Team managers and people on sidelines.
</td>
<td align="center" valign="center">
<img src='{filename}/images/snap4.png'>
<br/>
Referees.
</td>
</tr>
</table>


#### FP pruning results for France vs Croatia video.
<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Model</th>
      <th>Method</th>
      <th>Source data</th>
      <th>Test data</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>mAP</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
    <td>YOLOv3</td>
    <td>Pre-trained model</td>
    <td>MS Coco</td>
    <td>France vs Croatia - video</td>
    <td>0.14</td>
    <td>0.878</td>
    <td>0.682</td>
    </tr>
    <tr class="header">
    <td>YOLOv3</td>
    <td>Pre-trained + Unsupervised pruning</td>
    <td>MS Coco</td>
    <td>France vs Croatia - video</td>
    <td><b>0.602</b></td>
    <td>0.858</td>
    <td><b>0.763</b></td>
    </tr>
    </tbody>
</table>

-------
### Work to be done.
- Add new pruning method to papers
- Train transductive model with FP Pruning at every iteration
