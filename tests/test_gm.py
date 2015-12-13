#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_stockfighter
----------------------------------

Tests for `stockfighter` module.
"""
import os
import pytest
from stockfighter.gm import GM

@pytest.fixture
def client():
    return GM()


def test_start(client):
    assert client.start()
