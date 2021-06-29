import re

class SimpleCalc(object):

    def check(self,exp):

        res = re.findall(r"[^\d\+\-\*/\(\)\.]", exp)
        print(res)
        if res:
            print("The expression is incorrect!!!")
            print("Illegal character entered:", res)
            return False
        res = re.findall(r"(?:[\d\)]\()|(?:\([\*/\)])|(?:[\-\+\*/]\))",exp)
        if res :
            print("The expression is incorrect!!!")
            print("Brackets used incorrectly:", res)
            return False
        res = re.findall(r"\(|\)", exp)
        if res.count('(') != res.count(')'):
            print("The expression is incorrect!!!")
            print("Brackets do not match:", res)
            return False

        res = re.findall(r"[\-\+/]{2,}|\*{3,}", exp)
        if res:
            print("The expression is incorrect!!!")
            print("Wrong operator:", res)
            return False

        res = re.findall(r"(^(?<=[0-9])?\.\d+)|(\.\d*?\.)|\.(\D|$)", exp)

        if res:
            print("The expression is incorrect!!!")
            print("The decimal point is wrong:", res)
            return False

        return True

def main():
    simpleCalc = SimpleCalc()

    while True:
        exp = input("Please enter a correct expression (exit please enter e):\n")
        if exp == 'e':
            break
        if simpleCalc.check(exp):
            print('=',eval(exp))
        else:
            continue

if __name__ == '__main__':
    main()
