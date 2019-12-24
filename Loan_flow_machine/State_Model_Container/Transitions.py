
class Transition():

    def __init__(self,to_state=None):
        self.to_state = to_state

    def process(self):
        print("Transitioning .........")

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
LoanAction.re_apply = LoanAction("loan re apply and met eligibilty creteria")
LoanAction.checkEligibilty = LoanAction("check eligibility")
LoanAction.rejected = LoanAction("loan disapproved")