from treglog.Errors import TregGeneralErrors
from treglog.treglog import TlogFile

def test_raise_error_on_set_attr_buffer_log():
    tlog_tester = TlogFile()
    try:
        tlog_tester.buffer_log = 'any value'
    except TregGeneralErrors.TlogErrorIncorrectUtilization:
        assert True
    else:
        False