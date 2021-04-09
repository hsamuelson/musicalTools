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


## Spectral
Simple spectrogram calculation and convolution with .wav files. <br>
### Requirements
````matplotlib```` <br>
````numpy```` <br>
````scipy```` <br>
````tkinter```` <br>
### Running
To run ````python convolve.py```` or ````python spectrogram.py````


## ThroatSinging
A PureData patch that uses analog microphone input to drive a synthesizer. Includes sine and filtered noise synths, as well as the option to output MIDI through your computer's driver (e.g. IAC Driver bus). Intended to be used with a contact mic attached to the throat, so that by humming you can control any MIDI synth in your DAW of choice. Be sure to enable MIDI output through your system MIDI driver from PD's preferences.<br>

### Requirements
````cyclone```` <br>
