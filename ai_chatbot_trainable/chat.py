import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize, stem

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #use gpu if available

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = 'data.pth'
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device) #model
model.load_state_dict(model_state)
model.eval()

bot_name = 'Qezenfer'
print("Let's chat! (type 'quit' to exit)")
while True:
    sentence = input('You: ')
    if sentence == 'quit':
        break
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0]) #1 row, X.shape[0] columns
    X = torch.from_numpy(X).to(device) #convert to tensor

    output = model(X)
    _, predicted = torch.max(output, dim=1) #get the index of the max value
    tag = tags[predicted.item()] #get the tag 
    probs = torch.softmax(output, dim=1) #get the probability
    prob = probs[0][predicted.item()] #get the probability of the predicted tag
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")
    