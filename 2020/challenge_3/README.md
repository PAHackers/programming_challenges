# Challenge

I have implemented a simple guessing game. It listens on port 8888 and will allow
anyone to play without authenticating using a simple TCP client such as netcat
or telnet. The game play looks like this:

```
$ nc localhost 8888
Hello! What is your name?
ThunderHorse
Greetings, ThunderHorse, I'm thinking of a number between 1 and 32.
You get 5 guesses.
Make a guess:
10
Too low, try again.
Make a guess:
25
Too high, try again.
Make a guess:
22
Too high, try again.
Make a guess:
16
Too low, try again.
Make a guess:
17
Well done, ThunderHorse! You guessed correctly in 5 guesses.
```

The code for this guessing game can be found [here](./guessing_game_server.py).

## Goal

There's a bug in my code that results in a denial of service vulnerability. Write
a program (in any language) that exploits this vulnerability. You exploit should
be as simple as possible and behave predictably.

## Scoring Points

5 points will be awarded for exploits that appear to work for all practical purposes.

10 points will be awarded for exploits that are guaranteed to work if the server
is run using the CPython interpreter.

Points will not be awarded for exploits that can be further simplified.


## Submission and Due Date
PM your code to @ThunderHorse on the PA Hackers by 11:59PM on Sunday, January 3, 2021.
