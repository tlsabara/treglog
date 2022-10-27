import pytest
from treglog.treglog import TlogFile
from treglog.Errors import TregFileErrors, TregGeneralErrors

@pytest.fixture
def valid_instance_tlogfile() -> TlogFile:
    return TlogFile(mode_log='d')


def test_raises_exeption_if_kword_is_invalid():
    try:
        log = TlogFile(mode_log='d', worg_key='any_value')
    except TregGeneralErrors.TlogErrorParameterValue:
        assert True
    else:
        assert False


def test_raise_error_with_no_valid_path_for_path_export_file():
    try:
        log = TlogFile(mode_log='d', path_export=int)
    except TregFileErrors.TlogErrorPathNotExistsOrInacessible:
        assert True
    else:
        assert False

def test_write_lines_successfully_with_mlog_method(valid_instance_tlogfile):
    base_lines = 4
    qtd_lines = 10
    for i in range(qtd_lines):
        valid_instance_tlogfile.m_log(f'teste_{i}')

    file = valid_instance_tlogfile.export_file
    count_lines = 0
    with open(file, 'r') as log_file:
        for line in log_file.readlines():
            count_lines +=1

    assert  count_lines == base_lines + qtd_lines
