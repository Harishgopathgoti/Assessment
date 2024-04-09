import re


for _ in range(int(input())):
    num = input()

    flag1 = bool(re.match(r"^[456]\d{15}$", num))
    flag2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num = num.replace("-", "")
    flag3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (flag1 or flag2) and flag3:
        print("Valid")
    else:
        print("Invalid")
