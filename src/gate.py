from collections import deque

class Gate:
    def __init__(self):
        # Pattern is 1 fastpass, then 3 regulars
        self._pattern = ["fastpass", "regular", "regular", "regular"]
        self._idx = 0
        self._fast = deque()
        self._reg = deque()

    def arrive(self, line, person_id):
        # Enqueue into the chosen line
        if line == "fastpass":
            self._fast.append(person_id)
        elif line == "regular":
            self._reg.append(person_id)
        else:
            raise ValueError("Unknown line type")

    def serve(self):
        """
        Return the next person according to the repeating pattern.
        Skip empty lines but still move the cycle pointer correctly.
        Raise IndexError only if BOTH queues are empty.
        """
        # First, check if there's anyone to serve at all.
        if not self._fast and not self._reg:
            raise IndexError("Both lines are empty")

        # Now, find the next person. We are guaranteed to find one because
        # of the check above.
        while True:
            line_to_serve = self._pattern[self._idx]

            if line_to_serve == "fastpass" and self._fast:
                person = self._fast.popleft()
                self._idx = (self._idx + 1) % len(self._pattern)
                return person
            elif line_to_serve == "regular" and self._reg:
                person = self._reg.popleft()
                self._idx = (self._idx + 1) % len(self._pattern)
                return person
            else:
                # The designated line is empty, just move the pointer and
                # the loop will try the next slot in the pattern.
                self._idx = (self._idx + 1) % len(self._pattern)

    def peek_next_line(self):
        """
        Predict which line will serve next without dequeuing anyone.
        """
        # Create a temporary index so we don't change the gate's actual state
        temp_idx = self._idx
        
        # Check a full cycle of the pattern
        for _ in range(len(self._pattern)):
            line = self._pattern[temp_idx]
            if line == "fastpass" and self._fast:
                return "fastpass"
            if line == "regular" and self._reg:
                return "regular"
            # Move to the next slot for the next check
            temp_idx = (temp_idx + 1) % len(self._pattern)
        
        # If the loop completes, it means no one is in any line
        return None