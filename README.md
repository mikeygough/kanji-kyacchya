# kanji-kyacchya
kanji-kyacchya is a pygame built to help japanese language learners better distinguish similar kanji.

one aspect that makes learning kanji so difficult is how similar they can be!

take, for instance, __存__ & __在__. they just barely differ and in this instance the two actually have the same meaning (exist).

in kanji-kyacchya, a goal kanji is presented to the user and they must catch that kanji while
avoiding the visually similar alternative (and the demons 👹).

to play kanji-kyacchya, clone this repo and install the requirements:

```pip3 install -r requirements.txt```

then, once inside the repo run the game with:

```python3 main.py```

kanji-kyacchya has two modes: easy & difficult!

to switch between easy and difficult mode simply uncomment the mode you prefer in the constants.py file.

### Demo:



### Reference:

#### virtual environments
Create a Python3 Virtual Environment: 
```python3 -m venv env```

Activate the Virtual Environment:
```source env/bin/activate```

Deactivate the Virtual Environment:
```deactivate```

To Remove a Virtual Environment:
```sudo em -rf venv```

#### requirements.txt
Automagically create a requirements.txt file:
```pip3 freeze > requirements.txt```
