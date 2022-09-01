

class pair:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def __eq__(self, other):
        return (
            self.a == other.a
            and
            self.b ==other.b
        )

    def __hash__(self):
        return hash(self.a + self.b)
    def __str__(self) -> str:
        return f"[{self.a}, {self.b}]"
p = pair(1,4)
q = pair(1,4)
s = set()

s.add(p)
s.add(q)
print(*s)