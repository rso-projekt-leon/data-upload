from flask import Flask
import os
import datetime


def info_log(app, method_name, marker, message):
    service_name = app.config["SERVICE_NAME"]
    verison = app.config["VERSION"]
    env = os.getenv("FLASK_ENV")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log_string  = f'{{time: {time}, service_name:{service_name}, verison:{verison}, env:{env}, method:{method_name}, marker:{marker}, message:{message}}}'
    app.logger.info(log_string)
