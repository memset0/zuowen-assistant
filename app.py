import jieba
from flask import Flask, url_for
from os import path


def fenci(article):
    paras = list(filter(lambda x: x, map(lambda s: s.strip(), article.split('\n'))))
    words = list(map(lambda line: list(jieba.cut(line, cut_all=False)), paras))
    print(paras)
    return words

app = Flask(__name__)


@app.route('/')
def index():
    return url_for('.', filename='index.html')


if __name__ == '__main__':
    article = '''
    正如一天建不起罗马城一样，一项伟大事业的成就，往往有赖于那些点滴的努力和重复枯燥的工作。个人能力的培养亦是如此，不坐十年冷板凳，哪能有一技在身呢？
    耐心和积累，是实现理想的前提。只要认定了自己奋斗的目标，努力坚持下去，总会取得属于自己的一番成绩。毕淑敏曾说：“每一颗钻石在被发现前，都要经受埋藏尘埃的寂寞时光。”保持等侍与希望，总有一天，埋得再深的钻石，也会发光。
    '''
    print(fenci(article))
    # app.run()