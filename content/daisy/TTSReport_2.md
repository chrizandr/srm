Title: TTS Report 2
Slug: tts-report-2
Category: Daisy Project
Date: 2018-09-10
Modified: 2018-09-10
Authors: Chris Andrew

## Work done:
- Completed integration of MaryTTS into the Daisybook pipelin
- Completed addition of multiple TTS functionality for changing the TTS engine.
- Made methods for adding custom TTS engines by using abstract functions.
- Generated 10 audibooks using MaryTTS.
- Started annotation of 2 new books.
- Started development of Tacotron 2 model for regional languages.
- Acquired IIT Madras data for Telugu. Female 23.5 hours.

----

### Tacotron 2:
It is a combination of both Tacotron and Wavenet that are used to create a True End to End TTS system. It contains two networks that can be trained independently or in an End to End manner, although they employed independent training to speed up the training process and parallely train the two networks.

![model]({filename}/images/image2.png)

#### Pros:
- End to End model, which can be trained parallely for more efficiency.
- MOS higher than that of Human Voice.
- Can be tuned to generate various accents and voices by only retraining the modified wavenet.
#### Cons:
- Still relies on Mel Spectrograms as intermediate results.
- Little slower than Wavenet in terms of performance.

----

## Work to be done:
- Finish Developing Tacotron 2 for regional languages.
- Train model for Telugu data.
