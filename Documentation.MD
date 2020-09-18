River-Crossing Game:

AIM:
	The River-Crossing Game is a game that involves a rabbit that needs to cross a river. For some reason, this rabbit can swim, which is how it crosses the river. There are bridges across the river which allow the rabbit to rest when it gets tired of crossing the river. Of course, the bridge is not completely safe because there are walls on the bridge. If the rabbit crashes into the wall, it dies. So stay away from the walls. The river is not completely safe either because it is infested with hungry crocodiles who love eating rabbits, especially rabbits that can swim, for some reason. When the crocodiles get too close to the rabbit, they can eat it and obviously the rabbit dies. 

	However, if you open the game, you will see that the rabbit is really cute, and has a family that will miss it if it dies. So try to help the rabbit cross the river and reach the other side alive. 

	To play this game, you need 2 players. Players 1 and 2 play each level alternatively. There are 3 levels in all. The player that earns maximum points wins. Note that even if a player loses, both progress to the next level. The only difference between levels is that the speed of the crocodiles increases, so there is a greater chance of getting eaten. But your aim is to cross the river without getting eaten, and without hitting a wall. 

	To control the rabbit, Player 1 will use the arrow keys and Player 2 will use the W, A, S, D keys to move up, left, down and right respectively. Time is also a key element because the rabbit does not like to wait. Finishing in under 8 seconds gets you a 50 point bonus, and under 12 seconds gets you a 25 point bonus. Finishing in between 12 and 20 seconds incurs a 25 point penalty and any more than that incurs a 50 point penalty.

	Crossing a crocodile earns you 10 points while crossing a wall will earn you 5 points. There are 9 walls and 6 crocodiles you must cross.

	Your mission, should you choose to accept it, is to help the rabbit cross the river as fast as possible without hitting any obstacles.

FUNCTIONALITY:
	This game was developed using Python3. It depends mainly on the pygame module that is part of Python3. The majority of the code is present in the 2019101120_game.py file while the remainder is present in the config.py file, which contains the win/lose messages, colors and fonts used.

	The game exists in a 1000x1000 display with a blue background to show the river. The bridges are created by drawing rectangles on top of the display. There are classes for the player, moving obstacles and fixed obstacles, all of which belong to the group all_sprites. The moving obstacles belong to a group called mobs and fixed obstacles belong to a group called fobs. These groups also belong to all_sprites. The fobs group members have fixed x and y coordinates, whereas the x coordinates of the mobs group members keep varying so they are stored in an array, which is varied in each tick of the game clock.

	The game has a clock to measure the progress of the game and synchronize all the elements with each other. A variable called stop is set to False. It becomes true when the game window is closed. Closing the game window also stops the execution of the game. The frame rate is set to 60 FPS to give an optimal viewing experience to the users. 

	The main player1 sprite can be controlled using arrow keys and W, A, S, D keys depending on who is currently playing. The collisions are checked by comparing the positions of the rectangles of each sprite using the sprite.spritecollide function offered in pygame. The variables x and y maintain the position of the sprite and they get updated whenever the user presses any of the keys given. The x coordinates of the moving obstacles are updated by storing their values inside an array that continuously gets updated with each clock cycle. If the position exceeds the screen width, start again from original position.

	The scoring is controlled by checking if the main sprite has y coordinates + sprite length <= y coordinates of the obstacle for player 1 and the reverse for player 2. These points get added until the player wins or hits an obstacle. In this case, the points for that round get updated to scores array along with any time bonus the player gets. In the end, when 6 rounds or 3 levels have been played, the show function shows the total points for both players and the winner.

	The timer function gets the ticks at the start of the round and then subtracts from the current ticks to find the time elapsed since the start of the particular round. 

	The scoreboard function receives inputs about the current status of the score and gets updated continuouly and displays scores without the time bonus and penalty.

	The config.py file stores information about colors used, fonts printed, and messages given to the user.

	In addition, a loser function alerts the user that they have lost, and winner function alerts the user that they have won, along with their points. Note that even if you lose a round, your points will still get added for that level depending on how far you have reached.If you lose, time bonus or penalty will not be awarded.

	The main loop continuously checks if the player sprite has reached its destination, upon which the winner function is displayed. Points along with time bonus get added to score array.

	Upon calling the winner and loser functions, the refresh function is called. This function checks the current player and round and adjusts the start position, the positions of the start and end variables, the speed of the moving obstacles, etc.

	When the game ends and the show function occurs, the winner is displayed for 5 seconds and then the game quits and ends.