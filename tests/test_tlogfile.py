import pytest
from treglog.treglog import TlogFile
from treglog.Errors import TregFileErrors, TregGeneralErrors


def test_raises_exeption_if_kword_is_invalid():
    try:
        log = TlogFile(worg_key='any_value')
    except TregGeneralErrors.TlogErrorParameterValue:
        assert True
    else:
        assert False

def test_raise_error_with_no_valid_path_for_path_export_file():
    try:
        log = TlogFile(path_export='')
    except TregFileErrors.TlogErrorPathNotExistsOrInacessible:
        assert True
    else:
        assert False