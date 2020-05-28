from flask import Flask

app = Flask(__name__)

from tft_tier.app import views