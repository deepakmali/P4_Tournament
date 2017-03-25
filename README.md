# Synopsis
This Project is to create and test a database backend for pairing up the 
players, storing the matches and the results for a tournament.

# Motivation
I have done this project as part of Full Stack Nano Degree from Udacity.
This is the fourth project in the curriculam.

# Installation
* Make sure your system has [python](https://www.python.org/downloads/) installed.
* Install [postgresql](https://www.postgresql.org/download/) database.
* Download all the files or clone the repository to your local machine.
* This project uses a python module *bleach* Install it from [here.](https://pypi.python.org/pypi/bleach)
* Connect to postgresql db ```psql ``` from command line.
* Run the SQL file ```tournament.sql``` in ```psql``` prompt 
using ```\i tournament.sql```.
* Run ```\q``` to exit from the ```psql``` prompt.

# How to run the project?
* Open the terminal(Linux & Mac), command prompt(Windows).
* Navigate to the directory where the files are downloaded.
* Run ``` python tournament_test.py ``` This should provide the below output.
```
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```

# Credits
* README.md format is taken from [jxon](https://gist.github.com/jxson/1784669)
* Test cases file ```tournament_test.py``` is provided from [Udacity.](https://www.udacity.com)
* I would like to thank Udacity discussion forum for helping me out 
when stuck with problem.