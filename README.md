# KMNR Ultimate Music Machine

The KMNR Ultimate Music Machine was created to replace the previous automation system for KMNR radio station's DJs and employees. This is because the old system was outdated, difficult to maintain, and hard to use. We created this system based off the previous one with an updated front and backend, plus a few new, useful features.

## Installation
#### Requirements

- Python 3.7+
- pip 21.1.2+
- mpv


### Linux

1. (Optional, but *highly* recommended) Instantiate a virtual environment for the python installation.
   1. Run ``pip install virtualenv``
   2. Run ``virtualenv venv``
   3. Run ``source venv/bin/activate``
   4. Verify you are in the virtual environment - ``(venv)`` should appear at the start of the command line. 
2. Install all necessary packages by running ``pip install -r requirements.txt`` in the same directory as requirements.txt.
3. Update the settings file in your preferred editor.
   1. Ensure the OpenWeatherMap API key ``owm_api_key`` is up-to-date.
   2. Ensure the news API key ``news_api_key`` is up-to-date.
4. Update the supervisord configuration file in your preferred editor.
   1. Update the route to automation on line 83.
      1. This should point to the directory containing ``main.py``.
   2. Update the route to the automation error log on line 85.  
      1. Make sure you have write permissions to this folder. 
   3. Update the route to the crash handler on line 88.
      1. This should point to the directory containing ``crash_handler.py``.
   4. Update the route to the crash handler logging file on line 93.
      1. Make sure you have write permissions to this folder.
   5. (Optional) Enable the web interface for supervisor
      1. Uncomment lines 39-42.
      2. Change the default username and password (or don't, it's your funeral)
      3. If enabling the web interface, it's highly recommended you update file permissions so that other users are unable to read this file.
         1. ``chmod 700 supervisord.conf``
      4. Update the IP address:port specifier.
   6. Launch the supervisor daemon with ``supervisord``.
   7. Open the supervisor control console with ``supervisorctl``.
      1. Your terminal should now have ``supervisorctl>`` at the bottom.
   8. Run ``status`` in the supervisor console to validate automation and notifier started correctly.
      1. Both processes should have the status ``RUNNING``. If automation has the status ``FATAL``, type ``exit`` to leave the supervisor console and check the automation error log.
      2. Once the script has been fixed, re-open the supervisor console and run ``start automation`` to relaunch automation.

At this point, automation has been successfully started!

## Starting the user interface
1. Ensure that the location listed in ``app.py`` is the correct location you would like to host the page at
2. Run the command  ``nohup python3 frontend/app.py &``
3. The frontend is now hosted at the address you specified in ``app.py``. Kill the process if necessary to turn off the frontend


## How to Use
Instructions in KMNR Automation Director red book in the KMNR drive

## Tech Stack
Python 3.9

Flask

Uptime Manager - Supervisord


## Contributions
To make contributions to this project,

## Credit
This project was created/updated by:

Ryan Kruger

Caleb Roth

Anne Marie Westervelt

Jennings Randolph

Morgen Nicodemus

Preston Dailey

For their CS 4096/4097 class credit
lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll./.
