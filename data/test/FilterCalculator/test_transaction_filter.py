from unittest import TestCase
from data.data_processing.FilterCalculator.transaction_filter import TransactionFilter
from utils import TestUtils

class TestTransactionFilter(TestCase):
    def setUp(self):
        self.utils = TestUtils()
        self.filter = TransactionFilter()
        self.test_data = self.utils.get_test_data(250)

    def test_volume_filter(self):
        threshold = 0.5
        period = 3
        result_one = self.filter.volume_filter(self.test_data, period, threshold)

        self.assertEqual(result_one['CompanyA'][4], True)

        threshold = 3
        period = 3
        result_two = self.filter.volume_filter(self.test_data, period, threshold)

        self.assertEqual(result_two['CompanyE'][4], False)


    def test_transaction_amount_filter(self):
        threshold = 0.5
        period = 3
        result_one = self.filter.transaction_amount_filter(self.test_data, period, threshold)
        self.assertEqual(result_one['CompanyA'][4], True)

        threshold = 3
        period = 3
        result_two = self.filter.transaction_amount_filter(self.test_data, period, threshold)
        self.assertEqual(result_two['CompanyE'][4], False)


    def test_turn_over_filter(self):
        threshold = 0.5
        period = 3
        result_one = self.filter.turn_over_filter(self.test_data, period, threshold)
        self.assertEqual(result_one['CompanyA'][4], True)

        threshold = 3
        period = 3
        result_two = self.filter.turn_over_filter(self.test_data, period, threshold)
        self.assertEqual(result_two['CompanyE'][4], False)


