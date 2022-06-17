from shortest_path import shortest_path_search


def successors(B):
    def sc(state):
        l, b, r = state
        ml, cl = l
        mb, cb, = b
        mr, cr = r

        return {
            ((ml - 1, cl), (mb + 1, cb), r) if ml - 1 >= cl and mb + cb < B else (l, b, r): 'ml -> mb',
            ((ml, cl - 1), (mb, cb + 1), r) if ml >= cl and mb + cb < B else (l, b, r): 'cl -> cb',
            (l, (mb - 1, cb), (mr + 1, cr)) if mr >= cr and mb >= 1 else (l, b, r): 'mb -> mr',
            (l, (mb, cb - 1), (mr, cr + 1)) if mr >= cr + 1 and cb >= 1 else (l, b, r): 'cb -> cr'
        }

    return sc


if __name__ == '__main__':
    res = shortest_path_search(((3, 3), (0, 0), (0, 0)), successors(2),
                               lambda state: state == ((0, 0), (0, 0), (3, 3)))
    print(res)
    print('% s transitions' % (int(len(res) / 2)))
