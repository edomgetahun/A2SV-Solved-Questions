class Solution:
    def minOperations(self, logs: List[str]) -> int:
            stack = []
            for folder in logs:
                if folder == "../":
                    if stack:
                        stack.pop()
                elif folder == "./":
                    continue
                else:
                    stack.append(folder)
            return len(stack)