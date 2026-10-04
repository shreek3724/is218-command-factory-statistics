import pytest
from calculator.commands import Command, CalculateCommand, HistoryCommand, ClearHistoryCommand, HelpCommand, CountCommand
from calculator.factory import CalculationFactory
from calculator.session import CalculatorSession


def test_contract_is_abstract():

    class IncompleteCommand(Command):
        pass
    with pytest.raises(TypeError):
        IncompleteCommand()


def test_action_flow_and_history():
    session = CalculatorSession()
    calculation = CalculationFactory.create('add', *[2, 3])
    command = CalculateCommand(session, calculation)
    assert session.get_history() == []
    assert command.execute() == 'Result: 5.0000'
    assert 'add 2.0 3.0 = 5.0000' in HistoryCommand(session).execute()
    assert ClearHistoryCommand(session).execute() == 'History cleared.'
    assert HistoryCommand(session).execute() == 'History is empty.'


def test_failure_is_not_recorded():
    session = CalculatorSession()
    command = CalculateCommand(session, CalculationFactory.create('divide', *[1, 0]))
    with pytest.raises(ZeroDivisionError):
        command.execute()
    assert session.get_history() == []


def test_help_has_no_session_dependency():
    assert 'history' in HelpCommand().execute()

# added new tests for CountCommand for part 4
def test_count_command_and_faliure_isolation():
    session = CalculatorSession()
    count_cmd = CountCommand(session)
    assert count_cmd.execute() == 'Saved calculations: 0'

    #successful calculation increments count
    calc = CalculationFactory.create('add', 2,3)
    CalculateCommand(session, calc).execute()
    assert count_cmd.execute() == 'Saved calculations: 1'

    #failed calculation does not increment count
    bad_calc = CalculationFactory.create('divide', 1, 0)
    with pytest.raises(ZeroDivisionError):
        CalculateCommand(session, bad_calc).execute()
    assert count_cmd.execute() == 'Saved calculations: 1'