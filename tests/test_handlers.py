import pytest

from treglog.Errors import TregGeneralErrors
from treglog.treglog import TlogFile, TlogDB


@pytest.fixture
def instance_tlogfile() -> TlogFile:
    return TlogFile(mode_log='d')


@pytest.fixture
def instance_tlogdb() -> TlogDB:
    return TlogDB(mode_log='d')


def test_raise_error_on_set_attr_buffer_log_on_tlogfile(instance_tlogfile: TlogFile):
    try:
        instance_tlogfile.buffer_log = 'any value'
    except AttributeError:
        assert True
    else:
        False


def test_raise_error_on_set_attr_full_log_on_tlogfile(instance_tlogfile: TlogFile):
    try:
        instance_tlogfile.full_log = 'any value'
    except AttributeError:
        assert True
    else:
        False


def test_raise_error_on_set_attr_buffer_log_on_tlogdb(instance_tlogdb: TlogDB):
    try:
        instance_tlogdb.buffer_log = 'any value'
    except AttributeError:
        assert True
    else:
        False


def test_raise_error_on_set_attr_full_log_on_tlogdb(instance_tlogdb):
    try:
        instance_tlogdb.full_log = 'any value'
    except AttributeError:
        assert True
    else:
        False
