# WTA Departures in CLI

Small Python program used to return upcoming bus departures given a stop ID.
I made this to teach myself more about Python. As such, this program is not intended to be practical. This program is intended for use only at WTA stops. It is not compatible with any other transit agency.

## Usage 

**WINDOWS**: **[Download][latest-release]** and run the pre-packaged .exe

**MACOS**: **[Download][latest-release]** the pre-packaged unix app, open a regular terminal window, drag the downloaded unix app into the terminal, and press enter.

**LINUX**: WIP. For now just run the python file with 'requests' installed (available in pip).

On start, the program will ask for a four-digit stop ID. This can be found either online at [ridewta.com](https://www.ridewta.com/) or in person on the bus stop sign.

### Stop ID Examples
- Bellingham Station - **2001**
- Cordata Station - **2000**
- Lincoln Creek - **9999**

If given a valid four-digit stop ID, the program will then print the current time, stop name, and the next 3 departures from said stop including route name, predicted minutes to arrival, and predicted arrival time. Arrival predictions are handled entirely by WTA's API.

### Example Output
```
Stop ID > 2052
URL IS: https://api.ridewta.com/stops/2052/predictions
 
THE TIME IS: 
07:59:15 AM
------------------------
Viking Union departures:

196 WWU/Lincoln
3 minutes
08:02:24 AM
 
190 Lincoln St
18 minutes
08:17:14 AM
 
14 Fairhaven via WWU
19 minutes
08:18:23 AM
```

## Building from source (How I did it)

Requirements:
- Python (Preferably latest, I wrote and packaged on 3.12.2) 
- pip 
- 'requests', available in pip
- 'pyinstaller', available in pip
- Source code (literally just WTAdepartures.py)

In terminal, navigate to the directory containing WTAdepartures.py and run the following command.
```
pyinstaller WTAdepartures.py --onefile
```
The packaged binary will be available in the newly created /dist.
Or you could just run the python file like a normal person.

**NOTE ON PYINSTALLER**: Pyinstaller can only package a binary for the OS and architechture it is running on. There is no way to get around this (to my knowledge).


## [API Reference Docs](https://data.ridewta.com/api/index.html)

[latest-release]: https://github.com/cyanisntblue/CLI-busdepartures/releases/latest