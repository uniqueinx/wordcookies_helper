from copy import deepcopy


SIZE = 4
EMPTY_CHAR = "e"

levels = {
    "level1": "r,b,b,b,b,r,r,r,e,e,e,e",
    "level2": "o,r,b,o,b,o,b,o,b,r,r,r,e,e,e,e,e,e,e,e",
    "level3": "p,b,g,p,p,b,g,g,b,g,p,b,e,e,e,e,e,e,e,e",
    "level10": "m,g,m,p,r,p,br,o,g,c,c,m,g,o,o,p,r,g,br,br,c,c,r,m,br,o,p,r,e,e,e,e,e,e,e,e",
    "level51": "c,o,p,b,dc,c,r,p,dc,p,dc,r,c,br,b,o,r,o,br,o,r,b,br,br,b,c,p,dc,e,e,e,e,e,e,e,e",
    "level74": "c,b,c,o,o,y,wc,p,p,p,br,c,b,m,wc,y,r,br,y,c,p,br,m,wc,r,m,y,o,o,wc,r,b,b,br,r,m,e,e,e,e,e,e,e,e",
}


def won(bottles):
    for bottle in bottles:
        if bottle and len(bottle) != SIZE or len(set(bottle)) > 1:
            return False
    return True


def gen_bottles(level):
    ll = level.split(",")
    bottles = []
    for i in range(0, len(ll), SIZE):
        bottle = []
        for j in range(i + SIZE - 1, i - 1, -1):
            if ll[j] != EMPTY_CHAR:
                bottle.append(ll[j])
        bottles.append(bottle)
    return bottles


def get_top_color(bottle):
    if bottle:
        return bottle[-1]
    return None


def useless_pour(src, dst):
    if not dst and len(set(src)) == 1:
        return True

    to_be_pourd_length = 0
    src_color = get_top_color(src)
    for i in range(len(src) - 1, -1, -1):
        if src[i] == src_color:
            to_be_pourd_length += 1
        else:
            break

    empty_length = SIZE - len(dst)

    if to_be_pourd_length > empty_length:
        return True

    return False


def done_bottle(bottle):
    return len(bottle) == SIZE and len(set(bottle)) == 1


def is_empty_bottle(bottle):
    return not bool(bottle)


def is_full_bottle(bottle):
    return len(bottle) == SIZE


def pour(src_bottle, dst_bottle):
    if is_empty_bottle(src_bottle):
        return False

    if is_full_bottle(dst_bottle):
        return False  # dst has no empty positions

    if done_bottle(src_bottle) or done_bottle(dst_bottle):
        return False

    if useless_pour(src_bottle, dst_bottle):
        return False

    src_color = get_top_color(src_bottle)
    dst_color = get_top_color(dst_bottle)

    if dst_color and src_color != dst_color:
        return False  # wrong top color, can't pour

    # pouring
    while len(dst_bottle) < SIZE and src_bottle and src_bottle[-1] == src_color:
        dst_bottle.append(src_bottle.pop())

    return True


def solve(bottles):
    if won(bottles):
        print("Solved!")
        return True, []

    for src_i in range(len(bottles)):
        for dst_j in range(len(bottles)):
            if src_i == dst_j:
                continue
            new_bottles = deepcopy(bottles)
            poured = pour(new_bottles[src_i], new_bottles[dst_j])
            if poured:
                result, moves = solve(new_bottles)
                if result:
                    return True, moves + [f"pour {src_i+1} to {dst_j+1}"]
    return False, None


for level in levels.values():
    succes, moves = solve(gen_bottles(level))
    for move in moves[::-1]:
        print(move)
