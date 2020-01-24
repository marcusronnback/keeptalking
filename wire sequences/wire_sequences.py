class wire_sequences:
    file_rules = "rules.txt"
    rules = {"RED": [], "BLUE": [], "BLACK": []}

    inputs = {}
    for key in rules.keys():
        inputs[key] = 0

    def __init__(self):

        f = open(self.file_rules,"r")
        current_color = ""

        for line in f:
            if line.rstrip() in self.rules.keys():
                current_color = line.rstrip()
            else:
                self.rules[current_color].append(line.upper().rstrip().split())

        print(self.rules)

    def enter_sequence(self):
        while(True):
            user_input = input("Enter wires in order (red b): ").upper()

            user_input = user_input.split()
            if(len(user_input) == 2):

                wire_color = user_input[0]
                wire_connection = user_input[1]

                if(wire_color in self.rules.keys()):
                    print(f"Wire color: {wire_color}, Connection: {wire_connection}, Previously entered: {self.inputs[wire_color]}, Rule saved: {self.rules[wire_color][self.inputs[wire_color]]}")
                    if(wire_connection in self.rules[wire_color][self.inputs[wire_color]]):
                        print(f"\nCut {wire_color}\n")
                    self.inputs[wire_color] += 1

nice = wire_sequences()
nice.enter_sequence()
