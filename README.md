# NG_BANKS

Python implementation of [ng-banks](https://github.com/BolajiOlajide/ng-banks).

## INSTALLATION

The package is available on Pypi for installation. To install simply run the command in your terminal

```sh
pip install ng_banks
```

The package contains two methods:

* `getBanks()`: this method is used to retrieve all the banks in the system.

* `getBank(slugOrCode)`: this method is used to retrieve a particular based on the parameter supplied. The parameter can either the be the slug of the bank or the bank code. For slugs or code that don't exist, this method returns None.

### USAGE

```sh
>>> from ng_banks import getBank, getBanks

>>> getBanks() # should print an array of banks

>>> getBank('GTB') # returns {'name': 'GUARANTY TRUST BANK PLC', 'code': '058', 'slug': 'GTB' }

>>> getBank('044') # returns {'name': 'ACCESS BANK PLC', 'code': '044', 'slug': 'ACC' },
```

### CONTRIBUTORS

This package is authored by Bolaji Olajide.
