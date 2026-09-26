# [1096. Brace Expansion II](https://leetcode.com/problems/brace-expansion-ii/description)

**Level**: <span style="color:red">Hard</span>

Under the grammar given below, strings can represent a set of lowercase words. Let `R(expr)` denote the set of words the expression represents.

The grammar can best be understood through simple examples:

- Single letters represent a singleton set containing that word.
    - `R("a") = {"a"}`
    - `R("w") = {"w"}`
- When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
    - `R("{a,b,c}") = {"a","b","c"}`
    - `R("{{a,b},{b,c}}") = {"a","b","c"}` (notice the final set only contains each word at most once)
- When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
    - `R("{a,b}{c,d}") = {"ac","ad","bc","bd"}`
    - `R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}`

Formally, the three rules for our grammar:

- For every lowercase letter `x`, we have `R(x) = {x}`.
- For expressions `e1, e2, ... , ek` with `k >= 2`, we have `R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...`
- For expressions `e1` and `e2`, we have `R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}`, where `+` denotes concatenation, and `×` denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return *the sorted list of words that the expression represents*.

## Examples

### Example 1:

Input: `expression = "{a,b}{c,{d,e}}"`

Output: `["ac","ad","ae","bc","bd","be"]`

### Example 2:

Input: `expression = "{{a,z},a{b,c},{ab,z}}"`

Output: `["a","ab","ac","z"]`

Explanation: Each distinct word is written only once in the final answer.


## Constraints

- `1 <= expression.length <= 60`
- `expression[i]` consists of `'{'`, `'}'`, `','` or lowercase English letters.
- The given expression represents a set of words based on the grammar given in the description.

## My Solution

[index.py](./index.py)

```python
def breakdown(expr: str) -> tuple[bool, list[str], bool]:
    """
    Take an expression and return a triple (L, T, B)
    where
    L: bool -> whether it is a list (union)
    T: [str] -> factors (if it is not a list) | terms (if it is a list)
    B: bool -> whether the expression has braces
    """
    is_list = False
    has_braces = False # to notice if the expression need further reduccion
    curr = ""
    factor = ""
    terms = []
    factors = []
    depth = 0
    for char in expr:
        # get deeper
        if char == '{':
            depth += 1
            has_braces = True
            if depth == 1:
                if factor:
                    factors.append(factor)
                    factor = ""
        # get shallower
        if char == '}':
            depth -= 1
            if not depth:
                factors.append(factor)
                factor = ""
        # first-order braces are not included
        if (char != '{' or depth != 1) and (char != '}' or depth != 0):
            factor += char
        # found a top-level comma: it is a list
        if char == ',' and depth == 0:
            is_list = True
            terms.append(curr)
            curr = ""
            continue
        curr += char
    if is_list:
        terms.append(curr)
        return True, terms, has_braces
    else:
        factors.append(factor)
        return False, factors, has_braces


def union(terms: set[str]) -> set[str]:
    ans = set()
    for term in terms:
        factors = reduce_expression(term)
        ans |= factors
    return ans

def cartesian_product(terms: list[str]) -> set[str]:
    head = terms[0]
    product = reduce_expression(head)
    for i in range(1, len(terms)):
        curr = terms[i]
        factors = reduce_expression(curr)
        new_terms = set()
        for curr_term in product:
            for factor in factors:
                new_term = curr_term + factor
                new_terms.add(new_term)
        product = new_terms
    return product

def reduce_expression(expr: str) -> set[str]:
    is_list, terms, has_braces = breakdown(expr)
    if is_list:
        return union(set(terms))
    if has_braces:
        return cartesian_product(terms)
    return set(terms)

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        terms = reduce_expression(expression)
        return sorted(list(terms))
```

## Brief Explanation
This is the first hard problem I solved on my own.
The idea is actually quite simple: expressions can be split into two categories, simple (atomic) and complex. Atomic expressions have this form:

- $e = L_1,L_2,...,L_n$ where $L_i = l_{i,1}l_{i,2}...l_{i,m_i}$ and each $l_{i,j}$ is a lowercase letter

Expressions of this form are called atomic because they are the base case of our recursion, and their value is simply $R(e) = [L_1,L_2,...,L_n]$

Some examples of these atomic expressions are `"a"`, `"aaaa"`, `"a,b"`,`"xz,y,z"` and `"az,xc"`.

The other group, which I call complex expressions, must be reduced. To do that, we divide them into two kinds:

- Lists: $E_l = e_1,e_2,e_3,...,e_n$
- Combinations: $E_c = e_1e_2e_3...e_n$

Their (recursive) definitions are:

- $R(E_l) = R(e_1) \cup R(e_2) \cup \cdots \cup R(e_n)$
- $R(E_c) = R(e_1) \times R(e_2) \times \cdots \times R(e_n)$

The definition of these operations is explained more clearly on the [problem's page](https://leetcode.com/problems/brace-expansion-ii/description).

Regarding the code, it is helpful to notice that lists contain zero-depth commas, where the depth of a character is the number of open braces to its left minus the number of closed ones. At the same time, braces that opens and closes at zero depth help to split the expression into factors in case it is an association.

The `breakdown` function iterates through the expression once to determine whether it is a list, and then splits it into sub-terms accordingly.

## Runtime

2 ms | Beats 83.42% ![clapping_hands](../../lib/clapping_hands.svg)

## Memory

19.46 MB | Beats 82.90% ![clapping_hands](../../lib/clapping_hands.svg)

## Link

[![leetcode](../../lib/leetcode.svg)](https://leetcode.com/problems/brace-expansion-ii)