from configparser import ConfigParser
from imgurpython import ImgurClient
import random

cfg = ConfigParser()
cfg.read('config.ini')

client = ImgurClient(cfg.get('imgur', 'client_id'), cfg.get('imgur', 'client_secret'))


def get_random_dank_meme():
	items = client.memes_subgallery('viral', random.randint(0, 3))
	return random.choice(items).link
