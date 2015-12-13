# -*- coding: utf-8 -*-
import os
import urlparse
import requests


class Stockfighter(object):
    base_url = 'https://api.stockfighter.io/ob/api/'

    def __init__(self, venue, account, api_key=None):
        self.venue = venue
        self.account = account

        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = os.environ['API_KEY']

        self.headers = {
          'X-Starfighter-Authorization': self.api_key
        }

    def heartbeat(self):
        """Check The API Is Up.
        
        https://starfighter.readme.io/docs/heartbeat
        """
        url = urlparse.urljoin(self.base_url, 'heartbeat')
        return requests.get(url).json()['ok']

    def venue_healthcheck(self):
        """Check A Venue Is Up.
        
        https://starfighter.readme.io/docs/venue-healthcheck
        """
        url = urlparse.urljoin(self.base_url, 'venues/TESTEX/heartbeat')
        return requests.get(url).json()['ok']

    def venue_stocks(self):
        """List the stocks available for trading on the venue.
        
        https://starfighter.readme.io/docs/list-stocks-on-venue
        """
        url = urlparse.urljoin(self.base_url, 'venues/{0}/heartbeat'.format(self.venue))
        return requests.get(url).json()

    def orderbook_for_stock(self, stock):
        """Get the orderbook for a particular stock.
        
        https://starfighter.readme.io/docs/get-orderbook-for-stock
        """
        url_fragment = 'venues/{venue}/stocks/{stock}'.format(
            venue=self.venue,
            stock=stock,
        )
        url = urlparse.urljoin(self.base_url, url_fragment)
        return requests.get(url).json()


    def place_new_order(self, stock, price, qty, direction, order_type):
        """Place an order for a stock.

        https://starfighter.readme.io/docs/place-new-order
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/orders'.format(
            venue=self.venue,
            stock=stock,
        )
        data = {
          "account": self.account,
          "venue": self.venue,
          "stock": stock,
          "qty": qty,
          "direction": direction,
          "orderType": order_type,
        }
        url = urlparse.urljoin(self.base_url, url_fragment)
        resp = requests.post(url, data=data, headers=self.headers)
        try:
            return resp.json()
        except:
            import pdb; pdb.set_trace()

    def quote_for_stock(self, stock):
        """Get a quick look at the most recent trade information for a stock.

        https://starfighter.readme.io/docs/a-quote-for-a-stock
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/quote'.format(
            venue=self.venue,
            stock=stock,
        )
        url = urlparse.urljoin(self.base_url, url_fragment)
        return requests.get(url).json()

    def status_for_order(self, order_id, stock):
        """Status For An Existing Order

        https://starfighter.readme.io/docs/status-for-an-existing-order
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/orders/{order_id}'.format(
            venue=self.venue,
            stock=stock,
            order_id=order_id,
        )
        url = urlparse.urljoin(self.base_url, url_fragment)
        return requests.get(url).json()

    def cancel_order(self, order_id, stock):
        """Cancel An Order

        https://starfighter.readme.io/docs/cancel-an-order
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/orders/{order_id}'.format(
            venue=self.venue,
            stock=stock,
            order_id=order_id,
        )
        url = urlparse.urljoin(self.base_url, url_fragment)
        return requests.delete(url, headers=self.headers).json()

    def status_for_all_orders(self):
        """Status for all orders

        https://starfighter.readme.io/docs/status-for-all-orders
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/accounts/{account}/orders'.format(
            venue=self.venue,
            account=self.account,
        )
        url = urlparse.urljoin(self.base_url, url_fragment)
        return requests.get(url).json()

    def status_for_all_orders_in_a_stock(self, stock):
        """Status for all orders in a stock

        https://starfighter.readme.io/docs/status-for-all-orders-in-a-stock
        """
        url_fragment = 'venues/{venue}/stocks/{stock}/accounts/{account}/stock/{stock}/orders'.format(
            stock=stock,
            venue=self.venue,
            account=self.account,
        )
        url = urlparse.urljoin(self.base_url, url_fragment)
        return requests.get(url).json()
