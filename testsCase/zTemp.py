"""import string
import random


def getAlphaNumericValue(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
"""
from utilites import commonUtil
print(commonUtil.getAlphaNumericValue())
