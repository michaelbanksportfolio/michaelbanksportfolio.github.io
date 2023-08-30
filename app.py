from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure static file serving
app.static_folder = "static"

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.porkbun.com'  # Replace with your email provider's SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'michael.banks@michaelbanksportfolio.com'  # Replace with your email address
app.config['MAIL_PASSWORD'] = '234ABeuphonium11!'  # Replace with your email password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
@app.route("/project1", methods=["GET"])
def project1():
    if request.method == "GET":
        return render_template("project1.html")
    
@app.route("/project2", methods=["GET"])
def project2():
    if request.method == "GET":
        return render_template("project2.html")

@app.route("/project3", methods=["GET"])
def project3():
    if request.method == "GET":
        return render_template("project3.html")

@app.route("/project4", methods=["GET"])
def project4():
    if request.method == "GET":
        return render_template("project4.html")

@app.route("/project5", methods=["GET"])
def project5():
    if request.method == "GET":
        return render_template("project5.html")

@app.route("/project6", methods=["GET"])
def project6():
    if request.method == "GET":
        return render_template("project6.html")

@app.route("/project7", methods=["GET"])
def project7():
    if request.method == "GET":
        return render_template("project7.html")
    
@app.route("/resume", methods=["GET"])
def resume():
    if request.method == "GET":
        return render_template("resume.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        # Send email
        msg = Message(subject, sender="michael.banks@michaelbanksportfolio.com", recipients=['michael.banks@michaelbanksportfolio.com'])
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage: {message}"
        mail.send(msg)
        return "Email sent successfully!"
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
