# bt,

def test(msg_from_papa):
    print("This is test function.\n"
          "Found msg from parent - %s" % msg)
    i = 1
    if i == 1:
        test2()
    else:
        print("Yay.. we made it!")


def test2(msg_from_granpa, msg_from_papa):
    print("This is test2 function.\n"
          "Found msg from parent - %s\n"
          "Found msg from grand parent - %s" % (msg_from_papa, msg_from_granpa))

def main():
    print("This is main function")
    test("calling test function from main function")
# import firstprog
# import pdb
# pdb.run('firstprog.test()')

# print("test")
main()