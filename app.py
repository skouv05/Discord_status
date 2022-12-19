from flask import Flask, send_file, render_template
from disc import get_user_from_id, run
import requests
from io import BytesIO
from PIL import Image
import easy_pil
from easy_pil import Font
app = Flask(__name__)
import os
import asyncio
import threading

def runner():
    asyncio.run(run())

t1 = threading.Thread(target=runner)
t1.start()



def make_embed(user, member, avar):
    background =easy_pil.Editor("back.png")
    if avar == "true":
        profile = easy_pil.Editor("img.png").resize((75, 75)).circle_image()
    else:
        profile = easy_pil.Editor("default2.png").resize((75, 75)).circle_image()
    background.paste(profile, (10, 10))

    poppins = Font.poppins(size=50, variant="bold")
    poppins_small = Font.poppins(size=20, variant="regular")
    poppins_light = Font.poppins(size=20, variant="light")

    background.text((105, 20), f"Name: {user.display_name}", color="white", font=poppins_small)
    background.text((105, 60), f"Status: {member.status}", color="white", font=poppins_small)




    background.save(fp="ting.png")
@app.route("/<id>")
def hello_world(id):
    if id == 1052919422068723752:
        return "You are not allowed to use this bot"
    
    user, member = get_user_from_id(id) 
    if user == None or member == None:
        return "User not found"   
    print(user, member)
    try:
        response = requests.get(user.avatar)
        img = Image.open(BytesIO(response.content))
        img.save("img.png")
        avar = "true"
    except:
        avar = "false"
    
    make_embed(user, member, avar)
    
    return send_file("ting.png", mimetype="image/png")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = os.environ.get("PORT")
    app.run(port=port, debug=True, host="0.0.0.0")