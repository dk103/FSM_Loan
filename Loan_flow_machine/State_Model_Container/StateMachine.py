
class StateMachine():
    def __init__(self):
        self.current_state = None
        self.curr_trans = None
        self.all_transition = {}
        self.all_state = {}
        self.previous_state = None

    def set_state(self,state_name):
        self.previous_state = self.current_state
        self.current_state = self.all_state[state_name]


    def executeFSM(self, input):
            if self.curr_trans:
                self.current_state.exit_block()
                print("input received - {}".format(str(input)))
                self.curr_trans.process()
                self.set_state(self.curr_trans.to_state)
                assert self.current_state == self.all_state[self.curr_trans.to_state]
                self.current_state.entry_block
                self.current_state.process()
                self.current_state.next(input)
            else:
               self.current_state.process()
               self.current_state.next(input)



    def add_transition(self,trans_name,transObj):
        self.all_transition[trans_name] =  transObj

    def add_states(self,state_name,stateObj):
        self.all_state[state_name] = stateObj

    def to_transition(self,trans_name):
        self.curr_trans = self.all_transition[trans_name]

