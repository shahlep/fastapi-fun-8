from fastapi import APIRouter
from fastapi import requests
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
router = APIRouter()
