from flask import Flask, render_template ,request
import time
import smtplib
import os
app = Flask(__name__)

def mail(email, pssd, mssg):
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, pssd)
    server.sendmail(email, 'av2935288@gmail.com', mssg)

    server.quit()




@app.route('/')
def home_page():
    return render_template("index.html")


def cleanMsg(data):
    name= data.get('name')
    email= data.get('email')
    msg=data.get('message')
    message = f"""From: {name} <{email}>
Subject: New Message On Our Official Website
{msg}
"""
    return message

@app.route('/submit_form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form.to_dict()
        msg = cleanMsg(data)  # Assuming you have a function to clean the message
        password = os.environ.get('EMAIL_PASS')
        mail('9610testing@gmail.com', password, msg)  # Assuming you have a function to send email
        return render_template("index.html", message="Query sent successfully!")  # Assuming you have an index.html template
    else:
        return render_template("index.html", message="Something went wrong.")  # Assuming you have an index.html template

@app.errorhandler(404)  
def not_found(e): 
  return render_template("404.html") 

if __name__ == '__main__':
    app.run(debug=True)