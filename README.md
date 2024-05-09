# WTA Departures in CLI

Small Python program used to return upcoming bus departures given a stop ID.
I made this to teach myself more about Python. As such, this program is not intended to be practical.
This program is intended for use only at WTA stops. It is not compatible with any other transit agency.

## Usage 
If you for some reason would like to use this program, all you need is the WTAdepartures python file.
The only external dependency is the 'requests' library, available in pip.

On start, the program will ask for a four-digit stop ID. This can be found either online at ridewta.com or in person on the bus stop sign.

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

## [API Reference Docs](https://data.ridewta.com/api/index.html)
