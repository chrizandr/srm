Title: Sport Analytics Report 1
Slug: sports-report-1
Category: Thesis
Date: 2019-02-18
Modified: 2019-02-18
Authors: Chris Andrew

## Work done:
- Read papers on unsupervised methods used in Sports Analytics
- Read papers on some recent work in sports analytics and event detection
- Prepared a few ideas on directions which we can further investigate.

-------

## Different classes of problems tackled along with some papers relating to them.
------------
### Learning features in an unsupervised way that can help with certain problems that are supervised.

#### Deep unsupervised learning of visual similarities. [[paper](https://www.sciencedirect.com/science/article/pii/S0031320318300293)]
- Authors: Artsiom Sanakoyeu, Miguel A.Bautista, Björn Ommer
- Venue: Pattern Recognition, 2018
- Basic idea:
  - New Deep Learning methods have given better accuracy, but requires lot of data
  - There are extremely large number of visual classes for supervised tasks
  - Labelling of data is really hard for visual scenes, specially at large scale
  - Exemplar learning has been very successfull for unsupervised learning, but we can't train CNNs since large number of positive samples are required.
  - We automatically build "cliques" to overcome this problem so that we can train exemplar CNNs
  - They use simple features as similarity measures, then use an optimisation problem to get batches of similar points. These are then used to train an exemplar CNN. This CNN representation is used to get similar points to a given query point.
  - Pose estimation is used for evalutation, given a query pose, they find similar poses using the CNN features.
- Motivation: We can try and learn similar feature representations for key events in a sports match and try and classify them into various categories.

#### Congested scene classification via efficient unsupervised feature learning and density estimation. [[paper](https://www.sciencedirect.com/science/article/pii/S003132031630005X)]
- Authors: Yuan Yuan, Jia Wan, Qi Wang
- Venue: Pattern Recognition, 2016
- Basic idea:
  - Use spherical K-means to get feature mapping for a given image patch.
  - Use SVM to remove noisy centroids
  - For a given image, patches are extracted and then mapped using the feature mapping to get feature vectors. These are then coded into a single vector for the image using LLC coding.
  - This vector is used for scene classification as well as density estimation.
- Motivation: We can try using similar feature learning for finding ROIs in a given image frame.


#### Unsupervised Learning of Video Representations using LSTMs. [[paper](http://proceedings.mlr.press/v37/srivastava15.pdf)]
- Authors: Nitish Srivastava, Elman Mansimov, Ruslan Salakhutdinov
- Venue: ICML, 2015
- Basic idea:
  - Use an encoder LSTM to encode time series video into a fixed length representation.
  - Use multiple decoders to reconstruct the original frame/future frame from representation.
  - Use these representations for supervised tasks, such as action/event recognition.
- Motivation: We try and use encoder and decoder networks to find representations for different tasks in sports analytics.


------------

### Event Detection in sports both supervised and unsupervised

#### Unsupervised Action Discovery and Localization in Videos. [[paper](http://openaccess.thecvf.com/content_ICCV_2017/papers/Soomro_Unsupervised_Action_Discovery_ICCV_2017_paper.pdf)]
- Authors: Khurram Soomro, Mubarak Shah
- Venue: ICCV, 2017
- Basic idea:
  - Discover action classes using spectral clustering on unlabelled videos.
  - Find the action spatiotemporal annotation of the action in the video using optimisation.
  - Try and localize and classify the action in test videos.
- Motivation: Try and build an end to end method similar to this to solve event recognition in sports videos.


#### Deep Progressive Reinforcement Learning for Skeleton-based Action Recognition. [[paper](http://openaccess.thecvf.com/content_cvpr_2018/papers/Tang_Deep_Progressive_Reinforcement_CVPR_2018_paper.pdf)]
- Authors: Yansong Tang, Yi Tian, Jiwen Lu, Peiyang Li, Jie Zhou
- Venue: CVPR, 2018
- Basic idea:
  - Select important frames/event frames using Reinforcement Learning(FDNet)
  - From the selected frames, extract the Skeleton of the person as a graph
  - Use a graph based CNN to classify the skeleton as an action(GCNN)
- Motivation: Maybe try and use reinforcement learning models to find key events/frames in a video and then classify them for a specific sport.(Ex: In Football, labels would be foul, penalty, goal, etc.)

#### Event detection in soccer videos using unsupervised learning of Spatio-temporal features based on pooled spatial pyramid model. [[paper](https://link.springer.com/content/pdf/10.1007%2Fs11042-018-7083-1.pdf)]
- Authors: Babak Fakhar, Hamidreza Rashidy Kanan, Alireza Behrad
- Venue: Multimedia Tools and Applications
- Basic idea:
  - Complex algorithm that uses pyramid model to learn features for event detection.
  - Starts at frame level and then finds shots in an unsupervised manner.
  - Shots are classified into views by thresholding/clustering certain features.
  - Shots are also classified as replays by finding the speed of the shot(replays are played in slow motion)
  - Shots are also classified as highlights. Highlight begins with a long view shot and ends with a logo.
  - Dictionaries are learned for different views/replays/highlights. Replays and Highlights are categorized as key events in the video.
- Motivation: Try and build an architecture that uses a combination of methods to complete a certain task.
-------------

### Match Result Prediction to predict the outcome of the match.
Most work done in this field uses hand crafted features, work done includes for sports like Rugby, Football. Mostly variables other than those obtained from the match are used, for example: players health condition, previous scores, team average. Along with this live data from the match is used: successfull passes, ball possession, score attempts, etc.

A survey of works using neural networks is found here:

[A machine learning framework for sport result prediction](https://www.sciencedirect.com/science/article/pii/S2210832717301485), Applied Computing and Informatics, Rory P.Bunker, Fadi Thabtah.

-----

### Summary of possible problems that can be worked on
-  We can try and learn unsupervised feature representations for sports videos and try and use these features for different tasks.
- Try and use reinforcement learning models to find key events/frames in a video and then classify them for a specific sport.(Ex: In Football, labels would be foul, penalty, goal, etc.)
- Try and build an end to end unsupervised method to solve event recognition in sports videos
- Try and use encoder and decoder networks to find representations for different tasks in sports analytics.
- Try using unsupervised feature learning for finding ROIs in a given image frame.
- Try and build an architecture that uses a combination of methods to complete a certain task.
- Can we use other data apart from the video to find key events in the match, such as audience reactions(audio), this might be a new approach that hasn't been tried before.

-------
## Work to be done
- Finalise an area in Sports Analytics that we will tackle.
- Finalise the problem statement and begin researching about it.
- Read and understand previous approaches to the problem.
