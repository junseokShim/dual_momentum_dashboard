from flask import Flask, request, render_template, redirect
from static.etf_parsing import stock_df, comb
import os, sys

application = Flask( __name__ )


@application.route("/")
def main_page():
    qqq, spy = stock_df()
    return render_template('main.html', 
                            qqq = qqq,
                            spy = spy)

@application.route("/comb")
def comb_chart():
    qqq, spy = stock_df()

    qqq_per = float(request.args['per1'])
    spy_per = float(request.args['per2'])

    comb_result = comb(qqq, spy, per1=qqq_per, per2=spy_per)
    return render_template('comb_chart_result.html',
                    comb_result = comb_result)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=4001, debug=True)