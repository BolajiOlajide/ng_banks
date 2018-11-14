"""
Module for handling main operations of the ng_banks package.
"""

banks = [
    {'name': 'ACCESS BANK PLC', 'code': '044', 'slug': 'ACC', 'ussd_code': '*901#'},
    {'name': 'CITIBANK NIGERIA PLC', 'code': '023', 'slug': 'CBN', 'ussd_code': None},
    {'name': 'DIAMOND BANK PLC', 'code': '063', 'slug': 'DMB', 'ussd_code': '*710#'},
    {'name': 'ECOBANK NIGERIA PLC', 'code': '050', 'slug': 'EBN', 'ussd_code': '*326#'},
    {'name': 'ENTERPRISE BANK', 'code': '084', 'slug': 'EPB', 'ussd_code': '*901#'},
    {'name': 'FIDELITY BANK PLC', 'code': '070', 'slug': 'FDB', 'ussd_code': '*770#'},
    {'name': 'FIRST BANK NIGERIA LIMITED', 'code': '011', 'slug': 'FBN', 'ussd_code': '*894#'},
    {'name': 'FIRST CITY MONUMENT BANK PLC', 'code': '214', 'slug': 'FCB', 'ussd_code': '*329#'},
    {'name': 'GUARANTY TRUST BANK PLC', 'code': '058', 'slug': 'GTB', 'ussd_code': '*737#'},
    {'name': 'HERITAGE BANK PLC', 'code': '030', 'slug': 'HTB', 'ussd_code': '*322#'},
    {'name': 'KEY STONE BANK', 'code': '082', 'slug': 'KSB', 'ussd_code': '*533#'},
    {'name': 'MAINSTREET BANK', 'code': '014', 'slug': 'MSB', 'ussd_code': None},
    {'name': 'POLARIS BANK LIMITED', 'code': '076', 'slug': 'PLB', 'ussd_code': None},
    {'name': 'PROVIDUS BANK LIMITED', 'code': '101', 'slug': 'PVB', 'ussd_code': None},
    {'name': 'STANBIC IBTC BANK LTD', 'code': '221', 'slug': 'SIB', 'ussd_code': '*909#'},
    {
        'name': 'STANDARD CHARTERED BANK NIGERIA LTD',
        'code': '068', 'slug': 'SCB', 'ussd_code': None
    },
    {'name': 'STERLING BANK PLC', 'code': '232', 'slug': 'STB', 'ussd_code': '*822#'},
    {'name': 'SUNTRUST BANK NIGERIA LTD', 'code': '100', 'slug': 'SBN', 'ussd_code': None},
    {'name': 'UNION BANK OF NIGERIA PLC', 'code': '032', 'slug': 'UBN', 'ussd_code': '*826#'},
    {'name': 'UNITED BANK FOR AFRICA PLC', 'code': '033', 'slug': 'UBA', 'ussd_code': '*919#'},
    {'name': 'UNITY BANK PLC', 'code': '215', 'slug': 'UNB', 'ussd_code': '*7799#'},
    {'name': 'WEMA BANK PLC', 'code': '035', 'slug': 'WEM', 'ussd_code': '*945#'},
    {'name': 'ZENITH BANK PLC', 'code': '057', 'slug': 'ZIB', 'ussd_code': '*966#'}
]


def getBanks():
    """ Method to return all the banks in Nigeria. """
    return banks


def getBank(_param):
    """Method to retreive a certain bank by slug or code.

    Args:
        _param: parameter to be used to search for the bank, this can either
                be the slug or the code.
    """
    param = str(_param)
    isCode = param.isdigit()

    if isCode:
        queryType = 'code'
    else:
        queryType = 'slug'
    try:
        bank = [bank for bank in banks if bank[queryType] == param]
        return bank[0]
    except IndexError:
        return None

def addBank(name, code, slug, ussd_code=None):
    
    for index, bank in enumerate(banks):
        if bank['code'] == code or bank['slug'] == slug:
            raise Exception('Bank Already Exists With This Code or Slug')
    bank = {'name': name.upper(), 'code':code, 'slug':slug, 'ussd_code':ussd_code}
    banks.append(bank)
    return bank