# batch-silence
### A batch silencer for mp4 files using ffmpeg

## ABOUT
This is a simple python script which will remove the audio track from any number of input mp4 files. 

## REQUIREMENTS
Python 3 must be installed.
A working build of FFMpeg must be placed in the same folder as silence.py, as should all input files, such that the directory structure is as follows:
    .
    +-- silence.py
	+-- ffmpeg
    |   +-- bin
    |   |   +-- ffmpeg.exe	
	+-- input1.mp4
	+-- input2.mp4
	...
	+-- inputN.mp4
	
The naming of input files is unimportant, so long as each is suffixed with '.mp4'.

## USAGE
Run the script either by double clicking silence.py (if you have a GUI file explorer handy) or using the following command:

    python silence.py
	
You will first be prompted with the number of input files detected and asked to confirm by typing 'Y' and pressing enter. This will begin the process of silencing all the input files.
Upon completion, the process will continue to run until you press enter with the terminal window focused. This is to ensure that you have a chance to look at the output of the script before the window closes if you ran the script by double clicking.
In the folder where you ran the script, you will now find a "file-silenced.mp4" for each "file.mp4" which was in the folder. The original files are not deleted.
	