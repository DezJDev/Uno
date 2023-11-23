# Uno
This is my first personal project. After I've completed the first step Docstring's formation, I decide to implement a Uno with Python to practice what I've learned.
In this readme i will explain you how it works, where are my difficulties and how can I improve this project in the futur.
Let's start our journey with how I've created a card.

  ### Card.py
Uno is a card game. To begin, I needed to create all cards in the game. 
* There are five colors [🟥, 🟨, 🟩, 🟦, ⬛]. 
* There are 15 values [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ⊝, ↺, +2, +4, ⊕].
* Each card has a value.

We find colors into "Couleur.py" except black color.
We find values into "Valeurs.py" except joker's values.
During game, we could set a joker's color. For that, we can use setCouleur(couleur) on a card.
At a moment we wanted to know when a card is a joker. So we will is isJoker() a boolean methods that returns true or false if the card is a joker or no.
That's all for card.py

*Now we're going to see how spade works.*

  ### Pioche.py
The spade is constitute by 108 cards, a discard pile and a current card.
* 19 blue cards, numbered from 0 to 9 (2 for each number except for 0).
- 19 red cards, numbered from 0 to 9 (2 for each number except for 0).
+ 19 yellow cards, numbered from 0 to 9 (2 for each number except for 0).
* 19 green cards, numbered from 0 to 9 (2 for each number except for 0).

- 8 "+2" cards, (2 for each color).
+ 8 "Reverse direction" cards, (2 for each color).
* 8 "Skip your turn" cards, (2 for each color).
- 4 "SwitchColor" cards.
+ 4 "+4" cards.

To implement the discard pile, we will use a FIFO structure.
To construct it, we draws in the spade while the drawed card isn't a joker. 
When a player plays a card, he puts it's card above the discard pile.
At a moment, the spade will be empty. So we reverse the discard pile to construct a new spade.
Now, when a player draws a card, he draws the first card played in the old discard pile.

The current card changes each time a card is play.
It tooks coulor and value of the last card play.
That's all for pioche.py
Now we're going to see how a player and a bot plays.

  ### MainJoueur.py & MainBots.py
At the beginning of the game, the player and each bot draws 7 cards.
With **Affichage.py** we show at player turn:
- Current Card
- Hand's player each card is indexed.
- A question that asks the player his moves for his turn.
An exemple of a display of a player's turn:

![playerview](https://github.com/DezJDev/Uno/assets/144434644/5a4abe55-2dd8-489c-adf4-13e5ac1c10d3)

He can decides to choose between 1 to N corresponding to his cards.
If he chooses a value outside this interval, that's return a message to the user and asks him again.
If he chooses a value that not correspond with the current card, that's return a message to the user and asks him again.
If he doesn't have any card corresponding with current card, he writes "p" to draw a card an pass his turn.

So we have two ways.
* The user plays a correct card. We apply the card's effect to the next bot. We add the card at the discard pile and change the current card with player's card value and color. We remove the card in his deck. We pass to the next bot's turn.
* The user draws a card. We take the card above the spade. We remove it from the spade. We add this card inside user's deck. We pass to the next bot's turn.

That's all for MainJoueur.py
Now we're going to see how a bot play.

With **Affichage.py** we show at each bot's turn:
- bot's name.
- bot's deck (card face hidden).
- bot's card played.
An exemple of a display of a player's turn:


![BotExemple1](https://github.com/DezJDev/Uno/assets/144434644/750ae950-d2b7-40fa-8208-c1a4782e6854)

In this exemple, we have 3 bots. Each turn, we see which card a bot played and how many cards still a bot have yet.
Each bot would play his card which have the most score and corresponding with the current card.
If any card doesn't correspond with the current card, the bot draws. 

That's all for MainBots.py
Now we're going to see how does the sense system work in the game.

### Fonctions.py
This file correspond of my functional work behind the appearance of the game.
The class called "Sens" implements the sense of the game.
We declare an array where we put our player & bots inside.
When a card that impacts the sense of the is played, we apply the methods corresponding of the card.

* __Exemple of the array :__ **[MainJoueur, MainBot("Bot n°1"), MainBot("Bot n°2"), MainBot("Bot n°3")]**
* __Retranscription:__ **[Player, Bot n°1, Bot n°2, Bot n°3]**
* __Number of cards by character :__ **[7, 7, 7, 7]**

Conventionally, it is asserted that the player is the one who plays the example cards.
It's the first character inside the array to play, after it's the second, then it's the third and finally it the fourth character to play.

| <p align="center">**Value of special card**</p>| <p align="center">**methods corresponding**</p>               |<p align="center">**resultat on the array**</p>                                     |
|:-----------------------------------------------|:--------------------------------------------------------------|:-----------------------------------------------------------------------------------|
|<p align="center">+2</p>                        |<p align="center">Sens.piochetonext(2) + Sens.finTour()</p>    |<p align="center">__Number of cards by character:__ [B2: 7, B3: 7, P: 7, B1: 9]</p> |
|<p align="center">+4</p>                        |<p align="center">Sens.piochetonext(4) + Carte.setCouleur()</p>|<p align="center">__Number of cards by character:__ [B2: 7, B3: 7, P: 7, B1: 11]</p>|
|<p align="center">↺</p>                         |<p align="center">Sens.reverse() + Sens.finTour()</p>          |<p align="center">__Exemple of the array:__ [Bot n°3, Bot n°2, Bot n°1, Player]</p> |
|<p align="center">⊝</p>                        |<p align="center">Sens.passerTour() + Sens.finTour()</p>       |<p align="center">__Exemple of the array:__ [Bot n°2, Bot n°3, Player, Bot n°1]</p> |
|<p align="center">⊕</p>                        |<p align="center">Carte.setCouleur() + Sens.finTour()</p>      |<p align="center">__Exemple of the array:__ [Bot n°1, Bot n°2, Bot n°3, Player]</p> |

```py
    while not iswinner:
        logging.debug(f"Voici le cursor: {sens.cursor}.")
        if type(sens.tableau[sens.cursor % (nb_bots + 1)]).__name__ == "MainJ":
            logging.debug(f"C'est au Joueur de jouer.")
            iswinner = sens.tableau[sens.cursor % (nb_bots + 1)].jouer(pioche, sens)
            if iswinner:
                aff_gagnant()
        else:
            logging.debug(f"C'est au Bot n°{sens.cursor % (nb_bots + 1)} de jouer.")
            logging.debug(f"Voici la taille du sens.tableau = {len(sens.tableau)}.")
            name = sens.tableau[sens.cursor % (nb_bots + 1)].name
            iswinner = sens.tableau[sens.cursor % (nb_bots + 1)].jouer(pioche, f"{sens.tableau[sens.cursor % (nb_bots + 1)].name}", sens)
            if iswinner:
                aff_perdant(name)
```
