# Prime Game

## Description
Maria and Ben play a game involving prime numbers. The rules of the game are as follows:

1. Given a set of consecutive integers starting from 1 up to and including `n`, players take turns picking a prime number from the set.
2. When a prime number is chosen, it and all of its multiples are removed from the set.
3. The player who cannot make a move loses the game.

Maria always goes first, and both players play optimally.

The task is to determine who the overall winner is after `x` rounds of the game.

---

## Prototype
```python
def isWinner(x, nums):
```

### Parameters:
- `x` (int): The number of rounds.
- `nums` (list of int): A list where each element `n` represents the range of numbers (1 to `n`) for each round.

### Returns:
- A string:
  - `"Maria"` if Maria wins the most rounds.
  - `"Ben"` if Ben wins the most rounds.
  - `None` if the result is a tie.

---

## Example
```python
x = 3
nums = [4, 5, 1]

print(isWinner(x, nums))
# Output: "Ben"
```

### Explanation:
1. **Round 1 (n=4)**:
   - Maria picks 2, removing 2 and 4 (set: [1, 3]).
   - Ben picks 3, removing 3 (set: [1]).
   - Ben wins as there are no primes left for Maria.

2. **Round 2 (n=5)**:
   - Maria picks 2, removing 2 and 4 (set: [1, 3, 5]).
   - Ben picks 3, removing 3 (set: [1, 5]).
   - Maria picks 5, removing 5 (set: [1]).
   - Maria wins as there are no primes left for Ben.

3. **Round 3 (n=1)**:
   - Ben wins immediately as there are no primes for Maria to pick.

Result: Ben wins 2 rounds, Maria wins 1 round. Ben is the overall winner.

---

## Files
### `0-prime_game.py`
Contains the implementation of the `isWinner` function.

### `main_0.py`
A script to test the `isWinner` function with various inputs.

---

## Requirements
- Python 3.x
- Code follows [PEP 8](https://peps.python.org/pep-0008/) style guidelines.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-interview.git
   cd alx-interview/0x0A-primegame
   ```

2. Run the test script:
   ```bash
   ./main_0.py
   ```

---

## Author
**Daniel Kipkosgei**  
[GitHub](https://github.com/Chirchir-Dan)


