def test(game_window):
    def tst():
        print('TEST')
        for row in game_window.city_space.lots:
            for lot in row:
                print(lot.show(), end=' | ')
            print('---')
    return tst