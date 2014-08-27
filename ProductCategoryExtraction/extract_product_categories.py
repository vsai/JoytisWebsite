import pprint

filename = "ProductsnCategories.txt"
f = open(filename)

all_txt = f.read()
all_txt = all_txt.splitlines()

p_n_c = []

d = {}

for line in all_txt:
    d = {}
    p = line.split(": ")
    #print p
    product = p[0]
    categories = p[1].split(", ") if (p[1] != '') else []
    d['product'] = product
    d['examples'] = categories
    p_n_c.append(d)

pprint.pprint(p_n_c)
