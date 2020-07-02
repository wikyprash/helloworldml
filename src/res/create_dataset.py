from random import randint
from sklearn.linear_model import LinearRegression
import json


def create_dataset():
    TRAIN_SET_LIMIT = 1000
    TRAIN_SET_COUNT = 100

    TRAIN_INPUT = []
    TRAIN_OUTPUT = []
    x1 = []
    x2 = []
    x3 = []
    op = []
    for _ in range(TRAIN_SET_COUNT):
        a = randint(0, TRAIN_SET_LIMIT)
        b = randint(0, TRAIN_SET_LIMIT)
        c = randint(0, TRAIN_SET_LIMIT)
        o = a + (2*b) + (3*c)
        TRAIN_INPUT.append([a, b, c])
        TRAIN_OUTPUT.append(o)

        x1.append(a)
        x2.append(b)
        x3.append(c)
        op.append(o)

    for _ in range(len(TRAIN_INPUT)):
        d = {}
        d['x1'] = x1
        d['x2'] = x2
        d['x3'] = x3
        d['op'] = op

    with open('data.json', 'w') as f:
        json.dump(d, f, indent=2)
