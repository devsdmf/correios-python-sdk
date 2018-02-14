# -*- coding: utf-8 -*-

import re
import requests
import xml.etree.ElementTree

class CorporateCredentials(object):

    def __init__(self, user, password):
        self.user = user
        self.password = password

class Correios(object):

    SERVICE_SEDEX_RETAIL = '40010'
    SERVICE_SEDEX_A_COBRAR_RETAIL = '40045'
    SERVICE_SEDEX_10_RETAIL = '40215'
    SERVICE_SEDEX_HOJE_RETAIL = '40290'
    SERVICE_SEDEX = '04014'
    SERVICE_SEDEX_A_COBRAR = '04065'
    SERVICE_PAC_RETAIL = '41106'
    SERVICE_PAC = '04510'
    SERVICE_PAC_A_COBRAR = '04707'

    API_SHIPPING_RATE_ENDPOINT = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx'

    def __init__(self):
        self.credentials = None
    
    def set_credentials(self, user, password):
        self.credentials = CorporateCredentials(user,password)

    def get_shipping_rates(self, origin, destination, package, services, 
                           in_hands = False, declared_value = False, delivery_notification = False):
        payload = {
            'sCepOrigem': re.sub('\D','',origin),
            'sCepDestino': re.sub('\D','',destination),
            'nCdServico': ','.join(services),
            'sCdMaoPropria': 'S' if in_hands else 'N',
            'nVlValorDeclarado': float(declared_value) if declared_value else 0.0,
            'sCdAvisoRecebimento': 'S' if delivery_notification else 'N',
            'StrRetorno': 'XML'
        }

        if self.credentials is not None:
            payload.update({
                'nCdEmpresa': self.credentials.user,
                'sDsSenha': self.credentials.password
            })
        
        payload.update(package.api_format())
        response = requests.get(self.API_SHIPPING_RATE_ENDPOINT,payload)

        services = []
        root = xml.etree.ElementTree.fromstring(response.text)
        for service in root.findall('cServico'):
            services.append(ShippingRateResultService(
                code = service.find('Codigo').text,
                days = int(service.find('PrazoEntrega').text),
                price = float(service.find('Valor').text.replace(',','.')),
                in_hands_cost = float(service.find('ValorMaoPropria').text.replace(',','.')),
                delivery_notification_cost = float(service.find('ValorAvisoRecebimento').text.replace(',','.')),
                declared_value_cost = float(service.find('ValorValorDeclarado').text.replace(',','.')),
                home_delivery = True if service.find('EntregaDomiciliar').text == 'S' else False,
                saturday_delivery = True if service.find('EntregaSabado').text == 'S' else False,
                error_code = int(service.find('Erro').text),
                error_message = service.find('MsgErro').text,
                additional_information = service.find('obsFim').text
            ))
        
        return ShippingRateResult(origin,destination,package,services)


class ShippingRateResult(object):

    def __init__(self, origin, destination, package, services):
        self.origin = origin
        self.destination = destination
        self.package = package
        self.services = services
        self.errors = False

        for service in services:
            if not service.is_success():
                self.errors = True
    
    def has_errors(self):
        return self.errors

class ShippingRateResultService(object):
    
    def __init__(self, code, days, price, in_hands_cost = 0.0, delivery_notification_cost = 0.0, 
                declared_value_cost = 0.0, home_delivery = True, saturday_delivery = False, 
                error_code = 0, error_message = '', additional_information = None):
        self.code = code
        self.days = int(days)
        self.price = float(price)
        self.prices = (
            float(price - in_hands_cost - delivery_notification_cost - declared_value_cost),
            float(in_hands_cost),
            float(delivery_notification_cost),
            float(declared_value_cost)
        )
        self.home_delivery = home_delivery
        self.saturday_delivery = saturday_delivery
        self.error_code = int(error_code)
        self.error_message = error_message
        self.additional_information = additional_information
    
    def get_prices(self):
        return self.prices
    
    def is_home_delivery(self):
        return self.home_delivery
    
    def is_saturday_delivery(self):
        return self.saturday_delivery
    
    def is_success(self):
        return True if self.error_code == 0 else False
