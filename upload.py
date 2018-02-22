from os.path import join, dirname
import dotenv 
from stravalib.client import Client

#get athlete
dotenv.load()
client = Client(dotenv.get("STRAVA_TOKEN"))



