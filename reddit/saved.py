from pickle import UNICODE
from posixpath import splitext
import praw
import os
from dotenv import load_dotenv
import requests
from urllib.parse import urlparse
from yt_dlp import YoutubeDL


load_dotenv()

path = "downloads"




if not os.path.exists(path):
    os.makedirs(path)

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    redirect_uri=os.getenv('REDIRECT_URI'),
    user_agent=os.getenv('USER_AGENT'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)

user = reddit.redditor("chachink19")

for item in user.saved(limit=None):
    url = item.url
    print("Getting ", url, "...")

    customName = os.path.join(path, item.title) + ".mp4"
    ytdl_opts = {
        'outtmpl': customName
    }
    with YoutubeDL(ytdl_opts) as ydl:
        ydl.download(url)

    # data = requests.get(url).content


    # get extension from url
    # parsed = urlparse(url)
    # root, ext = splitext(parsed.path)

    # with open(os.path.join(path, item.title) + ext, 'wb') as handler:
    #     handler.write(data)


