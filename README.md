# WTA Departures in CLI

Small Python program used to return upcoming bus departures given a stop ID.
I made this to teach myself more about Python. As such, this program is not intended to be practical.
This program is intended for use only at WTA stops. It is not compatible with any other transit agency.

## Usage 
If you for some reason would like to use this program, all you need is the WTAdepartures python file.
The only external dependency is the 'requests' library, available in pip.

On start, the program will ask for a four-digit stop ID. This can be found either online at ridewta.com or in person on the bus stop sign.

### Examples
- Bellingham Station - **2001**
- Cordata Station - **2000**
- Lincoln Creek - **9999**

If given a valid four-digit stop ID, the program will then print the current time, stop name, and the next 3 departures from said stop including route name, predicted minutes to arrival, and predicted arrival time. Arrival predictions are handled entirely by WTA's API.

## [API Reference Docs](https://data.ridewta.com/api/index.html)
