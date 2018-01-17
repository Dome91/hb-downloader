__author__ = "Brian Schkerke"
__copyright__ = "Copyright 2016 Brian Schkerke"
__license__ = "MIT"


class ConfigData(object):
    VERSION = 0.41
    username = ""
    password = ""
    authy_token = ""
    download_location = ""
    debug = True
    cookie_filename = "cookies.txt"
    auth_sess_cookie = ""
    write_md5 = True
    read_md5 = True
    force_md5 = False
    chunk_size = 8192000
    ignore_md5 = False
    resume_downloads = True

    download_platforms = {
        'ebook': True,
    }

    file_formats = {
        'CBZ': True,
        'PDF': True,
        'EPUB': True,
        'PDF (HQ)': True
    }
