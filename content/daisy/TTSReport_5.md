Title: TTS Report 5
Slug: tts-report-5
Category: Daisy Project
Date: 2018-12-10
Modified: 2018-12-10
Authors: Chris Andrew

## Work done:
- Wrote module for creating Audio books in Telugu using MaryTTS
- Completed building Tacotron 2 model for English, including real time waveform generation.
- Generated Audio books for 5 English and 5 Telugu articles.
- Tried experimenting with different methods of waveform generation.
----

### Model Trained
Tacotron 2 completed training for 200k iterations over 400 epochs. The validation loss is at 0.34 MSE loss. The training loss is also at a similar value. The model is able to generate audio for a given sentence in English. Here are samples of various texts along with the audio generated using the Griffin-Lim estimator for reconstruction.

<audio controls>
  <source src="{filename}/data/test.wav" type="audio/mpeg">
</audio>


### Hindi TTS data:
IIT Madras has taken down their website to access the data. I have data on Telugu, but the data they have for other languages is no longer available to download. Need to get in touch with them to get the data.


### Google TTS:
Google has no TTS services available for any Indian Languages. They only offer TTS for 11 languages, which are mostly European including Chinese and Korean.

----
## Work to be done:
- Finish developing Wavenet model for getting raw audio using spectrograms
- Start training the model for other Indian languages.
