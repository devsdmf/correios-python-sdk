# -*- coding: utf-8 -*-

import unittest
from correios import Correios, ShippingRateResult, ShippingRateResultService
from correios.package import *

class TestCorreios(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_get_shipping_rates(self):
        pass

class ShippingRateResultTest(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_shipping_rate_result_with_success_service(self):
        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,0.3)
        
        services = [ShippingRateResultService(1234,2,10.0)]
        
        result = ShippingRateResult('10000000','30000000',package,services)
        
        self.assertFalse(result.has_errors())
    
    def test_create_shipping_rate_result_with_errored_service(self):
        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,0.3)

        services = [ShippingRateResultService(1234,2,10.0,error_code=-1,error_message='Test error')]

        result = ShippingRateResult('10000000','30000000',package,services)

        self.assertTrue(result.has_errors())

class ShippingRateResultServiceTest(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_shipping_rate_result_service_with_success(self):
        delivery_cost = 10.0
        in_hands_cost = 2.0
        delivery_notification_cost = 0.3
        declared_value_cost = 0.9

        service = ShippingRateResultService(
            code = 1234,
            days = 2,
            price = delivery_cost + in_hands_cost + delivery_notification_cost + declared_value_cost,
            in_hands_cost = in_hands_cost,
            delivery_notification_cost = delivery_notification_cost,
            declared_value_cost = declared_value_cost,
            home_delivery = True,
            saturday_delivery = True,
            error_code = 0,
            error_message = None,
            additional_information = None
        )

        self.assertTupleEqual(
            service.get_prices(),
            (delivery_cost,in_hands_cost,delivery_notification_cost,declared_value_cost)
        )
        self.assertTrue(service.is_home_delivery())
        self.assertTrue(service.is_saturday_delivery())
        self.assertTrue(service.is_success())
    
    def test_create_shipping_rate_result_service_with_errors(self):
        service = ShippingRateResultService(
            code = 1234,
            days = 2,
            price = 10.0,
            error_code = -20,
            error_message = 'Test error'
        )

        self.assertFalse(service.is_success())
