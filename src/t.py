
def merge(l1, l2):
    if len(l1) == 0:
        return l2

    if len(l2) == 0:
        return l1

    if l1[0] > l2[0]:
        [l1[0]].append(merge(l1[1:], l2))
    else:
        [l2[0]].append(merge(l1, l2[1:]))

