E = 'Є'
is_terminal = lambda x: not x.isupper()

def first(head: str, prods: dict):
    if is_terminal(prods[head][0][0]):
        ret = [p[0][0] for p in prods[head] if is_terminal(p[0][0])]
        for p in prods[head]:
            if E in p: ret.append(E)
        return ret
    return first(prods[head][0][0], prods)

def main():
    prods = {}
    p = int(input("Enter no.of prods: "))
    for i in range(1, p+1):
        buf = input(f"{i}: ")
        head, body = [x.strip() for x in buf.split("->")]
        body = [[y for y in x.strip().split(" ")] for x in body.split("|")]
        prods[head] = body
    for (k, _) in prods.items():
        print(f'FIRST({k})', first(k, prods))

if __name__ == "__main__":
    exit(main() or 0)
