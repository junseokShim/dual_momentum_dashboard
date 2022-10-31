from flask import Flask, request, render_template, redirect
import sys

application = Flask( __name__ )

@application.route("/") # html document를 response 하는 방법
def main_page():
    return render_template('main.html') # response hn path


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=3001, debug=True)