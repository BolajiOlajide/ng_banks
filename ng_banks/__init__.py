"""
Module for handling main operations of the ng_banks package.
"""

banks = [
  { 'name': 'ACCESS BANK PLC', 'code': '044', 'slug': 'ACC' },
  { 'name': 'CITIBANK NIGERIA PLC', 'code': '023', 'slug': 'CBN' },
  { 'name': 'DIAMOND BANK PLC', 'code': '063', 'slug': 'DMB' },
  { 'name': 'ECOBANK NIGERIA PLC', 'code': '050', 'slug': 'EBN' },
  { 'name': 'ENTERPRISE BANK', 'code': '084', 'slug': 'EPB' },
  { 'name': 'FIDELITY BANK PLC', 'code': '070', 'slug': 'FDB' },
  { 'name': 'FIRST BANK NIGERIA LIMITED', 'code': '011', 'slug': 'FBN' },
  { 'name': 'FIRST CITY MONUMENT BANK PLC', 'code': '214', 'slug': 'FCB' },
  { 'name': 'GUARANTY TRUST BANK PLC', 'code': '058', 'slug': 'GTB' },
  { 'name': 'HERITAGE BANK PLC', 'code': '030', 'slug': 'HTB' },
  { 'name': 'KEY STONE BANK', 'code': '082', 'slug': 'KSB' },
  { 'name': 'MAINSTREET BANK', 'code': '014', 'slug': 'MSB' },
  { 'name': 'POLARIS BANK LIMITED', 'code': '076', 'slug': 'PLB' },
  { 'name': 'PROVIDUS BANK LIMITED', 'code': '101', 'slug': 'PVB' },
  { 'name': 'STANBIC IBTC BANK LTD', 'code': '221', 'slug': 'SIB' },
  { 'name': 'STANDARD CHARTERED BANK NIGERIA LTD', 'code': '068', 'slug': 'SCB' },
  { 'name': 'STERLING BANK PLC', 'code': '232', 'slug': 'STB' },
  { 'name': 'SUNTRUST BANK NIGERIA LTD', 'code': '100', 'slug': 'SBN' },
  { 'name': 'UNION BANK OF NIGERIA PLC', 'code': '032', 'slug': 'UBN'},
  { 'name': 'UNITED BANK FOR AFRICA PLC', 'code': '033', 'slug': 'UBA' },
  { 'name': 'UNITY BANK PLC', 'code': '215', 'slug': 'UNB' },
  { 'name': 'WEMA BANK PLC', 'code': '035', 'slug': 'WEM' },
  { 'name': 'ZENITH BANK PLC', 'code': '057', 'slug': 'ZIB' }
];


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

