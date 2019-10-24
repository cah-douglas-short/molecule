import os
import pytest

pytest_plugins = ['helpers_namespace']


@pytest.fixture(scope="session", autouse=True)
def environ():
    # disable use of .netrc file to avoid galaxy-install errors with:
    # [ERROR]: failed to download the file: HTTP Error 401: Unauthorized
    # https://github.com/ansible/ansible/issues/61666
    os.environ['NETRC'] = ''
