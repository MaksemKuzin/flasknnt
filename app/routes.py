# -*- coding: utf-8 -*-
from app import app
import NN


@app.route('/')
@app.route('/index')
def index():
    return "Сейчас доступна только одна Нейросеть, это NNT2 Для доступа к ней перейдите в /nnt2"

@app.route('/nnt2')
@app.route('/NNT2')
def NNT2():
    return "Это вывод нейросети NNT2, главаня задача это НС в увеличение чисел на еденицу. Вы можете посмотреть копию исходного кода здесь -> https://colab.research.google.com/drive/17IXR1DfzEc1sQodG6W8EAu4QSbnQEkjh?usp=sharing  Результат работы НС  " + str(NN.NNT2())