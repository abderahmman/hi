from ast import Sub
from importlib.resources import path
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
import geocoder
import socket
import subprocess
import os

loc = geocoder.ip("me")
print(loc)

put_text("hello")
