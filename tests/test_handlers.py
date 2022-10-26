from treglog.Errors import TregGeneralErrors
from treglog.treglog import TlogFile, TlogDB

def test_raise_error_on_set_attr_buffer_log_on_tlogfile():
    tlog_tester = TlogFile()
    try:
        tlog_tester.buffer_log = 'any value'
    except AttributeError:
        assert True
    else:
        False

def test_raise_error_on_set_attr_full_log_on_tlogfile():
    tlog_tester = TlogFile()
    try:
        tlog_tester.full_log = 'any value'
    except AttributeError:
        assert True
    else:
        False

def test_raise_error_on_set_attr_buffer_log_on_tlogdb():
    tlog_tester = TlogDB()
    try:
        tlog_tester.buffer_log = 'any value'
    except AttributeError:
        assert True
    else:
        False

def test_raise_error_on_set_attr_full_log_on_tlogdb():
    tlog_tester = TlogDB()
    try:
        tlog_tester.full_log = 'any value'
    except AttributeError:
        assert True
    else:
        False