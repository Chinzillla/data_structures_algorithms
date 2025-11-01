# Skill Level of player

### Problem: Identify the skill level of a player by rating

You are given a starting rating from the player, then the player plays a series of games that will impact the users rating.

### Input:

Starting Rating of player

Array of rating adjustments to be made

### Output:
Return the designated skill level of the player using this guideline:
Beginner - rating < 1500
Intermediate - 1500 <= rating < 2500
Advanced - 2500 <= rating < 3500
Expert - rating >= 3500

### Example:

Input:
- starting_rating = 1200
- adjustments = [150, -50, 200, 75, -25, 100]

Output: "Intermediate"

Explanation:
- Start: 1200
- After game 1: 1200 + 150 = 1350
- After game 2: 1350 - 50 = 1300
- After game 3: 1300 + 200 = 1500
- After game 4: 1500 + 75 = 1575
- After game 5: 1575 - 25 = 1550
- After game 6: 1550 + 100 = 1650
- Final rating: 1650
- 1500 <= 1650 < 2500, so skill level is "Intermediate"
