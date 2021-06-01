from app.utils.const import UPLOAD_URL
import requests
from app.utils.db_functions import photo_db

async def upload_to_server(file):
    result = requests.post(url= UPLOAD_URL, files={"image":file})
    photo_url = result.json()
    img_id = photo_url["data"]["id"]
    img_url = photo_url["data"]["url"]
    img_size = str(photo_url["data"]["size"] / 1000) + "kb"
    await photo_db(img_id, img_url, img_size )

