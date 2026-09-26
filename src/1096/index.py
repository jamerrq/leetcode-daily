def breakdown(expr: str) -> tuple[bool, list[str], bool]:
    """
    Take an expression and return a triple (L, T, B)
    where
    L: bool -> whether it is a list (union)
    T: [str] -> factors (if it is not a list) | terms (if it is a list)
    B: bool -> whether the expression has braces
    """
    is_list = False
    has_braces = False
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
        # found a top-level comma: it is a list
        if char == ',' and depth == 0:
            is_list = True
            terms.append(curr)
            curr = ""
            continue
        # get shallower
        if char == '}':
            depth -= 1
            if not depth:
                factors.append(factor)
                factor = ""
        curr += char
        # first-order braces are not included
        if (char != '{' or depth != 1) and (char != '}' or depth != 0):
            factor += char
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