# Uno
This is my first personal project. After I've completed the first step Docstring's formation, I decide to implement a Uno with Python to practice what I've learned.
In this readme i will explain you how it works, where are my difficulties and how can I improve this project in the futur.\n
Let's start our journey with how I've created a card.

### Card.py
Uno is a card game. To begin, I needed to create all cards in the game. 
* There are five colors [🟥, 🟨, 🟩, 🟦, ⬛]. 
* There are 15 values [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ⊝, ↺, +2, +4, ⊕].

We find colors into "Couleur.py" except black color.
We find values into "Valeurs.py" except joker's values.
During game, we could set a joker's color. For that, we can use setCouleur(couleur) on a card.
At a moment we wanted to know when a card is a joker. So we will is isJoker() a boolean methods that returns true or false if the card is a joker or no.
That's all for card.py

Now we're going to see how spade works.

### Pioche.py
The spade is constitute by 108 cards:
* 19 blue cards, numbered from 0 to 9 (2 for each number except for 0).
+ 19 red cards, numbered from 0 to 9 (2 for each number except for 0).
* 19 yellow cards, numbered from 0 to 9 (2 for each number except for 0).
+ 19 green cards, numbered from 0 to 9 (2 for each number except for 0).

* 8 “+2” cards, (2 for each color).
+ 8 “Reverse direction” cards, (2 for each color).
* 8 “Skip your turn” cards, (2 for each color).
+ 4 “SwitchColor” cards.
* 4 “+4” cards.
