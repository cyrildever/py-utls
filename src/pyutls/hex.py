
from typing import Optional


def from_hex(string: str) -> Optional[bytes]:
    """Builds some byte array from the passed hexadecimal string or None if not appropriate"""
    try:
        return bytes.fromhex(string)
    except:
        return None


def to_hex(barray: bytes) -> str:
    """Returns the hexadecimal representation of the passed byte array"""
    return ''.join('{:02x}'.format(x) for x in barray)
