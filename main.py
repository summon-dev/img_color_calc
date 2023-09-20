
import os
from werkzeug.utils import secure_filename
from flask import Flask, redirect, render_template, url_for, flash, request
from flask_bootstrap import Bootstrap
from ten_used_color import ten_color
from PIL import Image

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
SECRET_KEY = "SaeedMonfared"

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = SECRET_KEY

# chack if file name is correct and acceptable


def chaeck_file(filename):
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


@app.route("/", methods=['GET', 'POST'])
def home():
    filename = "img_holder.png"

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for("home"))
        file = request.files['file']
        print(file)
        # print(file)
        print(chaeck_file(file.filename))
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('Please Select a file')
            return redirect(request.url)
        if file and chaeck_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(r'static\img\uploads', filename))
            p_image = Image.open('static/img/uploads/' + filename)
            color_dict = ten_color(p_image)
            # print(color_dict)
            return render_template('index.html', file=filename, colors=color_dict)
        else:
            flash('Please chack the file and Try again')
            return redirect(request.url)

    return render_template("index.html", file=filename)


@app.route('/download_file')
def download_file():
    filename = request.args.get('name')
    return render_template("colors.html", file=filename)


if __name__ == "__main__":
    app.run(debug=True)
