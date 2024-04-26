import os
# from web3py_ext import extend
# from web3 import AsyncWeb3, AsyncHTTPProvider

from flask import Flask, render_template, request
from web3 import Web3
import json



def create_app(test_config=None):

    app = Flask(__name__)

    # # create and configure the app
    # app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template("test.html")
    

    @app.route('/test')
    def retrieve():
        klaytnBalance = "testing"
        balance = 0
        privateKey = "0xf0b695328ee59cec0bbf2f2efd309423c8e1cb427f82ac0ea3552d30c63f6f68"
        address = Web3.to_checksum_address("0x7cd2bb56142bf8ab104c8c1eddef9b1c32b04979")

        # w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider('https://public-en-baobab.klaytn.net', request_kwargs={'ssl':False}))
        w3 = Web3(Web3.HTTPProvider('https://public-en-baobab.klaytn.net'))

        try:
            result = w3.eth.get_balance(address)
            print(result)
            balance = result / 1000000000000000000
        except Exception as e:
            print(f"Error: {e}")

        return {"address":address, "balance": balance}

    @app.route('/test2')
    def fetch():
        # read database
        return {"1":30, "2": 40, "3":50, "4": 60, "5":70, "6": 80}


    return app