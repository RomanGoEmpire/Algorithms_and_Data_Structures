from shortest_path import shortest_path_search


def successors(X, Y):
    def sc(state):
        x, y = state

        assert x <= X and y <= Y
        return {(0, y + x) if y + x <= Y else (x - (Y - y), Y): 'x->y',
                (x + y, 0) if x + y <= X else (X, y - (X - x)): 'x<-y',
                (X, y): 'fill x',
                (x, Y): 'fill y',
                (0, y): 'empty x',
                (x, 0): 'empty y'}

    return sc


if __name__ == '__main__':
    res = shortest_path_search((0, 0), successors(418, 986), lambda state: state == (6, 0))
    print(res)
    print('% s transitions' % (int(len(res) / 2)))
    for i in range(10, 5, -1):
        print(i)
