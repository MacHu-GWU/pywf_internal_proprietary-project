# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from cookiecutter_pywf_internal_proprietary_demo.tests import run_cov_test

    run_cov_test(
        __file__,
        "cookiecutter_pywf_internal_proprietary_demo",
        is_folder=True,
        preview=False,
    )
