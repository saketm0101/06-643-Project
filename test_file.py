import distillation as d


def is_int(n):
    return isinstance(n, int)


def test_distillation():
    n_test = d.mccabe_thiele_calculations(3000, 0.6, 0.98)[0]
    assert is_int(n_test)
