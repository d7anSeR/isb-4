import hashlib
import itertools

import multiprocessing as mp


def check_num_card(main_part_card: int, default_hash: str, bin: str, last_num: str) -> bool:
    card_num = f"{bin}{main_part_card}{last_num}"
    if hashlib.sha256(card_num.encode()).hexdigest() == default_hash:
        return card_num
    return False

def find_num_card(default_hash: str, last_num: str, bin: str, pools: int) -> int: 
    list_num = list(itertools.combinations_with_replacement(range(10), 7))
    arg = []
    for elem in list_num:
        arg.append((elem, default_hash, bin, last_num))
    with mp.Pool(processes=pools) as p:
        for result in p.map(find_num_card, arg):
            if result:
                p.terminate()
                return result
    return 0
