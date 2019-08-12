Title: Sport Analytics Report 3
Slug: sports-report-3
Category: Thesis
Date: 2019-06-07
Modified: 2019-06-07
Authors: Chris Andrew

### Work done:
- Ran YOLOv3 on more diverse dataset
- Evaluated using MAP metrics
- Created dataset for evaluation
- Categorized results based on camera views
- Categorized results based on jersey color
- Read and started implementation of Rahul's paper for top view registration

-------
### Metrics
For the evaluation of the model I used Mean Average Precision (mAP) as a metric. Average precision computes the average precision value for recall value over 0 to 1. A mean of this over all images is called the mean average precision. We first classify predictions as True Positive or False Positive. This is done using the framework described below:


<img src='{filename}/images/flow.png' width="100%">

For each prediction made by the model, I find the nearest matching bounding box in the ground truth value and then calculate the IoU with this bounding box. If the IoU is above a specified threshold, the prediction is classified as valid, else it is invalid.
**AP50** is mAP with a threshold of 0.5, **AP75** is mAP with a threshold of 0.75, **AP@[0.5:0.95]** is mean of **AP50, AP55, AP60 ... AP95**.

Once all predictions have been classified as valid/invalid we find the mAP value for different categories:

- General performance of the model over the entire dataset.
- Performance of the model based on the camera views.
- Performance of the model based on the players jersey colors.
- A combination of the two above mentioned categories.

----------
### Dataset
For the purpose of this experiment I created a dataset of 400 images consisting of different camera views and different teams. Videos were mainly taken from 4 FIFA 2018 matches and annotated based on camera view, jersey color, and player positions.
A uniform distribution of all categories was taken in the test dataset to ensure that performance could be evaluated over a more diverse set of conditions.

We mainly considered 4 views, as mentioned in [paper](https://arxiv.org/pdf/1703.01437.pdf), they are:

- Top Zoomed In
- Top Zoomed Out
- Ground Zoomed In
- Ground Zoomed Out

Player jersey colors were also annotated and categorized as:

- Blue
- Red
- White
- Green
- Yellow

These seem to be the dominant colors as mentioned in this [study](https://www.kennisbanksportenbewegen.nl/?file=4310&m=1430485253&action=file.download).

<img src='{filename}/images/jersey-color.png'>

----------
### Results
For the detection task, I found AP50, AP75 and AP@[.5: .95] for all categories.

#### Results for the entire dataset:

<img src='{filename}/images/all-data.png' width="100%">

The average values of mAP for all classes of the MS COCO dataset for YOLOv3 are AP50 = 0.44, AP75 = 0.19 and AP@[.5:.95] = 0.33.

There is a significant drop in mAP@[.5:.95] as it is only 0.21 for player detection. AP50 values are better than the average value of the model and AP75 scores are lower than the average for the model. There is a significant loss of precision as the threshold for True positives is increased to 0.75, this seems to cause a large impact on AP@[.5:.95].

#### Results for different camera views:

<img src='{filename}/images/view-based.png' width="100%">

We observe that zoomed out views are better for detection than zoomed in views. Even though AP50 is relatively same for all four views, we see significant decrease in score for AP75 and AP@[.5:.95] for the zoomed in views as compared to the zoomed out views. Part of the reason why this would be the case is because in zoomed in views, the whole player is not usually visible.

#### Results for player jersey colors:

<img src='{filename}/images/color-based.png' width="100%">

There is not much disparity in detection scores based on jersey colors of the players, however some decrease in score can be seen when players wear green/yellow jerseys. This can be attributed to the fact that green/yellow matches the color profile of grass and thus it might be harder to perform detection. This still however is a small decrease.

#### Jersey color and camera view results:

** AP50 **

|          | top-in  |  top-out  | ground-in  | ground-out |
|----------|---------|-----------|------------|------------|
|  blue    | 0.562   | 0.555     | 0.526      | 0.525      |
|  red     | 0.566   | 0.53      | 0.512      | 0.505      |
|  white   | 0.566   | 0.53      | 0.531      | 0.514      |
|  green   | 0.457   | 0.467     | 0.468      | 0.487      |
|  yellow  | 0.457   | 0.467     | 0.468      | 0.487      |

** AP75 **

|        | top-in | top-out | ground-in | ground-out |
|--------|--------|---------|-----------|------------|
| blue   | 0.183  | 0.213   | 0.173     | 0.17       |
| red    | 0.176  | 0.188   | 0.169     | 0.159      |
| white  | 0.158  | 0.176   | 0.166     | 0.161      |
| green  | 0.109  | 0.127   | 0.125     | 0.138      |
| yellow | 0.109  | 0.127   | 0.125     | 0.138      |

** AP@[.5:.95] **

|        | top-in | top-out | ground-in | ground-out |
|--------|--------|---------|-----------|------------|
| blue   | 0.242  | 0.26    | 0.228     | 0.227      |
| red    | 0.24   | 0.241   | 0.221     | 0.216      |
| white  | 0.228  | 0.232   | 0.223     | 0.216      |
| green  | 0.184  | 0.197   | 0.192     | 0.207      |
| yellow | 0.184  | 0.197   | 0.192     | 0.207      |

We observe here that top-out scores are higher than all other views, but have a significant drop when green/yellow jerseys are worn. ground-in views on the other hand are higher than ground-out but there is a large drop again when green/yellow jerseys are used. We can thus say that top-out and ground-in views are better for detection and green/yellow jerseys are bad.

----
### Implementation of Rahul's paper
I have started implementation of Rahul's paper for top view registration of players. Right now I am implementing the MRF based optimisation to find the best match in the dictionary. I have already implemented nearest neighbour based matching using HoG and CNN based features. I will implement Chamfer matching after the MRF optimisation and then move on to creating the dictionary of homography and edge image pairs.

-------
### Work to be done
- Complete implementation of Rahul's paper
- Get the system working for multiple camera views/videos
- Evaluate results and see where method can be improved.
