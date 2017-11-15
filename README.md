# Nim in Brainfuck

A simple version of the game Nim written in Brainfuck. This was done in a single
night years ago, putting it on Github for fun. The `nim.pybf` file is a
pseudo-Brainfuck file that the `bf_reader.py` file translates into actual
Brainfuck (the main advantage of this is the ability to repeat characters with a
number, e.g. writing `++++` (`bf`) as `+4` (`pybf`)).

There are also comments in `nim.pybf` roughly explaining what's happening
throughout.

To build:

```
make
```

To run:

```
./nim
```

The program will wait for you to input a sequence of heaps (separated by
spaces), where each number you input represents the number of sticks in that
heap. The heap sizes must always be `< 10`.

After that, the first player takes their turn by inputting the heap they want to
remove from followed by the number of sticks to remove from that heap. Heaps are
indexed from one.

Example run with initial heap sizes of 5, 4, and 3, then the first player takes
2 sticks from heap 1:

```
./nim
5 4 3
1 2
3 4 3
```

The program automatically prints out the result of the player's move (in this
case, it printed `3 4 3`).

The game will not end automatically and there is no error checking. If something
goes wrong, you won't see any output after making a move.
