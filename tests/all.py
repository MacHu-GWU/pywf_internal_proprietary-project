# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from pywf_internal_proprietary.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_internal_proprietary",
        is_folder=True,
        preview=False,
    )
