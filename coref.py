import pickle

# load saved model
with open('allen_coref' , 'rb') as f:
    predictor = pickle.load(f)

text = "Joseph Robinette Biden Jr. is an American politician who is the 46th and\
current president of the United States. A member of the Democratic Party, \
he served as the 47th vice president from 2009 to 2017 under Barack Obama and\
represented Delaware in the United States Senate from 1973 to 2009."


prediction = predictor.predict(document=text)  # get prediction
print("Clsuters:-")
for cluster in prediction['clusters']:
    print(cluster)  # list of clusters (the indices of spaCy tokens)
# Result: [[[0, 3], [26, 26]], [[34, 34], [50, 50]]]
print('\n\n') #Newline

print('Coref resolved: ',predictor.coref_resolved(text))  # resolved text
# Result: Joseph Robinette Biden Jr. is an American politician who is the 46th and