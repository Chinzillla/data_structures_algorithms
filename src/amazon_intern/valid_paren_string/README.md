# Valid Parenthesis String

### Problem: Validate Parenthesis with Wildcard

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

### Rules:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

### Input:

- **s**: A string containing only '(', ')', and '*' characters

### Output:

Boolean value (true if the string is valid, false otherwise)

### Examples:

Example 1:
```python
Input: s = "()"
Output: true
```

Example 2:
```python
Input: s = "(*)"
Output: true
```

Example 3:
```python
Input: s = "(*))"
Output: true
```

### Constraints:

- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'