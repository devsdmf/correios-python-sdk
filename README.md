# Correios Python SDK

[![Build Status](https://travis-ci.org/devsdmf/correios-python-sdk.svg?branch=master)](https://travis-ci.org/devsdmf/correios-python-sdk)
[![Coverage Status](https://coveralls.io/repos/github/devsdmf/correios-python-sdk/badge.svg?branch=master)](https://coveralls.io/github/devsdmf/correios-python-sdk?branch=master)

This is another unofficial Correios SDK for Python projects, that brings a concise and easy-to-use API, implementing the validations described in the Correios specification documents.

Currently the only supported task is the shipping price calculator, but feel free to contribute with new endpoints/APIs.

## Requirements

- Python 3.3+

## Installation

### From PyPi
```
$ pip install correios-python-sdk
```

### From source
```
$ git clone git@github.com:devsdmf/correios-python-sdk.git && cd correios-python-sdk
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

### Shipping Calculator API

Correios accepts three distinct types of packages: box, cylinder and envelope. And for each kind of package we have a specific model that implements some methods to calculate and validate dimensions and weight.

#### Box Package
```python
from correios.package import BoxPackage

box = BoxPackage()
box.add_item(height=10.0,width=25.0,depth=30.0,weight=0.6)
```

#### Cylinder Package
```python
from correios.package import CylinderPackage

cylinder = CylinderPackage()
cylinder.add_item(length=50.0,diameter=20.0,weight=3.0)
```

#### Envelope Package
```python
from correios.package import EnvelopePackage

envelope = EnvelopePackage()
envelope.add_item(width=10.0,length=25.0,weight=0.3)
```

#### Getting shipping rates for package

With a package object you can get the shipping rates from the Correios API using the method available in Correios class:

```python
from correios import Correios
from correios.package import BoxPackage

package = BoxPackage()
package.add_item(height=10.0,width=25.0,depth=30.0,weight=0.6)

correios = Correios()
result = correios.get_shipping_rates(
    origin='10000-000',
    destination='30000-000',
    package=package,
    ervices=[
        Correios.SERVICE_PAC,
        Correios.SERVICE_SEDEX
    ]
)

if not result.has_errors():
    for service in result.services:
        code = service.code
        days = service.days
        price = service.price
        print('The service {} will took {} days to delivery at the cost of ${}'.format(code,days,price))
else:
    for service in result.services:
        code = service.code
        error = service.error_code
        message = service.error_message
        print('The service {} returned the error {} with message: '.format(code,error,message))
```

## Documentation

Soon

## Tests

```
$ python setup.py test
```

## License

This library is licensed under the [MIT license](LICENSE).
