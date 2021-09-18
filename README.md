# **River-Crossing Game**

## Overview

The river-crossing game is an interactive, multi-player, multi-level game that involves a rabbit, and a crocodile infested river filled with obstacles.
The goal of the two players is to transport the rabbit to the other bank while ensuring the rabbit does not come into contact with the obstacles, and trying to do so as soon as possible. 

## Instructions and Rules

Player 1 starts the game, and controls the rabbit using the arrow keys and transports the rabbit from the bottom of the screen to the top. Player 2 controls the rabbit using the `W`, `A`, `S` and `D` keys and transports the rabbit from the top of the screen to the bottom. Completing the game before the timer counts down grants the player a bonus, and exceeding the time limit incurs a penalty. Each level has an increase in the difficulty caused by an increase in the speed of the moving obstacles. At the end of the three levels, the player with the most points wins.

## Implementation

- Object Oriented Programming: All major components are stored in the form of objects and classes in order to ensure smooth functioning and resuability of code. The `Player` class is used for the player sprite, and the `Mobstacle` and `Fobstacle` classes indicate moving and fixed obstacles respectively. Additionally, groups are used to control all sprites, moving obstacles and fixed obstacles.

- Initial Set Up: The clock is initialized using the time module, and the display is set using `pygame's` display function. The positions for the obstacles are stored in lists, and they are added on top of the background. Next, the player is initialized.

- Major Functions: 
  -  `Timer`: Monitor time for speed, and in-game clock display.
  -  `Refresh`: Restart the game after a round ends, which includes displaying points screen, resetting positions based on player, and speeds of obstacles.
  -  `Scoreboard`: Maintain the score using the `score` variable for each player, and display the score on the screen.
  -  `Show`: Shows the final score after the game ends.

- Game Loop: The components are rendered in a continuous while loop that terminates once the user exits the game. This function contains things like checking for success, collisions, rounds, bonus scores, etc.
