from tqdm import tqdm

import hashlib
import multiprocessing as mp


def check_num_card(default_hash: str, bin: int, main_part_card: list, last_num: str) -> bool:
    card_num = f"{bin}{main_part_card:06d}{last_num}"
    tmp = hashlib.sha3_256(card_num.encode()).hexdigest()
    if  tmp == default_hash:
        return card_num
    return False

def find_num_card(default_hash: str, bins: list, last_num: str, pool: int) -> int: 
    list_num = range(1000000)
    arg = []
    for bin in bins:
        for elem in list_num:
            arg.append((default_hash, bin, elem, last_num))
    with mp.Pool(processes=pool) as p:
        for result in p.starmap(check_num_card, tqdm(arg, colour= "#008000", 
                                                     desc="The card number is searched by hash: ")):
            if result:
                p.terminate()
                return result
    return 0
