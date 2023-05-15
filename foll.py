E = 'Є'
is_terminal = lambda x: not x.isupper()
prods = {}
first_set = {}
follow_set = {}

def first(head: str, prods: dict):
    if is_terminal(prods[head][0][0]):
        ret = [p[0][0] for p in prods[head] if is_terminal(p[0][0])]
        for p in prods[head]:
            if E in p: ret.append(E)
        return ret
    return first(prods[head][0][0], prods)


def follow(rel: dict):
    global E, prods, first_set, follow_set
    for cur in rel.keys():
        if cur == list(rel.keys())[0]:
            follow_set[list(rel.keys())[0]] = ['$']
        for h in rel[cur]:
            for prod in prods[h]:
                if cur in prod:
                    idx = prod.index(cur)
                    if idx+1 == len(prod):
                        if h != cur:
                            follow_set[cur].extend(follow_set[h])
                    elif is_terminal(prod[idx+1]):
                        follow_set[cur].append(prod[idx+1])
                    else:
                        f = first_set[prod[idx+1]]
                        if E in f:
                            f.remove(E)
                            follow_set[cur].extend(f)
                            if cur != h:
                                follow_set[cur].extend(follow_set[h])


def main():
    global prods, first_set, follow_set
    p = int(input("Enter no.of prods: "))
    for i in range(1, p+1):
        buf = input(f"{i}: ")
        head, body = [x.strip() for x in buf.split("->")]
        body = [[y for y in x.strip().split(" ")] for x in body.split("|")]
        prods[head] = body
    for (k, _) in prods.items():
        first_set[k] = first(k, prods)
    rel = {k:[x[0] for x in prods.items()
                            if any([k in y for y in x[1]])]
                                for k in prods.keys()}
    follow_set = {k: [] for k in prods.keys()}
    follow(rel)
    for (head, body) in follow_set.items():
        print(f"FOLLOW({head})", body)

if __name__ == "__main__":
    exit(main() or 0)
