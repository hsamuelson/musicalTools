# musicalTools
A Repo for electro-musical tooling

## Air-Conductor
Uses computer camera, to track motion and generate sounds given the total movement of frame. <br>
### Requirements
````opencv2```` <br>
````numpy```` <br>
````pygame```` <br>
### Running
To run ````python main.py````

<br>
<br>

## Spectral
Simple spectrogram calculation and convolution with .wav files. <br>
### Requirements
````matplotlib```` <br>
````numpy```` <br>
````scipy```` <br>
````tkinter```` <br>
### Running
To run ````python convolve.py```` or ````python spectrogram.py````

<br>
<br>

## ThroatSinging
A PureData patch that uses analog microphone input to drive a synthesizer. Includes sine and filtered noise synths, as well as the option to output MIDI through your computer's driver (e.g. IAC Driver bus). Intended to be used with a contact mic attached to the throat, so that by humming you can control any MIDI synth in your DAW of choice. Be sure to enable MIDI output through your system MIDI driver from PD's preferences.<br>

### Requirements
````cyclone```` <br>

## Stereo Interpolator
A Pure Data patch that can take in a total of 10 audio files (5 per channel) and interpolates them using the x and y coordinates of the mouse. The interpolation is done simply through mixing volume of adjacent samples as they play and loop. The samples must be wave files. The x coordinate controls one channel and the y coordinate controls the other channel. Pressing "1" starts mouse movement being processed, while pressing "2" will stop mouse movement from being processed. This can be used to make more abrupt, less smooth transitions by turning off reading the mouse movement, then moving it to a new spot and turning it back on. Also, the start and stop bang buttons turn on and off audio.
