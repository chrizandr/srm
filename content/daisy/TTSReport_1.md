Title: TTS Report 1
Slug: tts-report-1
Category: Daisy Project
Date: 2018-08-16
Modified: 2018-08-16
Authors: Chris Andrew

## Work done:
- Built a module to convert an annotated OCR text document into a Daisy Book using open source TTS systems. [Espeak]
- Read about the various types of TTS Models that are used and how they work.
- Read up on the various state of the art models that can be used to create TTS systems for native languages. [Detailed report at the end]
- Explored about the various options of TTS engines available for use. [MaryTTS]
-------

## Daisy Book Creation:
A Daisy Book consists of mainly three essential components that carry most of the content:
    - The text contained in .html files.
    - The audio contained in .mp3 files.
    - And a .smil file that links specific parts of the audio to specific parts of the text.

Apart from this a Daisy Book also contains an index file, called an NCC file[HTML], which is the main file that any Daisy player searches for in the audio book.

The code developed for the Daisy Book creation has been made modular in such a way that it would be extremely easy to incorporate a new TTS module into the existing system. A simple python function that takes two parameters, the text file and the output file needs to be created that takes the text from the text and outputs the audio in .wav format to the output file. This function must only be passed to the existing TTS Engine Class and everything else in the creation process would run automatically.

![model]({filename}/images/image1.png)

The system has been used to generate 10 audiobooks using Espeak, which are playable on Daisy Players. The books have been tried on Android Apps[Callos Player, Daisy Reader], Ubuntu[Daisy Duck]. However, not many apps support text based navigation and some do not display text at all, only the audio is heard. There may be a need to find/develop a better player for Daisy Books.

-----
## Types of TTS Models used:

TTS systems are mainly classified into hard disjoint sets based on the way they generate the text.

### Formant Synthesis:
These models are created to simulate the vocal tract to generate audio. A resonator is used to generate sounds which are then model based on formant frequencies to generate the desired audio.

### Concatenative synthesis
Concatenative synthesis generates speech by connecting natural, prerecorded speech units. These units can be words, syllables, half-syllables, phonemes, diphones or triphones.

### Articulatory synthesis:
Articulatory synthesis generates speech by direct modeling of the human articulator behavior. The articulatory control parameters include lip aperture, lip protrusion, tongue tip position, tongue tip height, tongue position and tongue height. These parameters are used to model audio.

### Unit selection synthesis:
In concatenative synthesis, units are modified by signal processing methods to produce the desired audio. This can make the speech sound unnatural. Unit selection synthesis (also, called corpus-based concatenative synthesis) solves this problem by storing multiple instances of each unit with varying parameters.


### Statistical Parametric Synthesis Techniques:
These models try and model the probability of a given speech signal for a given input text. These were the recent state of the art models before Deep Learning based models came into the picture. Examples include HMM to model each phoneme based on the text input.

----
## Deep Learning Based Speech Synthesis:
### Tacotron:
Tacotron is a Deep Learning based model that learns to estimate the Mel Spectrogram Representation of a given speech input. The model is trained in the following manner:

![tacotron]({filename}/images/image3.png)

Tacotron is not a true End to End Speech synthesis model in that it is never actually trained on the audio output. The model learns to estimate the audio signal Mel Spectrogram, which is a lossy transformation of the signal. The model also relies on the Griffin Lim algorithm to reconstruct the audio signal from the Mel Spectrogram. The algorithm iteratively estimates each frame, which is slow and also produces noise in the generated audio signal.

#### Pros:
- Character level modelling of the system.
- Generates close to human speech, under certain conditions.
- Deep Learning based framework.

#### Cons:
- Uses Mel Spectrograms, which are lossy.
- It is a sequence to sequence model, which require large training times.
- Relies on Griffin Lim algorithm, which has multiple iterations to estimate every frame.[Computationally heavy].

### Wavenet:
Wavenet is currently used by Google to generate the voice of Google Assistant. It is a Convolutional Neural Network that uses dilated convolutions to produce audio waveforms directly. Wavenet uses linguistic features extracted from the input text and uses that to model the audio waveform of the speech. Since it is directly conditioned to generate waveforms, Wavenet takes on the characteristic of the data on which it is trained.[Capture accent, breaths, pace, etc]. Wavenet audio is extremely human like and it is the current state of the art in human like speech.

#### Pros:
- CNN based architecture, fewer parameters than RNN based models.
- Catched nuances of speech, like pace, pauses, breath, etc.
- Extremely human like speech. Can also be used to create other waveforms.[Music]
#### Cons:
- Still not an end to end model as it relies on hand crafted linguistic features to generate audio, which requires heavy domain knowledge.
- Since it generates waveforms, it takes time to create audio[around 16k samples per second]. Output is hence not real time.


### Tacotron 2:
It is a combination of both Tacotron and Wavenet that are used to create a True End to End TTS system. It contains two networks that can be trained independently or in an End to End manner, although they employed independent training to speed up the training process and parallely train the two networks.

![tacotron2]({filename}/images/image2.png)

#### Pros:
- End to End model, which can be trained parallely for more efficiency.
- MOS higher than that of Human Voice.
- Can be tuned to generate various accents and voices by only retraining the modified wavenet.
#### Cons:
- Still relies on Mel Spectrograms as intermediate results.
Little slower than Wavenet in terms of performance.
- Can be optimized using other waveform generation methods
