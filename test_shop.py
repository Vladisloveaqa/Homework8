import pytest
from homework.models import Product, Cart


def test_check_quantity_true():
    p = Product("Book", 100, "Nice book", 10)
    assert p.check_quantity(5) is True


def test_check_quantity_false():
    p = Product("Book", 100, "Nice book", 10)
    assert p.check_quantity(15) is False


def test_buy_success():
    p = Product("Book", 100, "Nice book", 10)
    p.buy(3)
    assert p.quantity == 7


def test_buy_not_enough():
    p = Product("Book", 100, "Nice book", 10)
    with pytest.raises(ValueError):
        p.buy(20)


def test_add_product():
    p = Product("Book", 100, "Nice book", 10)
    cart = Cart()
    cart.add_product(p, 2)
    assert cart.products[p] == 2


def test_remove_product_all():
    p = Product("Book", 100, "Nice book", 10)
    cart = Cart()
    cart.add_product(p, 2)
    cart.remove_product(p)
    assert p not in cart.products


def test_get_total_price():
    p = Product("Book", 100, "Nice book", 10)
    cart = Cart()
    cart.add_product(p, 3)
    assert cart.get_total_price() == 300


def test_cart_buy_success():
    p = Product("Book", 100, "Nice book", 10)
    cart = Cart()
    cart.add_product(p, 3)
    cart.buy()
    assert p.quantity == 7
    assert len(cart.products) == 0
