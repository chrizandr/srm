Title: TTS Report 3
Slug: tts-report-3
Category: Daisy Project
Date: 2018-10-08
Modified: 2018-10-08
Authors: Chris Andrew

## Work done:
- Completed development of Mel-prediction model of Tacotron 2
- Retrieved English dataset for training of Tacotron 2, Female voice 23 hours.
- Started training of Tacotron 2 using English dataset.
- Generated one new audiobook using MaryTTS.
- Created a debugger to help annotators find mistakes in during the annotation part of the pipeline.

----

### Tacotron 2 mel prediction model:
Tacotron 2 consists of two models that can be independently trained: The Mel-prediction model which predicts the Mel-spectrogram of the audio given a sequence of characters as input, and a Wavenet model that converts the Mel-spectrograms to Audio.

![model]({filename}/images/r3_image1.png)

### LJ Speech Dataset:
- Single English female speaker.
- 23.6 hours of English audio from 7 different non-fiction books.
- 13,100 short audio clips (Around 15-20 words).
- Audio segmented automatically based on silences in the recording.
- Dataset is split into 12600 files for training and 500 for testing.
- Train set is split to 12500 for training and 100 for validation.

### Training:
The model has started training on the English dataset on Ada. Currently training is on 4 GPUs on a single node. The model has been set to train for 500 epochs with a checkpoint being saved after every 500 batches. Batch size is set to 48 files. Training and validation loss is decreasing as expected:

![model]({filename}/images/r3_image2.png)

### New Audiobook:
A new audiobook on Social Demography has been generated. Annotators gave me the annotated XML file, which I then corrected and generated an audiobook.

### New Debugging module for annotations:
There are a number of errors in the annotation process, even after repeated quality checking and asking annotators to check the work they do. To solve this problem, I made a module that can detect errors in the annotation done by the annotators. Have handed over the module to Vandanna and given instructions to use the module and asked her to forward the information to the annotators.

----

## Work to be done:
- Finish developing Wavenet model for getting raw audio using spectrograms
- Finish training of Tacotron prediction network and check output audio using Griffin-Lim algorithm.
- Finish integrating the debugging module to the annotation app.
- Finish integrating the audiobook generation into the annotation app.
