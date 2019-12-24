from State_Model_Container.LoanProcess import LoanProcess
from random import randint
from time import clock
#from State_Model_Container.Transitions import LoanAction


class LoanAction:

    def __init__(self, action):
        self.action = action

    def __str__(self):
        return self.action

    def __eq__(self, other):
        return self.action == other.action

    def __ne__(self, other):
        return self.action != other.action

    def __hash__(self):
        return hash(self.action)





LoanAction.loanCriteriaNotMet = LoanAction("criteria not met")
LoanAction.submitted = LoanAction("submitted")
LoanAction.documentVerification = LoanAction("started verifying document")
LoanAction.showDocument = LoanAction("need more document")
LoanAction.backgroundCheck = LoanAction("customer background check")
LoanAction.conditionClear = LoanAction("all condition met")
LoanAction.Clearance = LoanAction("loan provided")
LoanAction.conditionNotMet = LoanAction("condition not met")
LoanAction.re_apply = LoanAction("loan re apply")
LoanAction.checkEligibilty = LoanAction("check eligibility")
LoanAction.rejected = LoanAction("loan disapproved")


def transform_input_to_action(input):
    switcher = {
        "check eligibility":LoanAction.checkEligibilty,
        "criteria not met":LoanAction.loanCriteriaNotMet,
        "submitted":LoanAction.submitted,
        "started verifying document":LoanAction.documentVerification,
        "need more document":LoanAction.showDocument,
        "customer background check":LoanAction.backgroundCheck,
        "all condition met":LoanAction.conditionClear,
        "loan provided":LoanAction.Clearance,
        "loan disapproved":LoanAction.rejected,
        "condition not met":LoanAction.conditionNotMet,
        "loan re apply":LoanAction.re_apply

    }
    return switcher[input]


if __name__ == '__main__':
    actions = map(lambda lines:lines.strip(),open("Transtion.txt").readlines())
    loan_flow_machine = LoanProcess()
    for act in list(actions):
        action_obj =  transform_input_to_action(act)
        assert isinstance(action_obj,LoanAction) == True
        timer = randint(0,4)
        startTime = clock()
        while(startTime+timer > clock()):
            pass
        loan_flow_machine.execute(action_obj)


