# Nihon Kohden Neuropack S3 MEB-9600 Sanitizer
A small script to split the output file of the Nihon Codhen MEB-9600 into different files with each of the sweeps for data preprocessing and analysis.

========================= How to use it =========================

Demo: https://youtu.be/XIw2WCGoy1Q

You need Python installed on the machine (https://www.python.org/downloads/) <br>
Download the "<a href="https://github.com/Aloncifras/MEB-9600Sanitizer/blob/main/Sanitizer.py">Sanitizer.py</a>" script <br>
Drag the program to the folder with the Nihon Codhen MEB-9600 .TXT files. <br>
Double-click on the program

It will read all the .txt that are in the folder and look for each Nihon swipe in the file,
generating files in the format "OriginalFileName _n.bin" with n being the swipe number.<br>
generally the first is the average of all swipes performed in the collection, and if there is more than one screen
the next bin files will be for each screen in order from left to right.<br>

The program will also generate a file "FileName _merg.bin" which is the combination of the first two
Nihon screens for joint analysis if necessary.

And another file "FileName _sense.bin" which has a line saying the sensitivity of each screen.

===========================================================================

Extras:

Be careful. This program will rename any TXT file in the folder by replacing the dash "-" with an underscore "_."

===========================================================================
