from static import app, db
from flask import render_template, request, redirect, url_for, get_flashed_messages,flash
from static.entities import *
import locale
from static.forms import *

