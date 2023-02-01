def isIdentityCol(col):
    # Return n>= 0 if col is identity column, return index else -1
    try:
        if col.count(0) == len(col) - 1 and col.count(1) == 1:
            return col.index(1)
        return -1
    except:
        return -1


def isUnboundedCol(col):
    for i in col:
        if i > 0:
            return False
    return True
 