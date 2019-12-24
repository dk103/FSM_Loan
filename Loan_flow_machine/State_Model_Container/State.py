from Transitions import LoanAction
from StateMachine import StateMachine

class State:

    def __init__(self,state_name,FSM):
         assert isinstance(FSM, StateMachine)
         self.FSM = FSM
         self._stateName = state_name

    def entry_block(self):
        pass

    def  process(self):
        raise NotImplementedError

    def next(self,input):
         pass
    @property
    def get_state_name(self):
        return self._stateName

    def exit_block(self):
        print('Exiting...')
        self.timer = 0

    def __eq__(self, other):
        return self._stateName == other._stateName

    def __ne__(self, other):
        return self._stateName == other._stateName



class LoanEligibleCheckState(State):

    def __init__(self,state_name,FSM):
        super().__init__(state_name,FSM)

    def entry_block(self):
        super().entry_block()
        print("{} is started ".format(self.get_state_name))

    def process(self):
        print("undergoing eligible criterion :-{}" .format(self.get_state_name))

    def next(self,input):
        if input == LoanAction.submitted:
            self.FSM.to_transition("toApplied")
        elif input == LoanAction.loanCriteriaNotMet:
            self.FSM.to_transition("toRejected")

        elif input == LoanAction.re_apply:
            self.FSM.to_transition("toApplied")

        elif input == LoanAction.checkEligibilty:
            self.FSM.to_transition("toEligible")


    def exit_block(self):
        print(" {} exited".format(self.get_state_name))


class AppliedState(State):

    def __init__(self, state_name,FSM):
        super().__init__(state_name,FSM)

    def entry_block(self):
        super().entry_block()
        print("{} is begun ".format(self.get_state_name))

    def process(self):
        print("Executing...... {} ".format(self.get_state_name))

    def next(self,input):
        if input == LoanAction.documentVerification:
            self.FSM.to_transition("toDocVerification")
        elif input == LoanAction.showDocument:
            self.FSM.to_transition("toApplied")

        elif input == LoanAction.loanCriteriaNotMet:
            self.FSM.to_transition("toEligible")


    def exit_block(self):
        print("{} exited".format(self.get_state_name))


class DocumentVerifiedState(State):

    def __init__(self, state_name,FSM):
        super().__init__(state_name,FSM)

    def entry_block(self):
        super().entry_block()
        print("{} begun ".format(self.get_state_name))

    def process(self):
        print("Executing... {} ".format(self.get_state_name))

    def next(self,input):
        if input == LoanAction.backgroundCheck:
            self.FSM.to_transition("toPropertyCheck")
        elif input == LoanAction.showDocument:
            self.FSM.to_transition("toApplied")

    def exit_block(self):
        print("{} exited".format(self.get_state_name))


class ApplicantPropertyVerifiedState(State):
    def __init__(self, state_name,FSM):
        super().__init__(state_name,FSM)

    def entry_block(self):
        super().entry_block()
        print("{} begun ".format(self.get_state_name))

    def process(self):
        print("Executing {} ".format(self.get_state_name))

    def next(self,input):
        if input == LoanAction.conditionClear:
            self.FSM.to_transition("toApprove")
        elif input == LoanAction.conditionNotMet:
            self.FSM.to_transition("toRejected")

        elif input == LoanAction.showDocument:
            self.FSM.to_transition("toApplied")

    def exit_block(self):
        print("{} exited".format(self.get_state_name))


class LoanSanctionedState(State):
    def __init__(self, state_name,FSM):
        super().__init__(state_name,FSM)

    def entry_block(self):
        super().entry_block()
        print("{} begun ".format(self.get_state_name))

    def process(self):
        print("CONGO  !!!!!...........Loan amt will be processed{}")

    def next(self,input):
        if input == LoanAction.Clearance:
            super().next(self)

    def exit_block(self):
        print("{} exited".format(self.get_state_name))

class LoanRejectedState(State):
    def __init__(self, state_name,FSM):
        super().__init__(state_name,FSM)

    def entry_block(self):
        super().entry_block()
        print("{} begun ".format(self.get_state_name))

    def process(self):
        print("SORRYY...!!!! ...LOAN REJECTED")

    def next(self,input):
        if input == LoanAction.re_apply:
            self.FSM.to_transition("toApplied")
        elif input == LoanAction.rejected:
            super().next(input)

    def exit_block(self):
        print("{} exited".format(self.get_state_name))