Title: Sport Analytics Report 35
Slug: sports-report-35
Category: Thesis
Date: 2020-10-26
Modified: 2020-10-26
Authors: Chris Andrew

#### Updates
- Trained new model with GMMs for pruning False Positives
- Fixed error in annotations that caused wrong identification
- Recomputed anchors and retrained models based on fixed annotations
- Analysis on what cases where we still need to fix identification

#### Main types of False Positives.
<table width="500" border="0" cellpadding="5">
<tr>
<td align="center" valign="center">
<img src='{filename}/images/samples2.jpg'>
<br/>
Team managers and people on sidelines.
</td>
<td align="center" valign="center">
<img src='{filename}/images/samples3.jpg'>
<br/>
Camera crew and other support staff.
</td>
<td align="center" valign="center">
<img src='{filename}/images/samples5.jpg'>
<br/>
Transitioning BBoxes Errors
</td>
<td align="center" valign="center">
<img src='{filename}/images/samples1.jpg'>
<br/>
Referees.
</td>
<td align="center" valign="center">
<img src='{filename}/images/samples4.jpg'>
<br/>
Audience wearing team jersey.
</td>
</tr>
</table>


#### Results for France vs Croatia video.

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th rowspan="2">Model</th>
      <th rowspan="2">Training data</th>
      <th rowspan="2">Test data</th>
      <th colspan="3">Results</th>
      <th colspan="3">FP Pruning <br> (GMM + Kmeans)</th>
    </tr>
    <tr class="header">
      <th>Precision</th>
      <th>Recall</th>
      <th>mAP</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>mAP</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>9517 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.524</td>
    <td>0.932</td>
    <td>0.795</td>
    <td>0.555</td>
    <td>0.923</td>
    <td><b>0.837</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>19035 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.527</td>
    <td> 0.933</td>
    <td>0.796</td>
    <td>0.559</td>
    <td>0.925</td>
    <td><b>0.839</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>47587 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>0.524</td>
    <td>0.942</td>
    <td>0.817</td>
    <td>0.555 </td>
    <td>0.934 </td>
    <td><b>0.851</b></td>
    </tr>

    <tr class="header">
    <td>YOLOv3-pretrained</td>
    <td>95175 frames(France vs Croatia)</td>
    <td>95175 frames(France vs Croatia)</td>
    <td> 0.532</td>
    <td>0.939</td>
    <td>0.815</td>
    <td>0.566</td>
    <td>0.93</td>
    <td><b>0.849</b></td>
    </tr>

    </tbody>
</table>

-------
### Work to be done.
- Run tracking along with new models to get more reliable results.
