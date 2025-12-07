print(f"Empezamos")
res = 0
with open("input.txt", "r", encoding="utf-8") as f:
        for line in (l.strip() for l in f):
            print(f"{line}")
            first_digit = 0
            second_digit = 0
            n = len(line)
            for i, c in enumerate(line):
                first_digit_change = False               
                val = int(c)
                if val > first_digit and i < n - 1:
                    first_digit = val
                    second_digit = 0
                    first_digit_change = True    
                if val > second_digit and not first_digit_change:
                    second_digit = val
                # print(f"first_digit: {first_digit}, second_digit: {second_digit}, value proccessed: {val}")
            mimi = first_digit * 10 + second_digit
            # print(f"n-> {mimi}")
            res += mimi
            # print(f"res-> {res}")
          

    
print(f"Solución y valor del Joytalge: {res}")        