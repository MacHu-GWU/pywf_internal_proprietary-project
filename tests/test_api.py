# -*- coding: utf-8 -*-

from pywf_internal_proprietary import api


def test():
    _ = api


if __name__ == "__main__":
    from pywf_internal_proprietary.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_internal_proprietary.api",
        preview=False,
    )
