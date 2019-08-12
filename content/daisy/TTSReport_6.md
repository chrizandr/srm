Title: TTS Report 6
Slug: tts-report-6
Category: Daisy Project
Date: 2019-01-14
Modified: 2019-01-14
Authors: Chris Andrew

### Work done:
- Drafted a set of possible questions we need to ask for people in the blind trust to be able to move forward
- Training for Telugu TTS model has plateaued, possibly need to increase the data for further training.
- Started reading papers published by Anurag on his work during for Sports Analytics
- Compiling a list of seminal papers in the area to get a basic understanding.
----

#### Model Training for Telugu TTS plateaued
- Tacotron 2 model has plateaued over validation loss for training Telugu data. A few possible reasons may exists as to why it has stopped learning, but the most likely cause is less data.
The data available from IITM was 24hours, but they were large recordings which could not be passed into the model. Out of 4200 recordings only around 3100 were usable from that data. The remaining content was not segmented properly. The usable files mount to around 10.5 hours of data and might not be enough for the model to be able to learn.

##### Training loss
![model]({filename}/images/train2.png)

##### Validation loss
![model]({filename}/images/val2.png)


Since the model was able to learn English with 23 hours of data, we might need more data for Telugu to be able to learn the model properly.

- Another possiblity is that we need better representations for the text for Telugu. For now, the characters in Telugu are transliterated into English and then converted into character sequences. This was done because it was recommended for other languages based on the models trained by Nvidia. It may be possible that we get better results if we avoid transliteration and directly encode character sequences in Telugu.

### Sports Analytics:
- Have started reading Anurag's work on Badminton and Tennis. Also trying to compile a list of seminal works in the are to get a basic understanding of the different problem that are there in teh field.
- Will report more on this in the next week.


-----
### Work to be done:
- Try and change text representations to get better training results for TTS.
- Complete reading and understanding the work done by Anurag.
- Survey the area of Sports Analytics to see some of the major works and get a basic understanding of the issues.
