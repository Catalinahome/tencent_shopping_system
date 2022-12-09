from flask import Flask
from flask import send_file
from flask import render_template
from mysql import mysql
from loguru import logger

# 第三方模块

app = Flask(__name__)


# 根路径页面
@app.route('/')
def home():
    db = mysql.DBConnector(logger=logger)
    sql = "select * from standard_drug_library where drug_unique_index = 'std_1238888' limit 3"
    data = db.execute_sql(sql, with_return=True)[0][0]
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002)

