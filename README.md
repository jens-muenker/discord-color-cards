# discord-color-cards
Discord chat game. Who will be the first to run out of cards? Only the player with the correct color, number or symbol may discard a card. You can't lay? Then I guess you'll have to pick up a card! Special cards add to the fun. Let yourself be surprised. - It's simple to understand and easy to set up.

[Not the right game? Try Taboo for Discord!](https://github.com/Frosch2010/discord-taboo)

## Features

<img src="https://github.com/Frosch2010/discord-color-cards/blob/main/screenshots/Hand.jpg" height="521" width="353" align="right">

* 7 special cards (color wish, suspension, change of direction...)

* Voice output who is next

* Multilingual (English & German included. A language file for own translations can also be created).

* Viewer channel possible

* Setup wizard for easy startup

* Completely freely configurable

## Game principle

A randomly selected player starts. He must place a card on the deck. He can only place a card that has either the same color, the same number or the same symbol as the card on the deck.
If he cannot place a card, he must pick one up.
The first player to run out of cards wins the game.
(Which commands have to be entered for which action etc. is always written in the messages.)

## Special-cards (Symbols)

* 🔄 = Direction change
* 🔂 = Pass all hand cards in the direction of play.
* 🚫 = Suspension card
* ❌ = Put down all the cards of the suit.
* ⏫ = Plus card, the next player must take X cards or he can counter and put the same card.
* ❓ = The next player gets some cards. (Wish-Question)
* 👨‍👨‍👧‍👦 = All other players get some cards. (Wish-ALL)

## Installation

**What is needed?**
* Python 3.X
* Discord-Server
* ffmpeg

**Which Python packages are needed?**
* discord 1.5.X
* gtts
* termcolor


**Everything available?**
1. Download all files and copy all into the same folder
2. Launch the bot and use the setup wizard
3. **And your are ready to play with your friends.**

## Commands

The following commands are only for the following channels. (cc stands for the game-command.)

**Join Channel:**
```
!cc join                                - Join the game
!cc start [card-count]                  - Start the game (card-count defines the number of cards each player gets at the start of the game. If this is not specified, the default number from the settings is taken.)
```

**Private Channel (Player-Channel)**:
```
!card [card-number] or !c [card-number] - Lay a card (card-number = The number in front of the respective card.)
!getnewcard or !gnc                     - Pick up a card
!sitout or !so                          - Voluntarily sit out
!take or !t                             - Take the cards voluntarily
!leave                                  - Leave the game
```

**Admin Channel:**
```
!cc shutdown                            - Shutdown the bot
!cc kick @playername                    - Kick a player out of the game
!cc stop                                - Stop the current game
```

## Settings-file
```
Channel-IDs:
  "Administration": Channel for the admin commands.
  "Join":           Through the channel players can join and start the game.
  "Spectate":       Through the channel other players can watch the game.
  "Voice":          The channel is used to announce who is next. (The voice output must be activated for this.)
  
Game-Card-Settings:
  "Default-Cards-Per-Player":   Standard number of cards that everyone gets at the start of the game.
  "Plus-Card-Amount":           Number of cards you get with a Plus card.
  "Wish-All-Max-Amount":        Maximum number of cards you can get with a Wish All card.
  "Wish-All-Min-Amount":        Minimum number of cards you can get with a Wish All card.
  "Wish-Question-Max-Amount":   Maximum number of cards you can get with a Wish question card.
  "Wish-Question-Min-Amount":   Minimum number of cards you can get with a Wish question card.

Game-Settings
  "Better-Player-Notification": Should it be easier for players to see when it's their turn?
  "Delete-Old-Messages":        Strongly recommended not to change the setting!
  "Game-Command": "cc",         
  "Inf-Messages-Auto-Delete":   After how many seconds info messages should be deleted.
  "Min-Players":                What is the minimum number of players needed to start.
  "Output-To-Spectate":         Should there be a viewer channel.
  "Play-With-Reactions":        Strongly recommended not to change the setting!
  "Show-Player-Card-Count":     Should be displayed the number of cards of each player.
  
General-Settings
  "Bot-Token":
  "Server-ID":                  The ID of the server on which the game will be played.
   
Language-Settings
  "Discord-Language": "de"      Choose en or de or use the language-file.
  "Language-File-Path": "",     File path to the language-file.
  "Use-Language-File": false    User language-file.
    
Voice-Settings
  "Language":                   Choose one of these: https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang
  "Use-Voice":            
  "Windows-FFmpeg-Exe-Path":
    
```

## Wishes, Issues, Help needed?
Make a pull request. :)

## License
All code is under the [MIT](https://choosealicense.com/licenses/mit/) license.
