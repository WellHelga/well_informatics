gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]
gold_prices = [gold_prices_1, gold_prices_2, gold_prices_3, gold_prices_4, gold_prices_5]
for i, prices in enumerate(gold_prices, 1):
    mn = prices[0]
    mx = 0
    for j in prices[1:]:
        if j < mn:
            mn = j
        else:
            x = j - mn
            if x > mx:
                mx = x
    print(mx)