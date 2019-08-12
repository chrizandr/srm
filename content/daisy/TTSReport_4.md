Title: TTS Report 4
Slug: tts-report-4
Category: Daisy Project
Date: 2018-10-23
Modified: 2018-10-23
Authors: Chris Andrew

### Work done:
- Completed Training of Tacotron 2 model
- Finished testing of model.
- Hindi TTS data, possibilities
- Google TTS report

----

#### Model Trained
Tacotron 2 completed training for 120k iterations over 240 epochs. The validation loss is at 0.34 MSE loss. The training loss is also at a similar value. The model is able to generate audio for a given sentence in English.

![model]({filename}/images/r4_image2.png)

![model]({filename}/images/r4_image1.png)


#### Hindi TTS data:
IIT Madras has taken down their website to access the data. I have data on Telugu, but the data they have for other languages is no longer available to download. Need to get in touch with them to get the data.


#### Google TTS:
Google has no TTS services available for any Indian Languages. They only offer TTS for 11 languages, which are mostly European including Chinese and Korean.

----
### Work to be done:
- Finish developing Wavenet model for getting raw audio using spectrograms
- Start training the model for other Indian languages.
