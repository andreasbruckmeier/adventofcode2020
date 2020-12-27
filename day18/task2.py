def calculate(expression, level = 0):
    result = 0
    operator = None
    idx = 0
    while idx < len(expression):
        token = expression[idx]
        if token == ' ':
            idx += 1
            continue
        if token == '+':
            operator = token
        elif token == '*':
            token_value, subidx = calculate(expression[idx+1:], level + 1)
            memres = result
            result *= token_value
            idx += subidx + 1
            if level > 0:
                return result, idx
            operator = token
        elif token == '(':
            token_value, subidx = calculate(expression[idx+1:], level + 1)
            if operator == '+':
                result += token_value
            elif operator == '*':
                result *= token_value
            else:
                result = token_value
            idx += subidx + 1
        elif token == ')':
            return result, idx
        else:
            if operator:
                token_value = int(token)
                if operator == '+':
                    result += token_value
                else:
                    result *= token_value
            else:
                result = int(token)
            operator = None
        idx += 1
    return result, idx

with open('input.txt', 'r') as f:
   print(sum(map(lambda x: calculate(x)[0], map(str.strip, (map(str, f))))))
