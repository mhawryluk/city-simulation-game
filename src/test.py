from game_engine_tools.simulation_tools import GOODS_PER_PERSON


def test(game_window):
    def tst():
        print('TEST')
        ps = game_window.simulator.player_status
        print(ps.data['goods'], ps.data['population'], ps.data['goods'] - ps.data['population'] * GOODS_PER_PERSON)
    return tst