E = 'Є'
is_terminal = lambda x: not x.isupper()
prods = {}
first_set = {}
follow_set = {}
ll1_table = {}

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
                        f = first_set[prod[idx+1]].copy()
                        if E in f:
                            f.remove(E)
                            follow_set[cur].extend(f)
                            if cur != h:
                                follow_set[cur].extend(follow_set[h])

def ll1():
    global E, prods, first_set, follow_set, ll1_table
    for (k, v) in prods.items():
        for t in first_set[k]:
            if t == E:
                for b in follow_set[k]:
                    ll1_table[k][b] = {k: E}
            else:
                is_t_in_body = [pd for pd in range(len(v)) if t in v[pd]]
                if not is_t_in_body:
                    ll1_table[k][t] = {k: v}
                else:
                    ll1_table[k][t] = {k: v[is_t_in_body[0]]}

def main():
    global prods, first_set, follow_set, ll1_table
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
    terms = set(['$'])
    for prod in prods.values():
        for l in prod:
            for el in l:
                if is_terminal(el):
                    terms.add(el)
    ll1_table = {r: {c: None for c in terms} for r in first_set.keys()}
    ll1()
    print("LL(1) Parsing Table:-")
    for (r, c) in ll1_table.items():
        for (h, b) in c.items():
            print(r, h, b, sep="\t")
        print()

if __name__ == "__main__":
    exit(main() or 0)
