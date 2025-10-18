import random
def quick_sort_deck(deck):
    if len(deck) < 4:
        return sorted(deck)
    pivot = random.choice(deck)
    left = [x for x in deck if x < pivot]
    middle = [x for x in deck if x == pivot]
    right = [x for x in deck if x > pivot]
    return quick_sort_deck(left) + middle + quick_sort_deck(right)
deck_of_cards = input()
res = list(map(int, deck_of_cards.split()))
sorted_res = quick_sort_deck(res)
print(sorted_res)