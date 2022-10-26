from treglog.treglog import TlogFile

def test_create_treglog_with_no_arguments():
    tlog_tester = TlogFile()
    assert isinstance(tlog_tester, TlogFile)

