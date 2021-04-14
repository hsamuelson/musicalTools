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
````cyclone````

<br>
<br>

## Stereo Interpolator
A Pure Data patch that can take in a total of 10 audio files (5 per channel) and interpolates them using the x and y coordinates of the mouse. The interpolation is done simply through mixing volume of adjacent samples as they play and loop. The samples must be wave files. The x coordinate controls one channel and the y coordinate controls the other channel. 

Also controlled by the mouse is the resonance of a bandpass filter. The frequency value is based on the amplitude of the signal (an envelop). When the mouse is in the upper left corner (0 resonance), the filter does nothing, in the lower right corner, it completely warps the sound, and in between, it generates many crackles and pop as well as warping the sound. The x coordinate again controls one channel, and the y coordinate controls the other.

To start the sound files looping, start must be pressed, and stop can be pressed to end them. No audio will be heard at first, because the mouse position is not detected initially. "1" can be pressed for the mouse position to control which sound files play, and "2" can be pressed to control the resonance filters. The mouse will only control one at a time, and will keep the other setting constant until the other button is pressed.
