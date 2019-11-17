
from app import app
from flask import render_template, request, redirect, jsonify, make_response, Flask, url_for
import os
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET", "POST"])
def upload_image():
    feedback = ""
    if request.method == "POST":

        if request.files:
            image = request.files["image"]
            print(image)
            os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)
            image.save(os.path.join(app.instance_path, 'htmlfi', secure_filename(image.filename)))

            #Hier muss predicted werden

            feedback='Hier muss das Ergebnis hin'

    return render_template("public/upload_image.html", feedback=feedback)


