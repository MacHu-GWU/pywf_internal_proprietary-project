# -*- coding: utf-8 -*-

from cookiecutter_pywf_internal_proprietary_demo import api


def test():
    _ = api


if __name__ == "__main__":
    from cookiecutter_pywf_internal_proprietary_demo.tests import run_cov_test

    run_cov_test(
        __file__,
        "cookiecutter_pywf_internal_proprietary_demo.api",
        preview=False,
    )
