from copy import deepcopy


size = 4
empty_char = "e"
empty_set = set(empty_char)


level1 = "r,b,b,b,b,r,r,r,e,e,e,e"
level2 = "o,r,b,o,b,o,b,o,b,r,r,r,e,e,e,e,e,e,e,e"
level3 = "p,b,g,p,p,b,g,g,b,g,p,b,e,e,e,e,e,e,e,e"
level10 = "m,g,m,p,r,p,br,o,g,c,c,m,g,o,o,p,r,g,br,br,c,c,r,m,br,o,p,r,e,e,e,e,e,e,e,e"
level51 = "c,o,p,b,dc,c,r,p,dc,p,dc,r,c,br,b,o,r,o,br,o,r,b,br,br,b,c,p,dc,e,e,e,e,e,e,e,e"
level74 = "c,b,c,o,o,y,wc,p,p,p,br,c,b,m,wc,y,r,br,y,c,p,br,m,wc,r,m,y,o,o,wc,r,b,b,br,r,m,e,e,e,e,e,e,e,e"


def won(bottles):
    for bottle in bottles:
        if len(set(bottle)) > 1:
            return False
    return True


def gen_bottles(level):
    ll = level.split(",")
    return [ll[i : i + size] for i in range(0, len(ll), size)]


def get_top_color(bottle):
    for i in range(len(bottle)):
        if bottle[i] != empty_char:
            return bottle[i], i
    return empty_char, 3


def useless_pour(src, dst):
    s = set(src)
    s.discard(empty_char)
    d = set(dst)
    d.discard(empty_char)

    if (len(s) == 0 and len(d) == 1) or (len(s) == 1 and len(d) == 0):
        return True
    return False


def done_bottle(bottle):
    s = set(bottle)
    s.discard(empty_char)
    return bool(s)


def is_empty_bottle(bottle):
    return set(bottle) == empty_set


def pour(src_bottle, dst_bottle):
    if is_empty_bottle(src_bottle):
        return False

    if useless_pour(src_bottle, dst_bottle):
        return False

    src_color, src_pos = get_top_color(src_bottle)
    dst_color, dst_pos = get_top_color(dst_bottle)

    if dst_pos == 0 and dst_color != "e":
        return False  # dst has no empty positions

    if src_color != dst_color and dst_color != "e":
        return False  # wrong top color, can't pour

    to_be_pourd_length = 0
    for i in range(src_pos, len(src_bottle)):
        if src_bottle[i] == src_color:
            to_be_pourd_length += 1
        else:
            break

    empty_length = 0
    for i in range(size):
        if dst_bottle[i] == empty_char:
            empty_length += 1
        else:
            break

    if to_be_pourd_length > empty_length:
        return False

    # pouring
    from_pos = src_pos
    to_pos = dst_pos if dst_color == "e" else (dst_pos - 1)
    while to_pos > -1 and from_pos < 4 and src_bottle[from_pos] == src_color:
        dst_bottle[to_pos], src_bottle[from_pos] = (
            src_bottle[from_pos],
            dst_bottle[to_pos],
        )
        from_pos += 1
        to_pos -= 1
    return True


def solve(bottles):
    if won(bottles):
        print("Success")
        return True, []

    action = False
    for src_i in range(len(bottles)):
        for dst_j in range(len(bottles)):
            if src_i == dst_j:
                continue

            new_bottles = deepcopy(bottles)
            poured = pour(new_bottles[src_i], new_bottles[dst_j])
            if poured:
                action = True
                # print(f"move {src_i+1} to {dst_j+1}")
                result, moves = solve(new_bottles)
                if result:
                    return True, moves + [f"pour {src_i+1} to {dst_j+1}"]
    if not action:
        print("Stalled")
        return False, None
    return False, None


succes, moves = solve(gen_bottles(level2))
print("=========================================")
for move in moves[::-1]:
    print(move)

# print(bottles)
# print('==============================')
# print(get_top_color(['r','r','b','b']))
# print(get_top_color(['e','e','b','b']))
# print(get_top_color(['e','e','e','e']))
# print(get_top_color(['e','r','b','b']))
# print('==============================')
# print(pour(bottles[0], bottles[1]), '== False')
# print(pour(bottles[1], bottles[0]), '== False')
# print(bottles)
# print(pour(bottles[0], bottles[2]), '== True\n', bottles)
# print(pour(bottles[1], bottles[0]), '== True\n', bottles)
# print(pour(bottles[2], bottles[1]), '== True\n', bottles)
# print(won(bottles))
# print('==============================')
