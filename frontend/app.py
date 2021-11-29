from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('landing_page.html', page_name="KMNR Ultimate Music Machine")

@app.route("/admin")
def admin():
    return render_template('landing_page.html', page_name="Automation Admin")


@app.route("/playlists")
def playlists():
    playlists = sorted(os.listdir("/home/ryan/Documents/automation-rework/media/playlists"))    
    return render_template('playlists.html', page_name="Playlists", playlists=playlists)

@app.route("/playlists/<playlist>")
def song_view(playlist):
    songs = []
    with open("/home/ryan/Documents/automation-rework/media/playlists/"+playlist+"/playlist.config", "r") as f:
        songs = [line.rstrip() for line in f.readlines()]
    return render_template('playlist_view.html', page_name=playlist, songs=songs)


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

if __name__ == '__main__':
    app.run(debug=True)