#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_stockfighter
----------------------------------

Tests for `stockfighter` module.
"""
import os
import pytest
from stockfighter.stockfighter import Stockfighter

@pytest.fixture
def client():
    return Stockfighter(
        venue='TESTEX',
        account='EXB123456',
    )
STOCK = 'FOOBAR'


def test_heartbeat(client):
    assert client.heartbeat() is True

def test_venue_healthcheck(client):
    assert client.venue_healthcheck() is True

def test_venue_stocks(client):
    assert client.venue_stocks()['ok'] is True

def test_orderbook_for_stock(client):
    assert client.orderbook_for_stock(STOCK)['ok'] is True

def test_place_new_order(client):
    resp = client.place_new_order(
        stock=STOCK,
        price=500,  # Ignored for this market type
        qty=10,
        direction='buy',
        order_type='market',
    )
    assert resp

def test_quote_for_stock(client):
    assert client.quote_for_stock(stock=STOCK)['ok'] is True

def test_readme():
    """Test the content of the README works as advertised."""
    from stockfighter import Stockfighter
    s = Stockfighter(venue='TESTEX', account='EXB123456')

    from stockfighter import GM
    gm = GM()
