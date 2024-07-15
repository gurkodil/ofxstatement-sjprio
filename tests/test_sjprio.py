import os

from ofxstatement.ui import UI
from datetime import datetime

from ofxstatement_sjprio.plugin import SJPrioPlugin


def test_sjprio() -> None:
    pass
    plugin = SJPrioPlugin(UI(), {})
    here = os.path.dirname(__file__)
    sample_filename = os.path.join(here, "Transaktioner_Mitt SJ Prio Mastercard.xlsx")

    parser = plugin.get_parser(sample_filename)
    statement = parser.parse()

    assert statement is not None
    assert statement.account_id == '123456******1337'
    assert statement.currency == 'SEK'
    assert statement.bank_id == 'SJPRIO'

    assert len(statement.lines) == 1
    stmt_line = statement.lines[0]

    assert stmt_line.memo == 'ICA Nära We-Hås - Korpilombolo'
    assert stmt_line.amount == 125.42
    assert stmt_line.date == datetime(2020, 7, 6, 0, 0)
