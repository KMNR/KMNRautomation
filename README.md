# KMNR Ultimate Music Machine
### Overview

The KMNR Ultimate Music Machine (KUMM) acts as a replacement for the old automation tool, SHTR. It implements features such as town and campus TTS, weather TTS, playlist tracking, and automatic logging to (KLAP? I totally forgot).

### Installation
#### Requirements

- Python 3.7+
- pip 21.1.2+
- mpv

#### Steps
1. (Optional, but *highly* recommended) Instantiate a virtual environment for the python installation.
   1. Run ``pip install virtualenv``
   2. Run ``virtualenv venv``
   3. Run ``source venv/bin/activate``
   4. Verify you are in the virtual environment - ``(venv)`` should appear at the start of the command line. 
2. Install all necessary packages by running ``pip install -r requirements.txt`` in the root directory.
3. Update the settings file in your preferred editor.
   1. Ensure the OpenWeatherMap API key ``owm_api_key`` is up to date.
   2. Ensure the news API key ``news_api_key`` is up to date.
4. Update the supervisord configuration file in your preferred editor.
   1. Update the route to automation on line 83.
      1. This should point to ``main.py``, wherever it's saved on the machine.
   2. Update the route to the crash handler on line 87.
      1. This should point to ``crash_handler.py``, wherever it's saved on the machine.
   3. Update the route to the crash handler logging file on line 92.
      1. Make sure you have write permissions to this folder.
   4. (Optional) Enable the web interface for supervisor
      1. Uncomment lines 39-42.
      2. Change the default username and password (or don't, it's your funeral)
      3. If enabling the web interface, it's highly recommended you update file permissions so that other users are unable to read this file.
         1. ``chmod 700 supervisord.conf``