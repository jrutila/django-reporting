# -*- coding: utf-8 -*-


def lookup_key(key, dct, report):
    k = key
    # the key can be either a method or returned via a callable.
    if callable(key):
        attr = key
        value = attr(dct)
        k = None
    elif report is not None and hasattr(report, key):
        attr = getattr(report, key)
        value = attr(dct)
        k = None

    if k:
        attr = None
        if isinstance(dct, dict):
            value = dct[k]
        else:
            value = getattr(dct, k)

    return k, attr, value
