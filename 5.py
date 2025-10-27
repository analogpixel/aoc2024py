
rules = []
pages = []
#for line in open("data/5_demo.txt").readlines():
for line in open("data/5.txt").readlines():
    if "|" in line:
        rules.append( tuple(map(int, line.strip().split('|'))))
    elif "," in line:
        pages.append( list(map(int, line.strip().split(','))))
       

def apply_rules(rules, page):
    changed=True
    num_changes = 0
    # apply the rules until they stop changing.
    while changed:
        changed=False
        for r in rules:
            if r[0] in page and r[1] in page:
                idx1 = page.index(r[0])
                idx2 = page.index(r[1])
                
                if idx1 > idx2:
                    _a1 = page[idx1]
                    _a2 = page[idx2]
                    page[idx1] = _a2
                    page[idx2] = _a1
                    changed=True
                    num_changes +=1

    return [page, num_changes]

total_part_1=0
total_part_2=0
for p in pages:
    sorted_pages, change_count = apply_rules(rules, p)
    mid = int(len(p) / 2)
    if change_count == 0:
        total_part_1 += p[mid]  
    else:
        total_part_2 += p[mid]

print(total_part_1)
print(total_part_2)
