from flask import Flask , render_template ,request ,redirect, send_file
import numpy as np
from sqlalchemy import create_engine

#그래프를 이미지로 저장하기 위해 필요한 변환 라이브러리
from io import BytesIO , StringIO

app = Flask(__name__)

app.debug = True


@app.route('/', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("new_index.html", data="KIM")

if __name__ == '__main__':
  app.run()