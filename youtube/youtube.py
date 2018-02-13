from pytube import Playlist
from pytube import YouTube
import os
import logging

def download_playlist(url):
    pl = Playlist(url)
    pl.download_all()

def init_logger():
    logging.basicConfig(
        level=logging.DEBUG,
    )
    logger = logging.getLogger()
    return logger

def download_video(url):
    yt = YouTube(url)
    yt.streams.first().download()

if __name__ == '__main__':
    logger = init_logger()
    logger.info("Execution path is %s", os.getcwd())
    logger.info('Download begins')
    url = 'https://www.youtube.com/watch?v=HWHBCsUR-58'
    download_video(url)
    logger.info('Download finish ^_^')

