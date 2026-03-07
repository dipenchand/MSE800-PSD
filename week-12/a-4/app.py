import os
import logging
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return '''
    <h1>Hyperlink Example</h1>
    ''' + show_hyperlink() + '''
    <hr />
    <h1>File Upload Example</h1>
    ''' + upload_image()

def show_hyperlink():
    return "<a target='_blank' href='https://flask.palletsprojects.com/en/stable/quickstart/'>Flask Quickstart</a>"

def upload_image():
    if request.method == "POST":
        if not os.path.exists("uploads"):
            os.makedirs("uploads")

        file = request.files["image"]
        if file:
            file.save("uploads/" + file.filename)
            
            filename = file.filename
            return f"<a href='/view-image/{filename}'>View Uploaded Image</a>"
        
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="image">
            <input type="submit" value="Upload">
        </form>
        '''

@app.route("/uploads/<filename>")
def serve_upload(filename):
    return send_from_directory("uploads", filename)

@app.route("/view-image/<filename>")
def uploaded_file(filename):
    logging.info(f"Viewing image: {filename}")
    return f"<img src='/uploads/{filename}' />"

if __name__ == "__main__":
    app.run(debug=True)