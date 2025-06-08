"""
Utility functions for test automation.
"""
import base64


def decode_base64(encoded_text):
    """
    Decode a base64 encoded string.
    
    Args:
        encoded_text (str): Base64 encoded string
        
    Returns:
        str: Decoded string
    """
    return base64.b64decode(encoded_text).decode('utf-8')
