# -*- coding: utf-8 -*-

import os
import unittest
from unittest.mock import patch
from correios import Correios, ShippingRateResult, ShippingRateResultService
from correios.package import *

RESOURCES_DIR = os.path.dirname(os.path.realpath(__file__)) + '/resources'

class MockResponse(object):
    def __init__(self, text):
        self.text = text

class MockRequests(object):
    
    def get_shipping_rates_single_service_success(url,payload):
        fname = 'mock_correios_get_shipping_rate_single_service_result_success.xml'
        with open(RESOURCES_DIR + '/' + fname,'r') as f:
            r = MockResponse(f.read())
        return r
    
    def get_shipping_rates_multiple_service_success(url,payload):
        fname = 'mock_correios_get_shipping_rate_multiple_service_result_success.xml'
        with open(RESOURCES_DIR + '/' + fname,'r') as f:
            r = MockResponse(f.read())
        return r

    def get_shipping_rates_single_service_error(url,payload):
        fname = 'mock_correios_get_shipping_rate_single_service_error.xml'
        with open(RESOURCES_DIR + '/' + fname,'r') as f:
            r = MockResponse(f.read())
        return r
    
    def get_shipping_rates_multiple_service_error(url,payload):
        fname = 'mock_correios_get_shipping_rate_multiple_service_error.xml'
        with open(RESOURCES_DIR + '/' + fname,'r') as f:
            r = MockResponse(f.read())
        return r
        

class TestCorreios(unittest.TestCase):

    def setUp(self):
        pass
    
    @patch('requests.get', new=MockRequests.get_shipping_rates_single_service_success)
    def test_correios_get_shipping_rates_single_service_success(self):
        correios = Correios()
        
        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,0.3)

        origin = '10000000'
        destination = '30000000'

        result = correios.get_shipping_rates(origin,destination,package,[Correios.SERVICE_PAC])

        self.assertFalse(result.has_errors())
        self.assertEqual(origin,result.origin)
        self.assertEqual(destination,result.destination)
    
    @patch('requests.get', new=MockRequests.get_shipping_rates_multiple_service_success)
    def test_correios_get_shipping_rates_multiple_service_success(self):
        correios = Correios()

        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,0.3)

        origin = '10000000'
        destination = '30000000'

        result = correios.get_shipping_rates(origin,destination,package,[Correios.SERVICE_PAC,Correios.SERVICE_SEDEX])

        self.assertFalse(result.has_errors())
        self.assertEqual(origin,result.origin)
        self.assertEqual(destination,result.destination)
    
    @patch('requests.get', new=MockRequests.get_shipping_rates_single_service_error)
    def test_correios_get_shipping_rates_single_service_errors(self):
        correios = Correios()

        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,0.3)

        origin = '10000000'
        destination = '30000000'

        result = correios.get_shipping_rates(origin,destination,package,[Correios.SERVICE_PAC])

        self.assertTrue(result.has_errors())
    
    @patch('requests.get', new=MockRequests.get_shipping_rates_multiple_service_error)
    def test_correios_get_shipping_rates_multiple_service_errors(self):
        correios = Correios()

        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,0.3)

        origin = '10000000'
        destination = '30000000'

        result = correios.get_shipping_rates(origin,destination,package,[Correios.SERVICE_PAC,Correios.SERVICE_SEDEX])

        self.assertTrue(result.has_errors())

    @patch('requests.get', new=MockRequests.get_shipping_rates_single_service_success)
    def test_correios_get_shipping_rates_single_service_success_with_contract(self):
        correios = Correios()
        correios.set_credentials('someuser','somepass')
        
        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,0.3)

        origin = '10000000'
        destination = '30000000'

        result = correios.get_shipping_rates(origin,destination,package,[Correios.SERVICE_PAC])

        self.assertFalse(result.has_errors())
        self.assertEqual(origin,result.origin)
        self.assertEqual(destination,result.destination)
    
    @patch('requests.get', new=MockRequests.get_shipping_rates_multiple_service_success)
    def test_correios_get_shipping_rates_multiple_service_success_with_contract(self):
        correios = Correios()
        correios.set_credentials('someuser','somepass')

        package = BoxPackage()
        package.add_item(1.0,2.0,3.0,0.3)

        origin = '10000000'
        destination = '30000000'

        result = correios.get_shipping_rates(origin,destination,package,[Correios.SERVICE_PAC,Correios.SERVICE_SEDEX])

        self.assertFalse(result.has_errors())
        self.assertEqual(origin,result.origin)
        self.assertEqual(destination,result.destination)

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
