import base64
import collections
import json
import ntpath
import os
import zlib
from datetime import datetime
from random import random

import requests
import urllib
from urllib.parse import urlencode

import logging
import uuid
from typing import Union, List, Tuple

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

from dropbox import dropbox as dbx

""" ---------- FUNCTIONS ----------- """


# General Functions #
def _separate_with_and_without(items: List, attribute_name: str) -> Tuple[List, List]:
    """
    Split a list of items into those with a specific attribute and those without
    :param items: List of items
    :param attribute_name: Name of attribute to look for
    :return: list_with, list_without
    """
    items_with = []
    items_without = []
    for item in items:
        if object_has_attribute(obj=item, attribute_name=attribute_name):
            items_with.append(item)
        else:
            items_without.append(item)
    return items_with, items_without


# Files #
def split_file_path(file_path):
    return '/'.join(file_path.split('/')[:-1])


def make_path(file_path):
    working_path = split_file_path(file_path)
    if not os.path.exists(working_path):
        os.makedirs(working_path)


def write_to_file(text, filename, write_mode: str = "w+"):
    make_path(filename)
    f = open(filename, write_mode)
    f.write(text)
    f.close()


def read_from_file(filename, read_mode: str = 'r'):
    with open(filename, read_mode) as f:
        text = f.read()
    return text


def backup_file(filename, suffix: str = ".bk"):
    copy_file(filename, f'{filename}{suffix}')


def copy_file(filename, new_filename):
    text = read_from_file(filename)
    write_to_file(text=text, filename=new_filename)


# UUIDs #
def time_uuid():
    return uuid.uuid1()


def random_uuid():
    return uuid.uuid4()


def generate_uuid(use_random: bool = False):
    if use_random:
        return random_uuid()
    return time_uuid()


# Dictionaries #
def dict_to_json(dictionary: dict) -> json:
    """
    Convert a dictionary to valid JSON
    :param dictionary: Dictionary to convert
    :return: JSON representation of dictionary
    """
    return json.dumps(dictionary)


def combine_dictionaries(old_dictionary: dict, new_dictionary: dict, add_new_items: bool = False) -> dict:
    """
    Build a complete dictionary, overwriting values in old dictionary with values in new dictionary
    :param old_dictionary: Original (base) dictionary
    :param new_dictionary: New (updated values) dictionary
    :param add_new_items: If a new item is found in the new dictionary that is not present in the old dictionary,
    include it in the final dictionary. Otherwise, ignore it. (Default: False)
    :return: A dictionary
    """
    for k, v in new_dictionary.items():
        if k in old_dictionary.keys() or add_new_items:
            old_dictionary[k] = v
    return old_dictionary


def dictionary_is_complete(check_dictionary: dict, template_dictionary: dict, ignore_keys: List = []) -> bool:
    """
    Check that all keys in the template dictionary are present in the check_dictionary
    :param check_dictionary: Dictionary to parse
    :param template_dictionary: Dictionary to use for verification
    :param ignore_keys: List of keys to ignore when checking (Optional)
    :return: True if valid, False if not valid
    """
    for k in template_dictionary.keys():
        if k in ignore_keys or k in check_dictionary.keys():
            pass
        else:
            return False
    return True


# Checks #
def object_has_attribute(obj: object, attribute_name: str) -> bool:
    """
    Check if an object has an attribute (exists and is not None)
    :param obj: object to check
    :param attribute_name: name of attribute to find
    :return: True if exists and is not None, False otherwise
    """
    if hasattr(obj, attribute_name):
        if getattr(obj, attribute_name) is not None:
            return True
    return False


# Time Functions #
def remove_time_from_date(date_string: Union[datetime, str]) -> str:
    """
    Remove time, i.e. 00:00:00, from a datetime.datetime or string
    :param date_string: datetime.datetime object or string to convert
    :return: str without time, i.e. 2020-08-29
    """
    if type(date_string) == str:
        date_string = string_to_datetime(date_string=date_string)
    return date_string.strftime("%Y-%m-%d")


def get_year_from_date(date_string: Union[datetime, str]) -> int:
    """
    Extract year from a datetime.datetime or string
    :param date_string: datetime.datetime object or string
    :return: int of year, i.e. 2020
    """
    if type(date_string) == str:
        date_string = string_to_datetime(date_string=date_string)
    return int(date_string.strftime("%Y"))


def string_to_datetime(date_string: str, template: str = "%Y-%m-%dT%H:%M:%S") -> datetime:
    """
    Convert a string to a datetime.datetime object
    :param date_string: datetime string to convert
    :param template: (Optional) datetime template to use when parsing string (Default: "%Y-%m-%dT%H:%M:%S")
    :return: datetime.datetime object
    """
    if date_string.endswith('Z'):
        date_string = date_string[:-5]
    return datetime.strptime(date_string, template)


def datetime_to_string(datetime_object: datetime, template: str = "%Y-%m-%dT%H:%M:%S.000Z") -> str:
    """
    Convert a datetime.datetime object to a string
    :param datetime_object: datetime.datetime object to convert
    :param template: (Optional) datetime template to use when parsing string
    :return: str representation of datetime
    """
    return datetime_object.strftime(template)


def adjust_datetime_for_timezone(local_time: datetime) -> datetime:
    """
    Shift datetime.datetime in regards to UTC time
    :param local_time: local time datetime.datetime object
    :return: Shifted datetime.datetime object
    """
    difference = datetime.now() - datetime.utcnow()
    return local_time - difference


def hours_difference_in_timezone() -> int:
    """
    Get the hours difference between local and UTC time
    :return: int number of hours
    """
    return int((datetime.utcnow() - datetime.now()).total_seconds() / 60 / 60)


def get_nearest_30_minute_mark(time_format: str = "%Y-%m-%dT%H:%M:%S.000Z") -> str:
    """
    Get the most recently past hour or half-hour time
    :param time_format: (Optional) Format of timestamp (Default: "%Y-%m-%dT%H:%M:%S.000Z")
    :return: str of datetime
    """
    now = datetime.utcnow()
    if now.minute >= 30:
        now = now.replace(second=0, microsecond=0, minute=30)
    else:
        now = now.replace(second=0, microsecond=0, minute=0)
    return now.strftime(time_format)


def get_milliseconds_between_two_hours(start_hour: int, end_hour: int) -> int:
    """
    Get how many milliseconds between two 24-hour hours
    :param start_hour: starting hour (in 24-hour time)
    :param end_hour: ending hour (in 24-hour time)
    :return: int of milliseconds between the two hours
    """
    start_date = datetime(2020, 1, 1, start_hour, 0)
    if end_hour < start_hour:
        end_date = datetime(2020, 1, 2, end_hour, 0)
    else:
        end_date = datetime(2020, 1, 1, end_hour, 0)
    return int((end_date - start_date).total_seconds()) * 1000


def get_milliseconds_between_two_datetimes(start_datetime: datetime, end_datetime: datetime) -> int:
    """
    Get how many milliseconds between two datetime.datetime objects
    :param start_datetime: starting datetime.datetime object
    :param end_datetime: ending datetime.datetime object
    :return: int of milliseconds between the two datetime.datetime objects
    """
    return int((end_datetime - start_datetime).total_seconds()) * 1000


# Random #
def random_choice(items: List):
    """
    Get a random item from a list
    :param items: list of items
    :return: random item
    """
    return random.choice(items)


def random_with_attributes(items: List, attributes: List[str], attempts: int = 10) -> Union[object, None]:
    """
    Pick a random object with given attribute from a list
    Returns None after X failed attempts
    :param items: List of objects
    :param attributes: List of attributes to check for
    :param attempts: How many times to retry before returning None
    :return: Either a matching random object or None
    """
    if attempts == 0:
        return None
    temp_choice = random_choice(items)
    for attribute in attributes:
        if not object_has_attribute(temp_choice, attribute_name=attribute):
            return random_with_attributes(items=items, attributes=attributes, attempts=attempts - 1)
    return temp_choice


# Sorting #
def shuffle(items: List) -> bool:
    """
    Randomize the order of the items in a list in-place
    :param items: list of items to shuffle
    :return: True if successful, False if unsuccessful
    """
    try:
        random.shuffle(items)
        return True
    except:
        pass
    return False


def rotate_items(items: List, shift_index: int = None) -> List:
    """
    Rotate items in a list by a specific number of steps
    :param items: list of items
    :param shift_index: Optional index to shift list by. Otherwise random
    :return: rotated list of items
    """
    if not shift_index:
        shift_index = random.randint(0, len(items) - 1)
    collection_list = collections.deque(items)
    collection_list.rotate(shift_index)
    return list(collection_list)


def remove_duplicates(items: List) -> List:
    """
    Remove duplicate items from a list
    "Duplicate" objects must be exactly the same (all attributes)
    :param items: list of items to parse
    :return: list of filtered items
    """
    return list(set(items))


def remove_duplicates_by_attribute(items: List, attribute_name: str) -> List:
    """
    Remove duplicate items from a list, comparing on a specific attribute
    :param items: list of items to parse
    :param attribute_name: name of attribute to check by
    :return: list of filtered items
    """
    filtered = []
    filtered_attr = []
    for item in items:
        attr = getattr(item, attribute_name)
        if attr not in filtered_attr:
            filtered.append(item)
            filtered_attr.append(attr)
    return filtered


# Logging #
need_to_config_logs = True


def info(message):
    logging.info(msg=message)


def error(message):
    logging.error(msg=message)


def warning(message):
    logging.warning(msg=message)


level_map = {
    'info': info,
    'error': error,
    'warning': warning
}


def log(message: str, level: str = "info") -> None:
    """
    Log a message if verbose is enabled.
    :param message: Message to log
    :param level: info, error or warning
    """
    if level not in level_map.keys():
        level = 'info'
    level_map[level](message)


class Logs:
    def __init__(self, message_format: str = '%(asctime)s %(levelname)s:%(message)s', verbose: bool = False):
        global need_to_config_logs
        if need_to_config_logs:
            logging.basicConfig(format=message_format,
                                level=(logging.INFO if verbose else logging.ERROR))
            need_to_config_logs = False


# HTTP Requests #
def http_get(url: str,
             params: dict = None,
             headers: dict = None,
             timeout: int = 2,
             log_level: str = None) -> Union[requests.Response, None]:
    _ = Logs()
    if params:
        url += f"?{urlencode(params)}"
    try:
        res = requests.get(url=url, headers=headers, timeout=timeout)
        if log_level:
            log(message=f"GET {url}", level=log_level)
            log(message=f"Response: {res}", level=("error" if not res else log_level))
        return res
    except requests.exceptions.Timeout:
        return None


def http_post(url: str,
              params: dict = None,
              headers: dict = None,
              data: dict = None,
              timeout: int = 2,
              log_level: str = None) -> Union[requests.Response, None]:
    _ = Logs()
    if params:
        url += f"?{urlencode(params)}"
    try:
        res = requests.post(url=url, json=data, headers=headers, timeout=timeout)
        if log_level:
            log(message=f"POST {url}, Body: {data}", level=log_level)
            log(message=f"Response: {res}", level=("error" if not res else log_level))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None


def http_put(url: str,
             params: dict = None,
             headers: dict = None,
             data: dict = None,
             timeout: int = 2,
             log_level: str = None) -> Union[requests.Response, None]:
    _ = Logs()
    if params:
        url += f"?{urlencode(params)}"
    try:
        res = requests.put(url=url, json=data, headers=headers, timeout=timeout)
        if log_level:
            log(message=f"PUT {url}, Body: {data}", level=log_level)
            log(message=f"Response: {res}", level=("error" if not res else log_level))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None


def http_delete(url: str,
                params: dict = None,
                headers: dict = None,
                data: dict = None,
                timeout: int = 2,
                log_level: str = None) -> Union[requests.Response, None]:
    _ = Logs()
    if params:
        url += f"?{urlencode(params)}"
    try:
        res = requests.delete(url=url, json=data, headers=headers, timeout=timeout)
        if log_level:
            log(message=f"DELETE {url}, Body: {data}", level=log_level)
            log(message=f"Response: {res}", level=("error" if not res else log_level))
        return res
        # use json= rather than data= to convert single-quoted dict to double-quoted JSON
    except requests.exceptions.Timeout:
        return None


# Pastebin #
pastebin_expiration_options = ["5min", "10min", "1hour", "1day", "1week", "1month", "1year", "never"]


def _json_encode(d):
    return json.dumps(d, separators=(',', ':')).encode('utf-8')


def _base58_encode(v):
    # 58 char alphabet
    alphabet = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    alphabet_len = len(alphabet)

    if isinstance(v, str) and not isinstance(v, bytes):
        v = v.encode('ascii')

    nPad = len(v)
    v = v.lstrip(b'\0')
    nPad -= len(v)

    l = 0
    for (i, c) in enumerate(v[::-1]):
        if isinstance(c, str):
            c = ord(c)
        l += c << (8 * i)

    string = b''
    while l:
        l, idx = divmod(l, alphabet_len)
        string = alphabet[idx:idx + 1] + string

    return (alphabet[0:1] * nPad + string)


#
# The encryption format is described here:
# https://github.com/PrivateBin/PrivateBin/wiki/Encryption-format
#
def _privatebin_encrypt(paste_passphrase,
                        paste_password,
                        paste_plaintext,
                        paste_formatter,
                        paste_attachment_name,
                        paste_attachment,
                        paste_compress,
                        paste_burn,
                        paste_opendicussion):
    if paste_password:
        paste_passphrase += bytes(paste_password, 'utf-8')

    # PBKDF
    # kdf_salt = get_random_bytes(8)
    kdf_salt = bytes(os.urandom(8))
    kdf_iterations = 100000
    kdf_keysize = 256  # size of resulting kdf_key

    backend = default_backend()
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=int(kdf_keysize / 8),  # 256bit
                     salt=kdf_salt,
                     iterations=kdf_iterations,
                     backend=backend)
    kdf_key = kdf.derive(paste_passphrase)

    # AES-GCM
    adata_size = 128

    # cipher_iv = get_random_bytes(int(adata_size / 8))
    cipher_iv = bytes(os.urandom(int(adata_size / 8)))
    cipher_algo = "aes"
    cipher_mode = "gcm"

    compression_type = "none"
    if paste_compress:
        compression_type = "zlib"

    # compress plaintext
    paste_data = {'paste': paste_plaintext}
    if paste_attachment_name and paste_attachment:
        paste_data['attachment'] = paste_attachment
        paste_data['attachment_name'] = paste_attachment_name
        print(paste_attachment_name)
        print(paste_attachment)

    if paste_compress:
        zobj = zlib.compressobj(wbits=-zlib.MAX_WBITS)
        paste_blob = zobj.compress(_json_encode(paste_data)) + zobj.flush()
    else:
        paste_blob = _json_encode(paste_data)

    # Associated data to authenticate
    paste_adata = [
        [
            base64.b64encode(cipher_iv).decode("utf-8"),
            base64.b64encode(kdf_salt).decode("utf-8"),
            kdf_iterations,
            kdf_keysize,
            adata_size,
            cipher_algo,
            cipher_mode,
            compression_type,
        ],
        paste_formatter,
        int(paste_opendicussion),
        int(paste_burn),
    ]

    paste_adata_json = _json_encode(paste_adata)

    aesgcm = AESGCM(kdf_key)
    ciphertext = aesgcm.encrypt(cipher_iv, paste_blob, paste_adata_json)

    # Validate
    # aesgcm.decrypt(cipher_iv, ciphertext, paste_adata_json)

    paste_ciphertext = base64.b64encode(ciphertext).decode("utf-8")

    return paste_adata, paste_ciphertext


def _privatebin_send(paste_url,
                     paste_password,
                     paste_plaintext,
                     paste_formatter,
                     paste_attachment_name,
                     paste_attachment,
                     paste_compress,
                     paste_burn,
                     paste_opendicussion,
                     paste_expire):
    paste_passphrase = bytes(os.urandom(32))
    # paste_passphrase = get_random_bytes(32)

    paste_adata, paste_ciphertext = _privatebin_encrypt(paste_passphrase,
                                                        paste_password,
                                                        paste_plaintext,
                                                        paste_formatter,
                                                        paste_attachment_name,
                                                        paste_attachment,
                                                        paste_compress,
                                                        paste_burn,
                                                        paste_opendicussion)

    # json payload for the post API
    # https://github.com/PrivateBin/PrivateBin/wiki/API
    payload = {
        "v": 2,
        "adata": paste_adata,
        "ct": paste_ciphertext,
        "meta": {
            "expire": paste_expire,
        }
    }

    # http content type
    headers = {'X-Requested-With': 'JSONHttpRequest'}

    r = requests.post(paste_url,
                      data=_json_encode(payload),
                      headers=headers)
    r.raise_for_status()

    try:
        result = r.json()
    except:
        return False, 'Error parsing JSON: {}'.format(r.text)

    paste_status = result['status']
    if paste_status:
        paste_message = result['message']
        return False, "Error getting status: {}".format(paste_message)

    paste_id = result['id']
    paste_url_id = result['url']
    paste_deletetoken = result['deletetoken']

    return {'url': '{}{}#{}'.format(paste_url, paste_url_id, _base58_encode(paste_passphrase).decode("utf-8")),
            'delete': '{}/?pasteid={}&deletetoken={}'.format(paste_url, paste_id, paste_deletetoken)}, None


def privatebin(text, url: str = 'https://privatebin.net', pass_protect=False, expiration='never',
               burn_after_reading=False):
    paste_url = url
    paste_formatter = 'plaintext'
    paste_compress = True
    paste_opendicussion = 0
    paste_burn = 0
    paste_password = None
    paste_attachment_name = None
    paste_attachment = None

    if not text:
        return False, "You did not provide any text to send to {}".format(url)

    if expiration not in pastebin_expiration_options:
        return False, "Incorrect how_long option. Options: '{}'".format("', '".join(pastebin_expiration_options))

    if burn_after_reading:
        paste_burn = 1

    if pass_protect:
        paste_password = pass_protect

    return _privatebin_send(paste_url,
                            paste_password,
                            text,
                            paste_formatter,
                            paste_attachment_name,
                            paste_attachment,
                            paste_compress,
                            paste_burn,
                            paste_opendicussion,
                            expiration)


def hastebin(text, url: str = 'https://hastebin.com'):
    try:
        post = requests.post('{}/documents'.format(url), data=text.encode('utf-8'))
        data = {'url': '{}/{}'.format(url, post.json()['key'])}
        return data, None
    except Exception as e:
        print(e)
        return None, e


""" --------- CLASSES ------------- """


# GPG Keys #
class GPG:
    import pgp

    def __init__(self, key_server: str = "hkp://pgp.key-server.io/"):
        self.server = key_server

    def search(self, search_string: str):
        return pgp.keyserver.get_keyserver(self.server).search(search_string)


# SQL Functions #
class SQL:
    import sqlite3
    from pysqlcipher3 import dbapi2 as sqlcipher
    import mysql.connector
    import pyodbc

    def __init__(self,
                 sql_type: str,
                 server_ip: str = None,
                 database_name: str = None,
                 username: str = None,
                 password: str = None,
                 use_Active_Directory: bool = False,
                 sqlite_file: str = None,
                 encryption_key: str = None):
        self.SQL_TYPE = sql_type
        self.SERVER_IP = server_ip
        self.DATABASE_NAME = database_name
        self.USERNAME = username
        self.PASSWORD = password
        self.USE_ACTIVE_DIRECTORY = use_Active_Directory
        self.SQLITE_FILE = sqlite_file
        self.KEY = encryption_key
        self._requirements_check()

    def _requirements_check(self):
        if self.SQL_TYPE not in ['MySQL', 'SQLite', 'SQLCipher', 'MSSQL']:
            raise Exception("Not a valid sql_type.")
        if self.SQL_TYPE in ['SQLite', 'SQLCipher']:
            if not self.SQLITE_FILE:
                raise Exception("Please provide an SQLite or SQLCipher file.")
        if self.SQL_TYPE == 'SQLCipher':
            if not self.KEY and self.PASSWORD:
                self.KEY = self.PASSWORD
            if not self.KEY:
                raise Exception("Missing key to unlock encrypted database.")
        if self.SQL_TYPE in ['MySQL', 'MSSQL']:
            if not (self.SERVER_IP and self.DATABASE_NAME):
                raise Exception("Please provide a server IP address and a database name.")
        if self.SQL_TYPE == 'MySQL':
            if not (self.USERNAME and self.PASSWORD):
                raise Exception("Please provide a username and password.")
        if self.SQL_TYPE == 'MSSQL':
            if not ((self.USERNAME and self.PASSWORD) or self.USE_ACTIVE_DIRECTORY):
                raise Exception("Please use either username/password or Active Directory.")

    def _get_connection(self):
        db = None
        if self.SQL_TYPE == 'SQLite':
            db = sqlite3.connect(self.SQLITE_FILE)
        elif self.SQL_TYPE == 'SQLCipher':
            db = sqlcipher.connect(self.SQLITE_FILE)
            db.execute(f'pragma key="{self.KEY}"')
        elif self.SQL_TYPE == 'MySQL':
            db = mysql.connector.connect(user=self.USERNAME, password=self.PASSWORD, host=self.SERVER_IP,
                                         database=self.DATABASE_NAME)
        elif self.SQL_TYPE == 'MSSQL':
            db = pyodbc.connect(f'DRIVER={{/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.2.1}};'
                                f'SERVER={self.SERVER_IP};'
                                f'DATABASE={self.DATABASE_NAME};'
                                f'UID={self.USERNAME};'
                                f'PWD={self.PASSWORD}')
        return db

    def use_sql_locally(self):
        """
        Pass SQL instance over.
        :return:
        """
        return self._get_connection()

    def custom_query(self,
                     queries: [],
                     commit: bool = False):
        conn = self._get_connection()
        if conn:
            cur = conn.cursor()
            for query in queries:
                cur.execute(query)
            results = cur.fetchall()
            if commit:
                results = cur.rowcount()
                conn.commit()
            cur.close()
            conn.close()
            return results
        else:
            raise Exception("Couldn't connect to the database.")


# Google Analytics #
def make_GA_url(params_dict):
    base_url = "https://www.google-analytics.com/collect"
    args = urllib.parse.urlencode(params_dict)
    return f"{base_url}?{args}"


class GoogleAnalytics:
    def __init__(self,
                 analytics_id: str,
                 anonymous_ip: bool = False,
                 do_not_track: bool = False):
        self.analytics_id = analytics_id
        self.version = '1'
        self.anonymize_ip = anonymous_ip
        self.do_not_track = do_not_track

    def _send(self, final_params):
        if self.do_not_track:
            return True
        url = make_GA_url(params_dict=final_params)
        if http_post(url=url):
            return True
        return False

    def event(self,
              event_category: str,
              event_action: str,
              event_label: str = None,
              event_value: int = None,
              user_id: str = None,
              anonymize_ip: bool = False,
              random_uuid_if_needed: bool = False):
        if self.do_not_track:
            return True
        if not user_id:
            user_id = str(generate_uuid(use_random=random_uuid_if_needed))
        final_params = {'v': self.version, 'tid': self.analytics_id, 't': 'event', 'cid': user_id}
        if anonymize_ip or self.anonymize_ip:
            final_params['aip'] = 0
        final_params['ec'] = event_category
        final_params['ea'] = event_action
        if event_label:
            final_params['el'] = event_label
        if event_value:
            final_params['ev'] = event_value
        return self._send(final_params=final_params)

    def pageview(self,
                 visited_page: str,
                 page_title: str = None,
                 user_id: str = None,
                 anonymize_ip: bool = False,
                 random_uuid_if_needed: bool = False):
        if self.do_not_track:
            return True
        if not user_id:
            user_id = str(generate_uuid(use_random=random_uuid_if_needed))
        final_params = {'v': self.version, 'tid': self.analytics_id, 't': 'pageview', 'cid': user_id}
        if anonymize_ip or self.anonymize_ip:
            final_params['aip'] = 0
        if not visited_page.startswith('/'):
            visited_page = f"/{visited_page}"
        final_params['dl'] = visited_page
        if page_title:
            final_params['dt'] = page_title
        return self._send(final_params=final_params)


# Dropbox #
class Dropbox:
    def __init__(self, api_key: str):
        self.db = dbx.Dropbox(api_key)

    def download_file(self, filePath, toWhere=None) -> bool:
        try:
            if toWhere:
                self.db.files_download_to_file(f'/{filePath}', toWhere)
            else:
                self.db.files_download('/{}'.format(filePath))
            return True
        except FileNotFoundError:
            pass
        return False

    def upload_file(self, filePath, rename=False) -> bool:
        try:
            with open(filePath, 'rb') as f:
                print("Uploading {} to Dropbox...".format(filePath))
                if not rename:
                    filename = ntpath.basename(filePath)
                self.db.files_upload(f.read(), f'/{(rename if rename else filename)}',
                                     mode=dbx.files.WriteMode('overwrite'))
            return True
        except:
            pass
        return False

    def check_if_folder_exists(self, folderPath) -> bool:
        try:
            self.db.files_get_metadata(f'/{folderPath}')
            return True
        except:
            pass
        return False

    def create_folder_path(self, folderPath) -> bool:
        """
        Ex. Create /home/2020/Spring folders
        """
        try:
            folders = folderPath.split('/')
            from_root = ""
            for folder in folders:
                if not self.check_if_folder_exists(f"{from_root}{folder}"):
                    self.db.files_create_folder_v2(f"/{from_root}{folder}")
                from_root += folder + "/"
            return True
        except:
            pass
        return False


# Encryption (Fernet) #
def get_raw_fernet_key(key_file):
    return read_from_file(key_file)


def get_fernet_key_from_file(key_file):
    """
    WARNING: New key will be made (and potentially overwrite old file) if key cannot be loaded
    """
    try:
        key = read_from_file(key_file)
    except:
        key = make_fernet_key()
        save_fernet_key(key, key_file)
    return Fernet(key)


def make_fernet_key():
    return Fernet.generate_key()


def save_fernet_key(key, filename):
    write_to_file(text=key.decode('utf-8'), filename=filename)


class Encryption:
    def __init__(self, key: Fernet = None, key_file: str = None):
        self.key = key
        self.key_file = key_file
        if not key:
            if not key_file:
                self.key = make_fernet_key()
            else:
                self.key = get_fernet_key_from_file(key_file)

    def encrypt_text(self, text):
        token = self.key.encrypt(bytes(text, encoding='utf8'))
        return token.decode('utf-8')

    def decrypt_text(self, text):
        text = self.key.decrypt(bytes(text, encoding='utf8'))
        return text.decode('utf-8')

    def encrypt_file(self, text, filename):
        text = self.encrypt_text(text)
        write_to_file(text=text, filename=filename)

    def encrypt_file_in_place(self, filename):
        text = read_from_file(filename)
        os.remove(filename)
        self.encrypt_file(text=text, filename=filename)

    def decrypt_file(self, filename):
        text = read_from_file(filename=filename)
        return self.decrypt_text(text)

    def decrypt_file_in_place(self, filename):
        text = self.decrypt_file(filename=filename)
        os.remove(filename)
        write_to_file(text=text, filename=filename)

    def _make_temporary_file(self, permanent_file_name, temporary_file_name):
        text = read_from_file(permanent_file_name)
        text = self.decrypt_text(text)
        write_to_file(text=text, filename=temporary_file_name)

    def _back_to_permanent_file(self, permanent_file_name, temporary_file_name, delete_temp_file: bool = False):
        text = read_from_file(temporary_file_name)
        text = self.encrypt_text(text)
        write_to_file(text=text, filename=permanent_file_name)
        if delete_temp_file:
            os.remove(temporary_file_name)
