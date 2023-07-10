# Chatbot Deployment with Flask and JavaScript


## Initial Setup:
Clone repo and create a virtual environment
```
$ git clone
$ cd Rythmix
```
Install dependencies
```
$ pip install Flask torch torchvision nltk
```
Install nltk package
```
$  python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$  python chat.py
```



# Rhythmix
