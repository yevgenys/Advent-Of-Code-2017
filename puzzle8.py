from pprint import pprint

CMDS = {
    "inc": lambda var, val: var + val,
    "dec": lambda var, val: var - val
}


def read_input():
    with open("puzzle8_input", "r") as f:
        return f.read().splitlines()


def init_vars(vars_, expression, condition):
    for exp in (expression, condition):
        name = exp.split(" ")[0]
        if name not in vars_:
            vars_[name] = 0


def apply_instructions(instructions):
    vars_ = {}
    highest_value = 0
    for expr_cond in map(lambda l: l.split("if"), instructions):
        expression, condition = map(lambda v: v.strip(), expr_cond)
        init_vars(vars_, expression, condition)
        varname, cond, val = condition.split(" ")
        if eval("{var} {cond} {val}".format(var=vars_[varname], cond=cond, val=val)):
            varname, cmd, val = expression.split(" ")
            vars_[varname] = CMDS[cmd](vars_[varname], int(val))
            if abs(vars_[varname]) > highest_value:
                highest_value = abs(vars_[varname])
    return vars_, highest_value


if __name__ == '__main__':
    instructions = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    assert max(apply_instructions(instructions.splitlines())[0].values()) == 1

    vars, highest_value = apply_instructions(read_input())
    pprint(highest_value)
    print(max(vars.values()))
