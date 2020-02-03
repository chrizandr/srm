Title: Sport Analytics Report 22
Slug: sports-report-22
Category: Thesis
Date: 2020-02-03
Modified: 2020-02-03
Authors: Chris Andrew

#### Work done
- Extracted player identities and detection and tracking info from sensor data. [[dataset](http://home.ifi.uio.no/paalh/dataset/alfheim/)]
- Ran re-identitification model on new data

<table class="table table-bordered table-hover">
  <thead>
    <tr class="header">
      <th>Architecture</th>
      <th>Pre-train data</th>
      <th>Test data</th>
      <th>mAP</th>
      <th>CMC-Top 1</th>
      <th>CMC-Top 5</th>
      <th>CMC-Top 10</th>
    </tr>
  </thead>
  <tbody>
    <tr class="header">
      <td>MMT-Resnet50</td>
      <td>Duke-MTMC</td>
      <td>Soccer dataset(1 match)</td>
      <td>35.6%</td>
      <td>22.4%</td>
      <td>34.8%</td>
      <td>57.1%</td>
    </tr>
  </tbody>
</table>

- Need to find better data to test. Re-identitification does not work well for zoomed out images.

- Read an intersting paper that is trying to do something similar to us. [CVPR-2018](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w34/Theagarajan_Soccer_Who_Has_CVPR_2018_paper.pdf)

- Found a large scale dataset of match events that can be used to build our reasoning system. [dataset](https://figshare.com/collections/Soccer_match_event_dataset/4415000/2)

-------
### Work to be done.
- Look for or annotate better data.
- Try and improve results for re-identitification
