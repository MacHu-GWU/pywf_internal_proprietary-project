# -*- coding: utf-8 -*-

from pywf_internal_proprietary import api


def test():
    _ = api

    _ = api.PyWf
    _ = api.PyWf.create_virtualenv
    _ = api.PyWf.remove_virtualenv
    _ = api.PyWf.poetry_source_add_codeartifact
    _ = api.PyWf.poetry_authorization
    _ = api.PyWf.pip_authorization
    _ = api.PyWf.twine_authorization
    _ = api.PyWf.poetry_lock
    _ = api.PyWf.poetry_export
    _ = api.PyWf.poetry_install_only_root
    _ = api.PyWf.poetry_install
    _ = api.PyWf.poetry_install_dev
    _ = api.PyWf.poetry_install_test
    _ = api.PyWf.poetry_install_doc
    _ = api.PyWf.poetry_install_auto
    _ = api.PyWf.poetry_install_all
    _ = api.PyWf.run_unit_test
    _ = api.PyWf.run_cov_test
    _ = api.PyWf.view_cov
    _ = api.PyWf.run_int_test
    _ = api.PyWf.run_load_test
    _ = api.PyWf.notebook_to_markdown
    _ = api.PyWf.build_doc
    _ = api.PyWf.view_doc
    _ = api.PyWf.deploy_versioned_doc
    _ = api.PyWf.deploy_latest_doc
    _ = api.PyWf.view_latest_doc
    _ = api.PyWf.create_cloudflare_pages_project
    _ = api.PyWf.deploy_cloudflare_pages
    _ = api.PyWf.poetry_build
    _ = api.PyWf.publish_to_codeartifact
    _ = api.PyWf.remove_from_codeartifact
    _ = api.PyWf.publish_to_github_release
    _ = api.PyWf.setup_codecov_io_upload_token_on_github
    _ = api.PyWf.setup_cloudflare_pages_upload_token_on_github
    _ = api.PyWf.edit_github_repo_metadata


if __name__ == "__main__":
    from pywf_internal_proprietary.tests import run_cov_test

    run_cov_test(
        __file__,
        "pywf_internal_proprietary.api",
        preview=False,
    )
