import sys
from  financial_modeling_data.models.stock import Stock

import pytest
from unittest.mock import Mock, patch, PropertyMock


class Stock():
    payload = {
        'name' : 'AAPL'
    }    

    def test_stock_property(self):
        with patch('financial_modeling_data.models.stock.Stock.name', new_callable=PropertyMock) as mock_name:
            m = Mock()
            mock_name.return_value = 'AAPL'
            stock_ = Stock(m)
            print(stock_.name)
            mock_name.assert_called_once_with()

    def test_stock_name(self):
        sample_stock = Stock(payload)
        assert sample_stock.name == 'AAPL'


