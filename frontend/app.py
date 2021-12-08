#! /usr/bin/env python
from flask import Flask, render_template, redirect, request
from random import choice
import os
app = Flask(__name__)

@app.route("/")
def landing_page():
    funny_slider = ""
    logging_message = ""
    with open("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/frontend/static/slider_values.txt", "r") as f:
        options = f.readlines()
        funny_slider = choice(options)

    with open("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/backend/logging.txt", "r") as f:
        logging_status = f.read()
        if logging_status.strip() == "True":
            logging_message="Off"
        else:
            logging_message="On"

    # with open("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/backend/log.log", "r") as f:
    #     for line in f:
    #         pass
    #     songs = line.split("/")
    # current_song = songs[len(songs)-1]


    return render_template('landing_page.html', page_name="KMNR Ultimate Music Machine", slider=funny_slider, on_off=logging_message)

@app.route("/settings")
def settings():
    return render_template('settings.html', page_name="Settings")


@app.route("/playlists")
def playlists():
    playlists = sorted(os.listdir("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/media/playlists"))
    images = os.listdir("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/frontend/static/images")
    current_image = "../static/images/" + choice(images)
    return render_template('playlists.html', page_name="Playlists", playlists=playlists, image=current_image)

@app.route("/playlists/<playlist>")
def song_view(playlist):
    songs = []
    with open("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/media/playlists/"+playlist+"/playlist.txt", "r") as f:
        songs = [line.rstrip().split(",") for line in f.readlines()]
        for song in songs:
            if song[3] == "":
                song[3] = "-"
    print(songs)
    page_name = "Playlist Overview: " + playlist
    return render_template('playlist_view.html', page_name=page_name, pname = playlist, songs=songs)

@app.route("/songs")
def songs():
    return render_template('songs.html', page_name="Songs")

@app.route("/programming")
def programming():
    programs = os.listdir("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/media/programming")[1:]
    print(programs)
    return render_template('programming.html', page_name="Programming", list_of_programs=programs)

@app.route("/programming/<program>")
def program_view(program):
    program_content = os.listdir("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/media/programming/"+program)
    page_name = "Program Overview: " + program
    
    return render_template('program_view.html', page_name=page_name, pname = program, program_content=program_content)

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

@app.route("/toggle_logging", methods=['GET', 'POST'])
def toggle_logging():
    status = ""
    with open("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/backend/logging.txt" ,"r") as f:
        status = f.read()
    with open("C:/Users/weste/OneDrive/Documents/Class/CS4096/automation-rework-1/backend/logging.txt" ,"w") as f:
        if status == "True":
            f.write("False")
        else:
            f.write("True")
    return redirect(request.referrer), status

if __name__ == '__main__':
    app.run(debug=True)
