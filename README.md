# Uno
This is my inaugural personal project. Following the completion of the initial step in learning Docstrings, I resolved to implement a Uno game using Python to apply and reinforce my newfound knowledge. In this README, I will elucidate the functioning of the application, highlight the challenges I encountered, and outline potential avenues for enhancing the project in the future. Let's embark on this journey by exploring how I crafted the card functionality.

  ### Card.py
Uno is a card game, and to commence, I had to generate all the cards for the game.
* There are five colors [🟥, 🟨, 🟩, 🟦, ⬛].
* There are 15 values [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ⊝, ↺, +2, +4, ⊕].
* Each card is assigned a value.


Colors are defined in **Couleur.py**, excluding the black color.
Values are defined in **Valeurs.py**, excluding the values for jokers.
During gameplay, it's possible to designate a color for a joker using the setCouleur(couleur) method on a card.
At some point, we needed to determine whether a card is a joker. For this purpose, we introduced the isJoker() method, a boolean function that returns true or false depending on whether the card is a joker or not.
That concludes the explanation for **card.py**.

Now, let's delve into how the spade functionality operates.

  ### Pioche.py
The deck consists of 108 cards, a discard pile, and a current card.


* 19 blue cards, numbered from 0 to 9 (2 for each number except for 0).
* 19 red cards, numbered from 0 to 9 (2 for each number except for 0).
* 19 yellow cards, numbered from 0 to 9 (2 for each number except for 0).
* 19 green cards, numbered from 0 to 9 (2 for each number except for 0).
* 8 "+2" cards (2 for each color).
* 8 "Reverse direction" cards (2 for each color).
* 8 "Skip your turn" cards (2 for each color).
* 4 "SwitchColor" cards.
* 4 "+4" cards.

To manage the discard pile, we employ a FIFO structure. To populate it, we draw from the deck until a non-joker card is drawn. When a player plays a card, they place it on top of the discard pile.
Eventually, the deck will be depleted. At that point, we reverse the discard pile to create a new deck. Consequently, when a player draws a card, they draw the top card from the old discard pile.
The current card changes each time a card is played, taking on the color and value of the last played card. That concludes the explanation for pioche.py.
Next, let's explore how a player and a bot engage in the game.

  ### MainJoueur.py & MainBots.py
At the start of the game, both the player and each bot draw 7 cards. 
Utilizing **Affichage.py**, we display the following during the player's turn:
* The current card
* The player's hand, with each card indexed
* A prompt requesting the player to input their moves for the turn.

Here's an example of the display during a player's turn:

![playerview](https://github.com/DezJDev/Uno/assets/144434644/5a4abe55-2dd8-489c-adf4-13e5ac1c10d3)

He can choose a value between 1 and N corresponding to his cards. If he selects a value outside this interval, a message is returned to the user, prompting him to try again. If he picks a value that doesn't match the current card, another message is displayed, instructing him to make a different selection. If he doesn't have any cards that correspond to the current card, he can type 'p' to draw a card and pass his turn.

So, there are two possible scenarios:

* The user plays a correct card. We apply the card's effect to the next bot, add the card to the discard pile, update the current card with the player's card value and color, remove the card from his deck, and proceed to the next bot's turn.
* The user draws a card. We take the top card from the deck, remove it from the deck, add it to the player's deck, and move on to the next bot's turn.
That concludes the explanation for **MainJoueur.py**

Now, let's explore how a bot plays.
Using **Affichage.py**, we display the following at each bot's turn:
* Bot's name.
* Bot's deck (with card faces hidden).
* Bot's played card.
  
__Here's an example of the display during a player's turn:__


![BotExemple1](https://github.com/DezJDev/Uno/assets/144434644/750ae950-d2b7-40fa-8208-c1a4782e6854)

In this example, we have three bots. Each turn, we observe which card a bot plays and how many cards the bot still has.
Each bot is programmed to play the card with the highest score that corresponds to the current card. If none of the bot's cards match the current card, the bot draws a card.
That concludes the explanation for **MainBots.py**
Now, let's explore how the turn system works in the game.

### Fonctions.py
This file corresponds to the functional aspects behind the game's interface. The class called "Sens" manages the turn order in the game.
We declare an array where we place our player and bots. When a card that impacts the turn order is played, we apply the corresponding methods.

* Example of the array: [MainJoueur, MainBot("Bot n°1"), MainBot("Bot n°2"), MainBot("Bot n°3")]
* Representation: [Player, Bot n°1, Bot n°2, Bot n°3]
* Number of cards for each character: [7, 7, 7, 7]

Conventionally, it is asserted that the player is the one who plays the example cards. The player is the first character in the array to play, followed by the second, third, and finally, the fourth character.
That summarizes the functionalities in **Fonctions.py**

| <p align="center">**Value of special card**</p>| <p align="center">**methods corresponding**</p>               |<p align="center">**resultat on the array**</p>                                     |
|:-----------------------------------------------|:--------------------------------------------------------------|:-----------------------------------------------------------------------------------|
|<p align="center">+2</p>                        |<p align="center">Sens.piochetonext(2) + Sens.finTour()</p>    |<p align="center">__Number of cards by character:__ [B2: 7, B3: 7, P: 7, B1: 9]</p> |
|<p align="center">+4</p>                        |<p align="center">Sens.piochetonext(4) + Carte.setCouleur()</p>|<p align="center">__Number of cards by character:__ [B2: 7, B3: 7, P: 7, B1: 11]</p>|
|<p align="center">↺</p>                         |<p align="center">Sens.reverse() + Sens.finTour()</p>          |<p align="center">__Exemple of the array:__ [Bot n°3, Bot n°2, Bot n°1, Player]</p> |
|<p align="center">⊝</p>                        |<p align="center">Sens.passerTour() + Sens.finTour()</p>       |<p align="center">__Exemple of the array:__ [Bot n°2, Bot n°3, Player, Bot n°1]</p> |
|<p align="center">⊕</p>                        |<p align="center">Carte.setCouleur() + Sens.finTour()</p>      |<p align="center">__Exemple of the array:__ [Bot n°1, Bot n°2, Bot n°3, Player]</p> |

That concludes the explanation for **Sens.py**
Now, let's explore how the program ensures it doesn't stop until a winner is declared. This functionality is implemented in **main.py**
### Main.py

```py
while not iswinner:
if type(sens.tableau[sens.cursor % (nb_bots + 1)]).__name__ == "MainJ":
  iswinner = sens.tableau[sens.cursor % (nb_bots + 1)].jouer(pioche, sens)
  if iswinner:
    aff_gagnant()
else:
  name = sens.tableau[sens.cursor % (nb_bots + 1)].name
  iswinner = sens.tableau[sens.cursor % (nb_bots + 1)].jouer(pioche, f"{sens.tableau[sens.cursor % (nb_bots + 1)].name}", sens)
  if iswinner:
    aff_perdant(name)
```

This loop keeps the game running until a winner is declared. When a winner is determined, we display the rankings. For each character's deck, we calculate the total score by summing the scores of all the cards.

__Here's an example of a ranking after a game:__

![ranking](https://github.com/DezJDev/Uno/assets/144434644/ec5f1b42-63c7-4be1-ab2b-7720f6d69139)

The Future of this Project:
__I plan to:__
* Extend the coverage of my unit tests.
* Make my project executable.
* Enable multiplayer on a single machine.
* Enable online multiplayer with a server.
* Develop a dedicated application for the project.


That concludes this README. Thank you for reading.
