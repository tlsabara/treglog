import pytest

from treglog.treglog import TlogFile, TlogDB
from treglog.Errors import TregGeneralErrors
from treglog.Base.Interfaces import InterfaceTlog, InterfaceTlogCommander


def test_cant_create_tlogfile_with_no_arguments():
    try:
        tlog_tester = TlogFile()
    except TregGeneralErrors.TlogErrorParameterValue:
        assert True
    else:
        assert False


@pytest.mark.parametrize(
    'value_keys',
    ['d', 'v', 's']
)
def test_create_tlogfile_with_knew_arguments(value_keys: str):
    tlog_tester = TlogFile(mode_log=value_keys)
    assert isinstance(tlog_tester, TlogFile)


def test_raise_error_if_create_tlogfile_with_invalid_mode_log():
    try:
        tlog_tester = TlogFile(mode_log="*")
    except TregGeneralErrors.TlogErrorParameterValue:
        assert True
    else:
        assert False


def test_cant_create_tlogdb_with_no_arguments():
    try:
        tlog_tester = TlogDB()
    except TregGeneralErrors.TlogErrorParameterValue:
        assert True
    else:
        assert False


@pytest.mark.parametrize(
    'value_keys',
    ['d', 'v', 's']
)
def test_create_tlogdb_with_knew_arguments(value_keys: str):
    tlog_tester = TlogDB(mode_log=value_keys)
    assert isinstance(tlog_tester, TlogDB)


def test_interface_have_attr_accepted_modes():
    assert 'ACCEPTED_MODES' in InterfaceTlog.__dict__


def test_interface_have_attr_accepted_modes():
    assert 'ACCEPTED_KEYWORDS' in InterfaceTlog.__dict__