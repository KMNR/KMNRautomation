from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('landing_page.html', page_name="Automation Home")

@app.route("/admin")
def admin():
    return render_template('landing_page.html', page_name="Automation Admin")


@app.route("/playlists")
def playlists():
    return render_template('playlists.html', page_name="Playlists")

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