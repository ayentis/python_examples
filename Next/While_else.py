
def is_comment(item):
    return isinstance(item, str) and item.startswith("#")


def execute(program):
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else:
        print('empty program')
        return

    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:
        print("program successful.")
        print('Result: ', pending)
    print('finish')


if __name__ == "__main__":
    import operator

    program = list(reversed((
        "# Comment1",
        "# comment 2",
        5,
        2,
        operator.add,
        3,
        operator.mul

    )))
    execute(program)
