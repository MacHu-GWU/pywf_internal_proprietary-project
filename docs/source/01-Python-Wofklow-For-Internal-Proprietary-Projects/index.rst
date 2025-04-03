Python Workflow (PyWf) for Open Source Projects
==============================================================================


Overview
------------------------------------------------------------------------------
PyWf provides a comprehensive automation framework for managing the entire lifecycle of open source Python projects. By consolidating various development tasks into a consistent interface, it eliminates the cognitive overhead of switching between different tools and commands.


Getting Started
------------------------------------------------------------------------------
.. dropdown:: how_to_use.py

    .. literalinclude:: ./how_to_use.py
       :language: python
       :linenos:


Core Functionality
------------------------------------------------------------------------------
**Virtual Environment Management**

- :meth:`~pywf_open_source.define_02_venv.PyWfVenv.create_virtualenv`: Creates a virtual environment using Poetry with the specified Python version
- :meth:`~pywf_open_source.define_02_venv.PyWfVenv.remove_virtualenv`: Removes the virtual environment directory

**Dependency Management**

- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_lock`: Resolves and locks dependencies in the poetry.lock file
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_only_root`: Installs only the package in development mode without dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install`: Installs the package and its core dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_dev`: Installs development dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_test`: Installs testing dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_doc`: Installs documentation dependencies
- :meth:`~pywf_open_source.define_03_deps.PyWfDeps.poetry_install_all`: Installs all dependency groups

**Testing**

- :meth:`~pywf_open_source.define_04_tests.PyWfTests.run_unit_test`: Executes unit tests with pytest
- :meth:`~pywf_open_source.define_04_tests.PyWfTests.run_cov_test`: Runs code coverage tests and generates reports
- :meth:`~pywf_open_source.define_04_tests.PyWfTests.view_cov`: Opens the coverage report in your browser

**Documentation**

- :meth:`~pywf_open_source.define_05_docs.PyWfDocs.build_doc`: Builds documentation using Sphinx
- :meth:`~pywf_open_source.define_05_docs.PyWfDocs.view_doc`: Opens the documentation in your browser
- :meth:`~pywf_open_source.define_05_docs.PyWfDocs.deploy_versioned_doc`: Deploy documentation website to AWS S3 with version
- :meth:`~pywf_open_source.define_05_docs.PyWfDocs.deploy_latest_doc`: Deploy documentation website to AWS S3 as latest version
- :meth:`~pywf_open_source.define_05_docs.PyWfDocs.view_latest_doc`: View latest version of documentation website on AWS S3
- :meth:`~pywf_open_source.define_10_cloudflare.PyWfCloudflare.create_cloudflare_pages_project`: Create Cloudflare pages project
- :meth:`~pywf_open_source.define_10_cloudflare.PyWfCloudflare.deploy_cloudflare_pages`: Deploy Cloudflare pages project from docs/build/html folder

**Building and Publishing**

- :meth:`~pywf_open_source.define_06_build.PyWfBuild.poetry_build`: Creates distribution packages using poetry
- :meth:`~pywf_open_source.define_09_aws.PyWfAws.publish_to_codeartifact`: Publishes the package to AWS CodeArtifact using twine

**CI/CD Integration**

- :meth:`~pywf_open_source.define_08_saas.PyWfSaas.setup_codecov_io_upload_token_on_github`: Configures Codecov.io integration with GitHub Actions
- :meth:`~pywf_open_source.define_07_publish.PyWfPublish.publish_to_github_release`: Creates a GitHub Release for version tracking


**Configuration**

PyWf reads configuration from the `[tool.pywf]` section in your `pyproject.toml`:

TODO need to update this

.. code-block:: toml

    [tool.pywf]
    dev_python = "3.11.8"
    github_account = "YourUsername"
    # Create GitHub token in https://github.com/settings/tokens and put the token at
    # ``${HOME}/.github/${github_account}/pac/${github_token_name}.txt``
    github_token_name = "your-token-file-name"
    codecov_account = "YourUsername"
    # Create Codecov token in https://app.codecov.io/account/gh/${codecov_account}/access and put the token at
    # ``${HOME}/.codecov/github/${codecov_account}/${codecov_token_name}.txt``
    codecov_token_name = "your-token-file-name"
    readthedocs_username = "yourusername"
    readthedocs_project_name = "your-project-file-name"
    # Create Readthedocs token in https://app.readthedocs.org/accounts/tokens/ and put the token at
    # ``${HOME}/.readthedocs/${readthedocs_username}/${readthedocs_token_name}.txt``
    readthedocs_token_name = "your-token"


Unified Command System
------------------------------------------------------------------------------
To simplify your workflow and avoid memorizing complex commands, ``PyWf`` includes a lightweight command pattern that can be integrated with Makefile support:

**Command Wrappers**

The `bin/ directory <https://github.com/MacHu-GWU/pywf_open_source-project/tree/main/bin>`_ contains thin Python wrappers for all PyWf functionality:

.. dropdown:: bin/s01_1_venv_create.py

    .. literalinclude:: ../../../bin/s01_1_venv_create.py
       :language: python
       :linenos:

.. dropdown:: bin/s01_2_venv_remove.py

    .. literalinclude:: ../../../bin/s01_2_venv_remove.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_0_poetry_lock.py

    .. literalinclude:: ../../../bin/s02_0_poetry_lock.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_1_install_only_root.py

    .. literalinclude:: ../../../bin/s02_1_install_only_root.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_2_install.py

    .. literalinclude:: ../../../bin/s02_2_install.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_3_install_dev.py

    .. literalinclude:: ../../../bin/s02_3_install_dev.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_4_install_test.py

    .. literalinclude:: ../../../bin/s02_4_install_test.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_5_install_doc.py

    .. literalinclude:: ../../../bin/s02_5_install_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_6_install_automation.py

    .. literalinclude:: ../../../bin/s02_6_install_automation.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_7_install_all.py

    .. literalinclude:: ../../../bin/s02_7_install_all.py
       :language: python
       :linenos:

.. dropdown:: bin/s02_8_poetry_export.py

    .. literalinclude:: ../../../bin/s02_8_poetry_export.py
       :language: python
       :linenos:

.. dropdown:: bin/s03_1_run_unit_test.py

    .. literalinclude:: ../../../bin/s03_1_run_unit_test.py
       :language: python
       :linenos:

.. dropdown:: bin/s03_2_run_cov_test.py

    .. literalinclude:: ../../../bin/s03_2_run_cov_test.py
       :language: python
       :linenos:

.. dropdown:: bin/s03_3_view_cov_result.py

    .. literalinclude:: ../../../bin/s03_3_view_cov_result.py
       :language: python
       :linenos:

.. dropdown:: bin/s03_4_run_int_test.py

    .. literalinclude:: ../../../bin/s03_4_run_int_test.py
       :language: python
       :linenos:

.. dropdown:: bin/s03_5_run_load_test.py

    .. literalinclude:: ../../../bin/s03_5_run_load_test.py
       :language: python
       :linenos:

.. dropdown:: bin/s04_1_build_doc.py

    .. literalinclude:: ../../../bin/s04_1_build_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/s04_2_view_doc.py

    .. literalinclude:: ../../../bin/s04_2_view_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/s04_3_deploy_versioned_doc.py

    .. literalinclude:: ../../../bin/s04_3_deploy_versioned_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/s04_4_deploy_latest_doc.py

    .. literalinclude:: ../../../bin/s04_4_deploy_latest_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/s04_5_view_latest_doc.py

    .. literalinclude:: ../../../bin/s04_5_view_latest_doc.py
       :language: python
       :linenos:

.. dropdown:: bin/s04_6_create_cloudflare_pages_project.py

    .. literalinclude:: ../../../bin/s04_6_create_cloudflare_pages_project.py
       :language: python
       :linenos:

.. dropdown:: bin/s04_7_deploy_cloudflare_pages.py

    .. literalinclude:: ../../../bin/s04_7_deploy_cloudflare_pages.py
       :language: python
       :linenos:

.. dropdown:: bin/s05_1_build_package.py

    .. literalinclude:: ../../../bin/s05_1_build_package.py
       :language: python
       :linenos:

.. dropdown:: bin/s05_2_publish_package.py

    .. literalinclude:: ../../../bin/s05_2_publish_package.py
       :language: python
       :linenos:

.. dropdown:: bin/s05_3_remove_package_version.py

    .. literalinclude:: ../../../bin/s05_3_remove_package_version.py
       :language: python
       :linenos:

.. dropdown:: bin/s05_4_create_release.py

    .. literalinclude:: ../../../bin/s05_4_create_release.py
       :language: python
       :linenos:

.. dropdown:: bin/s06_1_setup_codecov.py

    .. literalinclude:: ../../../bin/s06_1_setup_codecov.py
       :language: python
       :linenos:

These wrappers initialize PyWf using your project configuration and execute specific functions with sensible defaults.

**Makefile Integration**

The included Makefile provides a unified command interface:

.. code-block:: make

    # -*- coding: utf-8 -*-

    help: ## ** Show this help message
        @perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'


    venv-create: ## ** Create Virtual Environment
        ~/.pyenv/shims/python ./bin/s01_1_venv_create.py


    venv-remove: ## ** Remove Virtual Environment
        ~/.pyenv/shims/python ./bin/s01_2_venv_remove.py


    poetry-source-add: ## Add AWS CodeArtifact as secondary source in poetry
        python ./bin/s02_0_poetry_source_add.py


    poetry-lock: poetry-source-add ## Resolve dependencies using poetry, update poetry.lock file
        ~/.pyenv/shims/python ./bin/s02_0_poetry_lock.py


    install-root: ## Install Package itself without any dependencies
        ~/.pyenv/shims/python ./bin/s02_1_install_only_root.py


    install: ## ** Install main dependencies and Package itself
        ~/.pyenv/shims/python ./bin/s02_2_install.py


    install-dev: ## Install Development Dependencies
        ~/.pyenv/shims/python ./bin/s02_3_install_dev.py


    install-test: ## Install Test Dependencies
        ~/.pyenv/shims/python ./bin/s02_4_install_test.py


    install-doc: ## Install Document Dependencies
        ~/.pyenv/shims/python ./bin/s02_5_install_doc.py


    install-automation: ## Install Dependencies for Automation Script
        ~/.pyenv/shims/python ./bin/s02_6_install_automation.py


    install-all: ## Install All Dependencies
        ~/.pyenv/shims/python ./bin/s02_7_install_all.py


    poetry-export: ## Export dependencies to requirements.txt
        ~/.pyenv/shims/python ./bin/s02_8_poetry_export.py


    test: install install-test test-only ## ** Run test


    test-only: ## Run test without checking test dependencies
        ~/.pyenv/shims/python ./bin/s03_1_run_unit_test.py


    cov: install install-test cov-only ## ** Run code coverage test


    cov-only: ## Run code coverage test without checking test dependencies
        ~/.pyenv/shims/python ./bin/s03_2_run_cov_test.py


    int: install install-test int-only ## ** Run integration test


    int-only: ## Run integration test without checking test dependencies
        ~/.pyenv/shims/python ./bin/s03_3_run_int_test.py


    view-cov: ## View code coverage test report
        ~/.pyenv/shims/python ./bin/s03_3_view_cov_result.py


    build-doc: install install-doc ## Build documentation website locally
        ~/.pyenv/shims/python ./bin/s04_1_build_doc.py


    view-doc: ## View documentation website locally
        ~/.pyenv/shims/python ./bin/s04_2_view_doc.py


    deploy-versioned-doc: install install-doc ## Deploy documentation website to AWS S3 with version
        ./.venv/bin/python ./bin/s04_3_deploy_versioned_doc.py


    deploy-latest-doc: install install-doc ## Deploy documentation website to AWS S3 as latest version
        ./.venv/bin/python ./bin/s04_4_deploy_latest_doc.py


    view-latest-doc: install install-doc ## View latest version of documentation website on AWS S3
        ./.venv/bin/python ./bin/s04_5_view_latest_doc.py


    create-pages-project: ## Create Cloudflare pages project
        ./.venv/bin/python ./bin/s04_6_create_cloudflare_pages_project.py


    deploy-pages: ## Deploy Cloudflare pages project from docs/build/html folder
        ./.venv/bin/python ./bin/s04_7_deploy_cloudflare_pages.py


    build: ## Build Python library distribution package
        ~/.pyenv/shims/python ./bin/s05_1_build_package.py


    publish: build ## Publish Python library to AWS CodeArtifact
        ~/.pyenv/shims/python ./bin/s05_2_publish_package.py


    remove: ## Remove Python package version from AWS CodeArtifact
        ~/.pyenv/shims/python ./bin/s05_3_remove_package_version.py


    release: ## Create Github Release using current version
        ~/.pyenv/shims/python ./bin/s05_4_create_release.py


    setup-codecov: ## Setup Codecov Upload token in GitHub Action Secrets
        ~/.pyenv/shims/python ./bin/s06_1_setup_codecov.py


When you type ``make``, you will see:

.. code-block:: bash

    $ make
    help                                     ** Show this help message
    venv-create                              ** Create Virtual Environment
    venv-remove                              ** Remove Virtual Environment
    poetry-source-add                        Add AWS CodeArtifact as secondary source in poetry
    poetry-lock                              Resolve dependencies using poetry, update poetry.lock file
    install-root                             Install Package itself without any dependencies
    install                                  ** Install main dependencies and Package itself
    install-dev                              Install Development Dependencies
    install-test                             Install Test Dependencies
    install-doc                              Install Document Dependencies
    install-automation                       Install Dependencies for Automation Script
    install-all                              Install All Dependencies
    poetry-export                            Export dependencies to requirements.txt
    test                                     ** Run test
    test-only                                Run test without checking test dependencies
    cov                                      ** Run code coverage test
    cov-only                                 Run code coverage test without checking test dependencies
    int                                      ** Run integration test
    int-only                                 Run integration test without checking test dependencies
    view-cov                                 View code coverage test report
    build-doc                                Build documentation website locally
    view-doc                                 View documentation website locally
    deploy-versioned-doc                     Deploy documentation website to AWS S3 with version
    deploy-latest-doc                        Deploy documentation website to AWS S3 as latest version
    view-latest-doc                          View latest version of documentation website on AWS S3
    create-pages-project                     Create Cloudflare pages project
    deploy-pages                             Deploy Cloudflare pages project from docs/build/html folder
    build                                    Build Python library distribution package
    publish                                  Publish Python library to AWS CodeArtifact
    remove                                   Remove Python package version from AWS CodeArtifact
    release                                  Create Github Release using current version
    setup-codecov                            Setup Codecov Upload token in GitHub Action Secrets

When you type ``make cov``, it actually runs ``python bin/s03_2_run_cov_test.py``

You may also edit the ``Makefile`` yourself to use different global Python instead of ``~/.pyenv/shims/python``.

This approach offers several advantages:

- Consistent command syntax across projects
- Self-documenting commands with ``make help``
- No need to remember underlying tools or syntax


Getting Started with Cookiecutter
------------------------------------------------------------------------------
For new projects, use our **Cookiecutter Template** `cookiecutter-pywf_internal_proprietary <https://github.com/MacHu-GWU/cookiecutter-pywf_internal_proprietary>`_ automatically set up the entire PyWf structure:

**The template provides**:

- Pre-configured directory structure
- Default Makefile with all common commands
- Command wrappers in the `bin/` directory
- Properly configured `pyproject.toml`
- GitHub Actions integration files
- Documentation templates

Simply run:

.. code-block:: bash

    pip install "cookiecutter>=2.6.0,<3.0.0" && cookiecutter https://github.com/MacHu-GWU/cookiecutter-pywf_internal_proprietary

Then follow the prompts to create a new project with the entire PyWf infrastructure ready to use.
