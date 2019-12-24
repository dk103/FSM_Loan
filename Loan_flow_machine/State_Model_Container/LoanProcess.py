from State import LoanEligibleCheckState
from State import AppliedState
from State import DocumentVerifiedState
from State import ApplicantPropertyVerifiedState
from State import LoanSanctionedState
from State import LoanRejectedState
from Transitions import Transition
from StateMachine import StateMachine

class LoanProcess:

    def __init__(self):
        self.FSM = StateMachine()

        #-----adding all states---------
        self.FSM.add_states("Eligible",LoanEligibleCheckState("LoanEligibleState",self.FSM))
        self.FSM.add_states("Applied", AppliedState("AppliedState",self.FSM))
        self.FSM.add_states("DocVerified", DocumentVerifiedState("DocumentVerifiedState",self.FSM))
        self.FSM.add_states("PropertyCheck", ApplicantPropertyVerifiedState("ApplicantPropertyVerifiedState",self.FSM))
        self.FSM.add_states("Approved", LoanSanctionedState("LoanSanctionedState",self.FSM))
        self.FSM.add_states("Rejected", LoanRejectedState("LoanRejectedState",self.FSM))


       #-----adding all Transition--------
        self.FSM.add_transition("toApplied", Transition("Applied"))
        self.FSM.add_transition("toEligible", Transition("Eligible"))
        self.FSM.add_transition("toDocVerification", Transition("DocVerified"))
        self.FSM.add_transition("toPropertyCheck", Transition("PropertyCheck"))
        self.FSM.add_transition("toApprove", Transition("Approved"))
        self.FSM.add_transition("toRejected", Transition("Rejected"))

        self.FSM.set_state("Eligible")

    def execute(self,input):
        self.FSM.executeFSM(input)
