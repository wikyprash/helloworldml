import pickle

ip = [1, 2, 3]

with open('model.pkl','rb') as f:
    mdl = pickle.load(f)

def model(ip):
    return mdl.predict([ip])

print(model(ip))
