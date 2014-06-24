To run:
1. have python 2.7 installed
2. open 2 command prompts/terminals
3. navigate to where the files are in both terminals
4. in one terminal type: python udptestrecieve.py
5. in the other terminal type: python udptest.py [number of frames you want to send] without the [], if you don't give a number then a default of 1 will be used, example: python udpbmpsend.py 60
6. the time taken to send the packets will be output to the terminal when udpbmpsend is run, and the number of packets received will be shown on the other terminal
7. no graceful exit has been implemented for bmpudprecieve, so to exit press ctrl+c, if you are on windows you may have to press ctrl+c and run udpbmpsend.py again
