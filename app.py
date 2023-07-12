from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle


from chat import get_response
#  importing function from the chat.py file

# laoding models
df = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommendation(song_df):
    idx = df[df['song'] == song_df].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    songs = []
    for m_id in distances[1:11]:
        songs.append(df.iloc[m_id[0]].song)

    return songs





app= Flask(__name__)

@app.get("/")

def index_get():
      names = list(df['song'].values)
      return render_template("base.html",name = names)



@app.route('/recom',methods=['POST'])
def mysong():
    user_song = request.form['names']
    songs = recommendation(user_song)

    return render_template('base.html',songs=songs)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)



if __name__ == "__main__":
    app.run(debug=True)