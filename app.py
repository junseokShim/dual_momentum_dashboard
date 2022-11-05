from flask import Flask, request, render_template, redirect
from static.etf_parsing import stock_df
import os, sys

application = Flask( __name__ )


@application.route("/")
def main_page():
    qqq, spy = stock_df()
    return render_template('main.html', 
                            qqq = qqq,
                            spy = spy)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=4004, debug=True)