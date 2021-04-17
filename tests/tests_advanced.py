import BetterString.Exceptions
from BetterString import *
# Tests for the errors

test_string = BetterString("This is an Better String")

try:
    test_string[12314232354325345]
except IndexError as IE:
    print(IE)

try:
    test_string[12312121212312:]
except IndexStartOutOfBoundError as ISOOB:
    print(ISOOB)

try:
    test_string.to_int()
except CannotConvertToError as CCTE:
    print(CCTE)

try:
    test_string.to_dict()
except CannotConvertToError as CCTE:
    print(CCTE)

try:
    test_string()
except StringNotCallable as SNC:
    print(SNC)

try:
    test_string.colorize("wrong color")
except ColorNotFoundError as CNFE:
    print(CNFE)