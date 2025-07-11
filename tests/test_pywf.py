# -*- coding: utf-8 -*-

"""
**IMPORTANT**:

De-activate virtualenv first, then run ``.venv/bin/python tests/test_pywf.py``
to run this test. And don't use PyCharm IDE, use a terminal instead.

If you are still in venv, then poetry will use the dev venv rather than
creating the .venv for the test project.
"""

from pywf_internal_proprietary.api import PyWf

import sys
import pytest

from pywf_internal_proprietary.vendor.os_platform import IS_MACOS
from pywf_internal_proprietary.runtime import IS_CI
from pywf_internal_proprietary.paths import dir_project_root
from pywf_internal_proprietary.logger import logger


class Test:
    pywf: PyWf

    @classmethod
    def setup_class(cls):
        path_pyproject_toml = (
            dir_project_root
            / "cookiecutter_pywf_internal_proprietary_demo-project"
            / "pyproject.toml"
        )
        cls.pywf = PyWf.from_pyproject_toml(path_pyproject_toml)
        dev_python = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        cls.pywf.toml_data["tool"]["pywf"]["dev_python"] = dev_python

    def test_define(self):
        pywf = self.pywf

        _ = pywf.dir_project_root
        _ = pywf.toml_data

        _ = pywf.package_name
        _ = pywf.package_name_slug
        _ = pywf.package_version
        _ = pywf.package_license
        _ = pywf.package_description
        _ = pywf.package_author_name
        _ = pywf.package_author_email
        _ = pywf.package_maintainer_name
        _ = pywf.package_maintainer_email
        _ = pywf.py_ver_major
        _ = pywf.py_ver_minor
        _ = pywf.py_ver_micro
        _ = pywf.github_account
        _ = pywf.github_token_field
        _ = pywf.git_repo_name
        _ = pywf.github_repo_fullname
        _ = pywf.github_repo_url
        _ = pywf.github_actions_secrets_settings_url
        _ = pywf.github_versioned_release_url
        _ = pywf.codecov_account
        _ = pywf.codecov_token_field
        _ = pywf.aws_region
        _ = pywf.aws_codeartifact_profile
        _ = pywf.aws_codeartifact_domain
        _ = pywf.aws_codeartifact_repository
        _ = pywf.doc_host_aws_profile
        _ = pywf.doc_host_s3_bucket
        _ = pywf.cloudflare_token_field
        _ = pywf.devops_aws_account_id

        if IS_CI is False:
            _ = pywf.github_token
            _ = pywf.codecov_token
            _ = pywf.cloudflare_token

    def test_define_01_paths(self):
        pywf = self.pywf

        _ = pywf.dir_home
        _ = pywf.dir_venv
        _ = pywf.dir_venv_bin
        _ = pywf.get_path_venv_bin_cli
        _ = pywf.path_venv_bin_python
        _ = pywf.path_venv_bin_pip
        _ = pywf.path_venv_bin_pytest
        _ = pywf.path_venv_bin_sphinx_build
        _ = pywf.path_venv_bin_bin_jupyter
        _ = pywf.path_sys_executable
        _ = pywf.get_path_dynamic_bin_cli
        _ = pywf.path_bin_virtualenv
        _ = pywf.path_bin_poetry
        _ = pywf.path_bin_twine
        _ = pywf.dir_python_lib
        _ = pywf.path_version_py
        _ = pywf.package_version
        _ = pywf.dir_tests
        _ = pywf.dir_tests_int
        _ = pywf.dir_tests_load
        _ = pywf.dir_htmlcov
        _ = pywf.path_htmlcov_index_html
        _ = pywf.dir_sphinx_doc
        _ = pywf.dir_sphinx_doc_source
        _ = pywf.dir_sphinx_doc_source_conf_py
        _ = pywf.dir_sphinx_doc_source_python_lib
        _ = pywf.dir_sphinx_doc_build
        _ = pywf.dir_sphinx_doc_build_html
        _ = pywf.path_sphinx_doc_build_index_html
        _ = pywf.path_requirements
        _ = pywf.path_requirements_dev
        _ = pywf.path_requirements_test
        _ = pywf.path_requirements_doc
        _ = pywf.path_requirements_automation
        _ = pywf.path_poetry_lock
        _ = pywf.path_poetry_lock_hash_json
        _ = pywf.path_pyproject_toml
        _ = pywf.dir_build
        _ = pywf.dir_dist
        _ = pywf.path_bin_aws
        _ = pywf.dir_node_modules
        _ = pywf.path_bin_wrangler

    def test_action(self):
        pywf = self.pywf
        verbose = True  # show more log for debugging
        # verbose = False # use verbose = False to hit 100% coverage
        logger.info("")

        pywf.remove_virtualenv(verbose=verbose)
        pywf.remove_virtualenv(verbose=verbose)  # do it twice to test the idempotency
        pywf.create_virtualenv(verbose=verbose)
        pywf.create_virtualenv(verbose=verbose)  # do it twice to test the idempotency

        if IS_MACOS:
            # --- dependency management
            codeartifact_repository_endpoint = pywf.get_codeartifact_repository_endpoint()
            pywf.poetry_source_add_codeartifact(
                codeartifact_repository_endpoint=codeartifact_repository_endpoint,
                verbose=verbose,
            )
            codeartifact_authorization_token = pywf.get_codeartifact_authorization_token()
            pywf.poetry_authorization(
                codeartifact_authorization_token=codeartifact_authorization_token,
                verbose=verbose,
            )
            pywf.poetry_lock(verbose=verbose)
            pywf.poetry_install_only_root(verbose=verbose)
            pywf.poetry_install(verbose=verbose)
            pywf.poetry_install_dev(verbose=verbose)
            pywf.poetry_install_test(verbose=verbose)
            pywf.poetry_install_doc(verbose=verbose)
            pywf.poetry_install_auto(verbose=verbose)
            pywf.poetry_install_all(verbose=verbose)

            pywf.path_poetry_lock_hash_json.unlink(missing_ok=True)
            pywf.poetry_export(verbose=verbose)
            pywf.poetry_export(verbose=verbose)

            # --- test related
            pywf.run_unit_test(verbose=verbose)
            pywf.run_cov_test(verbose=verbose)
            pywf.view_cov(real_run=False, verbose=verbose)
            with pytest.raises(RuntimeError):
                pywf.run_int_test(verbose=verbose)
            with pytest.raises(RuntimeError):
                pywf.run_load_test(verbose=verbose)

            # --- documentation related
            pywf.build_doc(verbose=verbose)
            pywf.view_doc(real_run=False, verbose=verbose)
            pywf.notebook_to_markdown(real_run=False, verbose=verbose)
            pywf.deploy_latest_doc()
            pywf.deploy_versioned_doc()
            pywf.view_latest_doc(real_run=False, verbose=verbose)
            pywf.deploy_cloudflare_pages(real_run=False, verbose=verbose)

            # --- build
            pywf.python_build(verbose=verbose)
            pywf.poetry_build(verbose=verbose)

            pywf.publish_to_codeartifact(real_run=False, verbose=verbose)
            pywf.bump_version(major=True, real_run=False, verbose=verbose)
            pywf.bump_version(minor=True, real_run=False, verbose=verbose)
            pywf.bump_version(patch=True, real_run=False, verbose=verbose)

            # --- setup SAAS service
            pywf.setup_codecov_io_upload_token_on_github(real_run=False, verbose=verbose)
            pywf.setup_cloudflare_pages_upload_token_on_github(real_run=False, verbose=verbose)
            pywf.create_cloudflare_pages_project(real_run=False, verbose=verbose)
            pywf.edit_github_repo_metadata(real_run=False, verbose=verbose)

        # --- clean up
        pywf.remove_virtualenv(verbose=verbose)
        pywf.remove_virtualenv(verbose=verbose)  # do it twice to test the idempotency


if __name__ == "__main__":
    from pywf_internal_proprietary.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_internal_proprietary",
        preview=False,
    )
