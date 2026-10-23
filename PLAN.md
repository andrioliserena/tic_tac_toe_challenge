# Tic-Tac-Toe — 5-Stage Implementation Plan

## Context
`tic_tac_toe.py` has 7 skeleton functions (`print_board`, `choose_player`, `ask_move`,
`check_winner`, `check_draw`, `switch_player`, `main`), all `pass`. `pseudocode.md`
describes the game. We fill them in over 5 stages, **one stage at a time**, stopping
after each so you can review and run it.

**Rules for all stages**
- Keep your function names; every function has a docstring.
- Each function body is 4–10 lines. Beginner-friendly Python, no classes.
- Run with: `uv run python tic_tac_toe.py`

**Board design (used by every stage):** a list of 9 strings, `" "` = empty.
Index `0–8` in code, the player types `1–9` (we subtract 1).
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

**Bug to fix in Stage 1:** the last lines read `if name == "main":` — must be
`if __name__ == "__main__":`, otherwise running the file crashes with `NameError`.

**New helper functions (additions, not renames):** to keep `main()` ≤ 10 lines we add
`create_board()` (Stage 1) and `play_round()` (Stage 2). `ask_move` and `main` stay.

---

## Stage 1 — Board + display
- `create_board()`: start with an empty list and `append(" ")` 9 times in a
  `for` loop, then return it (a loop instead of `[" "] * 9` keeps it within
  the 4–10 line rule).
- `print_board(board)`: print 3 rows `" X | O |  "` with `---+---+---` between them
  (loop over row starts `0, 3, 6`).
- `main()` (temporary): print a welcome line + the numbered guide, create a board,
  print it. Just enough to see the display working.
- Fix the `__name__ == "__main__"` guard.
- **Check:** run the script → empty grid is printed, no errors.

## Stage 2 — Turn-taking
- `choose_player()`: `input()` X or O, `.upper()`, return it (validation comes in Stage 5).
- `switch_player(player)`: return `"O"` if player is `"X"`, else `"X"`.
- `ask_move(board, player)`: ask for a number 1–9, place `player` at `board[move - 1]`.
- `play_round()`: create board, choose player, then a loop of
  ask_move → print_board → switch_player (no end condition yet besides 9 moves,
  using `for turn in range(9)`).
- `main()`: welcome + rules, call `play_round()`.
- **Check:** two players can fill all 9 squares, symbols alternate.

## Stage 3 — Win detection
- `check_winner(board)`: a list `WINNING_LINES` of the 8 index triples (3 rows,
  3 columns, 2 diagonals); loop over them and return the symbol (`"X"`/`"O"`) if all
  three squares are equal and not `" "`, else return `None`. The check is
  `board[a] != " " and board[a] == board[b] == board[c]` (simpler to read than
  the assignment's `all()` tip).
- `play_round()`: after each move, if `check_winner(board)` → print "Player X wins!"
  and `return` (ends the round).
- **Check:** play a row, a column and a diagonal win; game stops immediately.

## Stage 4 — Draw detection + play again
- `check_draw(board)`: loop over the squares, return `False` at the first `" "`,
  else return `True` (as in the pseudocode).
- `play_round()`: switch from `for` to `while not check_draw(board):`; when the
  loop ends without a winner, print "It's a draw!". The win check runs first, so
  a win on the last square counts as a win. (A `while True` with a separate draw
  check would make the function 12 lines.)
- `main()`: wrap in a loop — after a round, ask "Play again? (y/n)"; stop on `n`
  (the "start a new game or quit" part of the pseudocode).
- **Check:** fill the board without a winner → draw message; replay works.

## Stage 5 — Input validation
- `choose_player()`: `while True` loop — repeat until input is `"X"` or `"O"`,
  else print "Invalid input".
- `ask_move(board, player)`: `while True` loop —
  - if input is not in the list `"1"`–`"9"` → "Please enter a number from 1 to 9"
    (safer than `.isdigit()`, which lets through characters like `²` that crash `int()`)
  - elif square taken → "That square is taken, choose another"
  - else place the symbol and `return`.
- **Check:** try `abc`, `0`, `10`, empty input, an occupied square, lowercase `x`.

## Extra — Quit cleanly (EOF and Ctrl+C)
- In the `if __name__ == "__main__":` block, wrap `main()` in `try` / `except`
  so the game says goodbye instead of showing a traceback:
  - `except EOFError` → "No more input. Goodbye!" (input ran out, e.g. Ctrl+D
    or running without a keyboard)
  - `except KeyboardInterrupt` → "Game stopped. Goodbye!" (player pressed Ctrl+C)
- One wrapper covers every `input()` call, so no function changes.
- **Check:** press Ctrl+D and Ctrl+C at each question (symbol, square,
  play again) → goodbye message, no traceback.

---

## Workflow
Implement one stage, run it, review, then move on to the next stage.
