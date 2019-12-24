from State_Model_Container.LoanProcess import LoanProcess
from random import randint
from time import clock
from State_Model_Container.Transitions import LoanAction


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


