#!/usr/bin/env python
import base64
import re


class ImageBase64:
    prefix_pattern = r'^data:image/[a-z]+;base64,'

    def __init__(self, data: bytes):
        pass

    @classmethod
    def is_base64(cls, b64_data: str):
        if re.match(cls.prefix_pattern, b64_data):
            return True
        return False

    @classmethod
    def remove_prefix(cls, b64_data: str):
        return re.sub(cls.prefix_pattern, '', b64_data)

    @classmethod
    def add_prefix(cls, b64_data: str, image_type: str):
        return f'data:image/{image_type};base64,{b64_data}'

    @classmethod
    def get_image_type(cls, b64_data: str):
        return re.match(cls.prefix_pattern, b64_data).group(0).split('/')[1].split(';')[0]


def encode_base64(binary_data):
    base64_encoded_data = base64.b64encode(binary_data)
    base64_message = base64_encoded_data.decode('utf-8')
    return base64_message


def decode_base64(base64_message):
    base64_bytes = base64_message.encode('utf-8')
    decoded_data = base64.decodebytes(base64_bytes)
    return decoded_data
