from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('landing_page.html', page_name="KMNR Ultimate Music Machine")

@app.route("/admin")
def admin():
    return render_template('landing_page.html', page_name="Automation Admin")

@app.route("/settings")
def settings():
    return render_template('settings.html', page_name="Settings")


@app.route("/playlists")
def playlists():
    return render_template('playlists.html', page_name="Playlists")

@app.route("/songs")
def songs():
    return render_template('songs.html', page_name="Songs")

@app.route("/programming")
def programming():
    return render_template('programming.html', page_name="Programming")

@app.route("/logging")
def logging():
    return render_template('logging.html', page_name="View Logs")


@app.route("/song_logs")
def songlogs():
    return render_template('logging_templates/song_logs.html', page_name="Song Logs")

@app.route("/error_logs")
def errorlogs():
    return render_template('logging_templates/error_logs.html', page_name="Error Logs")

@app.route("/playlist_logs")
def playlistlogs():
    return render_template('logging_templates/playlist_logs.html', page_name="Playlist Logs")

def toggleLogging():
    if os.getenv('LOGGING')=="False":
        os.environ['LOGGING']="True"
    else:
        os.environ['LOGGING']="False"

if __name__ == '__main__':
    app.run(debug=True)
