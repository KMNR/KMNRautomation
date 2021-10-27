import os
from backend.constants import MEDIA_ROOT_DIRECTORY, PLAYLISTS_SUBDIRECTORY, IGNORED_FILE_EXTENSIONS
import random
import player

test = True


def playlist_handler():
    random.seed()
    if test:
        MEDIA_ROOT_DIRECTORY = "../media"
    playlist_to_play = random.choice(os.listdir(MEDIA_ROOT_DIRECTORY + PLAYLISTS_SUBDIRECTORY))
    playlist_path = MEDIA_ROOT_DIRECTORY + PLAYLISTS_SUBDIRECTORY + "/" + playlist_to_play
    songs = [x for x in os.listdir(playlist_path) if not x.endswith(IGNORED_FILE_EXTENSIONS)]
    if test:
        for song in songs:
            print(playlist_path + "/" + song)
    for song in songs:
        player.play(playlist_path + "/" + song)


if __name__ == "__main__":
    playlist_handler()
