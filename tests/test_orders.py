from app.orders import total


def test_total():
    assert total([{"price": 10, "qty": 2}]) == 20
