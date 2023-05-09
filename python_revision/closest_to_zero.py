# Closest to Zero Problem

# function returns integer in array 'ints' that is closest to zero
def closest_to_zero(ints):
    # if ints is None or empty, return 0
    if ints is None or ints == []:
        return 0
    else:
        # loop through ints and find closes to zero for pos and neg values
        pos_ints = []
        neg_ints = []
        for n in ints:
            if n > 0:
                pos_ints.append(n)
            elif n < 0:
                neg_ints.append(n)
            else:
                return 0
        pos_ctz = min(pos_ints)
        neg_ctz = max(neg_ints)
        # compare the closest to zero neg to pos
        if pos_ctz <= abs(neg_ctz):
            return pos_ctz
        else:
            return neg_ctz


print(closest_to_zero([]))
print(closest_to_zero(None))
print(closest_to_zero([-3, -23, 45, 3, 21, 204, -19, 233, 7, 20, -2]))

