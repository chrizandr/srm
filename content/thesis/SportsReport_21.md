Title: Sport Analytics Report 21
Slug: sports-report-21
Category: Thesis
Date: 2020-01-20
Modified: 2020-01-20
Authors: Chris Andrew

#### Work done
- Replicated unsupervised person re-identification paper. [[paper](https://arxiv.org/pdf/2001.01526.pdf)]
- Got results for re-identification on a benchmark re-id dataset. [[Market-1501](http://www.liangzheng.com.cn/Datasets.html)]
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
      <td>Market-1501</td>
      <td>71.2%</td>
      <td>87.7%</td>
      <td>94.9%</td>
      <td>96.9%</td>
    </tr>
  </tbody>
</table>

Found one possible dataset that can be used to evaluate, but data needs to be cleaned and pre-processed before we can use it.
[[dataset](http://home.ifi.uio.no/paalh/dataset/alfheim/)].
-------
### Work to be done.
- Try and get data for soccer.
- Finetune model on soccer data.
