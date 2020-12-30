import ply.lex as lex
import ply.yacc as yacc

tokens = ('NUMBER', 'PLUS', 'TIMES', 'LPAREN', 'RPAREN',)

t_PLUS    = r'\+'
t_TIMES   = r'\*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore = " \t"

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    t.lexer.skip(1)

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression TIMES expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    pass

lex.lex()

with open('input.txt', 'r') as f:
    input = list(map(str.strip, (map(str, f))))

precedence = (('left','PLUS','TIMES'),)
parser = yacc.yacc(debug=0, write_tables=0)
print("Task 1:", sum(map(lambda x: parser.parse(x), input)))

precedence = (('left','TIMES'),('right','PLUS'),)
parser = yacc.yacc(debug=0, write_tables=0)
print("Task 2:", sum(map(lambda x: parser.parse(x), input)))
