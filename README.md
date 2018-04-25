# MazeSolver
Maze Solver created in Python. Pretty lit.

This has been used to solve all three of the "largest" mazes shown on [astrolog.org](http://www.astrolog.org/labyrnth/maze.htm), with the help of a couple fellow developers and decent bit of time. It took just under 100 minutes to solve the 32767 x 32767 pixel (1.074 gigapixel) maze on that website using [Someone's](https://github.com/isik-kaplan) computer. In fact, here's a very zoomed-out screenshot of that:

<img src="https://i.imgur.com/2flbDmH.png">

More sample mazes (and their solutions) are provided in the repo, so you will be able to test them out for yourself. As these samples are very small, you'll likely want to use [astrolog's](http://www.astrolog.org/labyrnth/maze.htm) mazes to test it properly. You will probably have to adjust the start- and end-points in the code, though that isn't particularly difficult.

The program uses dead-end filling alongside a DFS algorithm to keep memory usage relatively low, while also keeping speed at a reasonable level (although some sacrifices had to be made in order to stop it from swallowing 30GB of memory on that ^ maze there).
