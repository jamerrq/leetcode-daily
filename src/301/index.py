class Solution:
    @staticmethod
    def isValid(s: str, ignore_set: set[int]):
        depth = 0
        for i, char in enumerate(s):
            if i in ignore_set:
                continue
            if char == '(':
                depth += 1
            elif char == ')':
                if not depth:
                    return False
                depth -= 1

        return not depth

    @staticmethod
    def isValidAfterChanges(
        s:str,
        index_stack: list[int],        # indexes that can be removed '(' or ')'
        remaining:int,                 # how many left to remove
        candidates:set[str],           # to store the candidates
        ignore_set:set[int],           # indexes that won't count
        ) -> bool:
        if not remaining:
            n = len(s)
            veredict = Solution.isValid(s, ignore_set)
            if veredict:
                s_cand = "".join(s[i] for i in range(n) if i not in ignore_set)
                candidates.add(s_cand)
            return veredict
        if not index_stack:
            return False

        indexes_copy = [index for index in index_stack]
        index_to_ignore = indexes_copy.pop()
        ignore_set_copy = set(x for x in ignore_set)
        ignore_set_copy.add(index_to_ignore)

        # option 1, to change
        option1 = Solution.isValidAfterChanges(
            s,
            indexes_copy,
            remaining - 1,
            candidates,
            ignore_set_copy,
        )
        # option 2, to pass
        option2 = Solution.isValidAfterChanges(
            s,
            indexes_copy,
            remaining,
            candidates,
            ignore_set,
        )

        return option1 or option2

    def removeInvalidParentheses(self, s: str) -> list[str]:
        depth, changes = 0, 0
        open_stack, close_stack = [], []
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
                open_stack.append(i)
            elif char == ')':
                if not depth:
                    changes += 1
                else:
                    depth -= 1
                close_stack.append(i)

        choosen_stack = []
        if depth and not changes:
            choosen_stack = [index for index in open_stack]
        elif changes and not depth:
            choosen_stack = [index for index in close_stack]
        else:
            choosen_stack = [index for index in open_stack + close_stack]

        choosen_stack.sort()

        candidates = set()
        ignore_set = set()
        remaining = depth + changes
        self.isValidAfterChanges(
            s, choosen_stack, remaining, candidates, ignore_set
        )

        return list(candidates)