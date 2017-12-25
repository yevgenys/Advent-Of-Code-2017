from Queue import Queue, Empty
from threading import Thread


def read_input():
    with open("puzzle18_input", "r") as f:
        return f.read().splitlines()


def play_and_save(a, db):
    name = "last_{}".format(a)
    dba = db.get(a, 0)
    db[name] = dba


def get_b(b, db):
    if isinstance(b, int):
        return b
    if b.isdigit() or b[0] == "-":
        return int(b)
    return db[b]


def set_(a, b, db):
    db[a] = get_b(b, db)


def add(a, b, db):
    dba = db.get(a, 0)
    db[a] = get_b(b, db) + dba


def mul(a, b, db):
    dba = db.get(a, 0)
    db[a] = get_b(b, db) * dba


def mod(a, b, db):
    dba = db.get(a, 0)
    db[a] = dba % get_b(b, db)


def rcv(a, db):
    if a != 0:
        name = "last_{}".format(a)
        name_ = db.get(name)
        if name_ is not None:
            return name_


def rcv_p2(register, q, db):
    b = q.get(True, 2)
    set_(register, b, db)


def jgz(a, b, db):
    if a.isdigit():
        val = int(a)
    else:
        val = db[a]
    if val > 0:
        return get_b(b, db)
    return 0


COMMANDS = {
    "snd": play_and_save,
    "set": set_,
    "add": add,
    "mul": mul,
    "mod": mod,
    "rcv": rcv,
    "jgz": jgz
}


def proc_p1(instrs):
    pointer = 0
    db = {}
    while True:
        t = instrs[pointer].split(" ")
        cmd_name = t[0]
        params = t[1:]
        params.append(db)
        res = COMMANDS[cmd_name](*params)
        if res and cmd_name == "rcv":
            return res
        pointer += res if res else 1


def proc(instrs, db, sndQ, rcvQ):
    pointer = 0
    while pointer < len(instrs):
        t = instrs[pointer].split(" ")
        cmd_name = t[0]
        params = t[1:]
        res = 0
        if cmd_name == "rcv":
            rcv_p2(params[0], rcvQ, db)
        elif cmd_name == "snd":
            sent = db.get("sent", 0)
            db["sent"] = sent + 1
            sndQ.put(get_b(params[0], db))
        else:
            params.append(db)
            res = COMMANDS[cmd_name](*params)

        pointer += res if res else 1


def proc_p2(instrs):
    db1 = {"p": 0}
    db2 = {"p": 1}
    q1 = Queue()
    q2 = Queue()

    t1 = Thread(target=proc, args=(instrs, db1, q1, q2))
    t2 = Thread(target=proc, args=(instrs, db2, q2, q1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Part2: {}".format(db2["sent"]))


if __name__ == '__main__':
    print("Part1: {}".format(proc_p1(read_input())))
    proc_p2(read_input())
