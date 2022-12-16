from flask import Flask, send_file, render_template
from disc import get_user_from_id
from PIL import Image
import requests
from io import BytesIO
import easy_pil
from easy_pil import Font
app = Flask(__name__)

def make_embed(user, member):
    background =easy_pil.Editor("back.png")
    profile = easy_pil.Editor("img.png").resize((75, 75)).circle_image()
    background.paste(profile, (10, 10))

    poppins = Font.poppins(size=50, variant="bold")
    poppins_small = Font.poppins(size=20, variant="regular")
    poppins_light = Font.poppins(size=20, variant="light")

    background.text((105, 20), f"Name: {user.display_name}", color="white", font=poppins_small)
    background.text((105, 60), f"Status: {member.status}", color="white", font=poppins_small)




    background.save(fp="ting.png")
@app.route("/<id>")
async def hello_world(id):
  
    user, member = get_user_from_id(id)    
    
    response = requests.get(user.avatar)
    img = Image.open(BytesIO(response.content))
    img.save("img.png")
    make_embed(user, member)
    


    return send_file("ting.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)