import sys 
input = sys.stdin.readline
cases = int(input())
for i in range(cases):
    phone = input().strip()
    phone = phone.replace("A", "2")
    phone = phone.replace("B", "2")
    phone = phone.replace("C", "2")
    phone = phone.replace("D", "3")
    phone = phone.replace("E", "3")
    phone = phone.replace("F", "3")
    phone = phone.replace("G", "4")
    phone = phone.replace("H", "4")
    phone = phone.replace("I", "4")
    phone = phone.replace("J", "5")
    phone = phone.replace("K", "5")
    phone = phone.replace("L", "5")
    phone = phone.replace("M", "6")
    phone = phone.replace("N", "6")
    phone = phone.replace("O", "6")
    phone = phone.replace("P", "7")
    phone = phone.replace("Q", "7")
    phone = phone.replace("R", "7")
    phone = phone.replace("S", "7")
    phone = phone.replace("T", "8")
    phone = phone.replace("U", "8")
    phone = phone.replace("V", "8")
    phone = phone.replace("W", "9")
    phone = phone.replace("X", "9")
    phone = phone.replace("Y", "9")
    phone = phone.replace("Z", "9")
    phone = phone.replace("-", "")
    print(phone[0:3]+"-"+phone[3:6]+"-"+phone[6:10])