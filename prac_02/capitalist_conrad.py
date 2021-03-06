MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "veet.txt"

price = INITIAL_PRICE
print("Starting price : $(:,.2f}".format(price))
i = 0

out_file = open(OUTPUT_FILE, 'w')

while price >= MIN_Price and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_PRICE, 0)
    price = (1 + price_change)
    i += 1
    print("On day {} price is ${:,.2f}".format(i, price), file = out_file)

out_file.close()