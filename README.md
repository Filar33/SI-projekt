# Rozwiązywanie labiryntów

Projekt optymalizacji rozwiązywania labiryntów za pomocą algorytmu DFS (Depth-first search).
Ścieżka wybierana jest na podstawie stosunku kosztu przejścia ścieżki do jej długości.
<br>-Każdy krok dodaje 1 do licznika kosztu
<br>-Pola nagrody z ,,+" odejmują 3 od licznika kosztu
<br>-Pola kary z ,,-" dodają 3 do licznika kosztu
<br>Po zrealizowaniu ścieżki tworzony jest GIF reprezentujący przechodzenie labiryntu optymalną ścieżką.

## Przykłady GIF
![](https://github.com/Filar33/SI-projekt/blob/main/maze_solution.gif)
![](https://github.com/Filar33/SI-projekt/blob/main/maze_solution-1.gif)

# Przykład wyniku

## Wynik w konsoli:

```
Original Maze:
# x # # # # #
# -   +   - #
#   # # #   #
#   +     + #
# # # - # - #
#   -   -   #
# - # # + # #
#         # #
# + # # - # #
#       -   #
# e # # # # #

Path found:
Maze with path:
# P # # # # #
# P         #
# P # # #   #
# P P P P P #
# # #   # P #
#       P P #
#   # # P # #
# P P P P # #
# P # #   # #
# P         #
# e # # # # #

Path length: 18
Cost: 7
Cost to Path ratio: 0.39

Process finished with exit code 0
```
## Wygenerowany GIF na podstawie wyniku z konsoli:
![](https://github.com/Filar33/SI-projekt/blob/main/maze_solution-2.gif)
