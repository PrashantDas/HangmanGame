doc = ["""-\_("_")_/-""", """-\_("/)_/-""", """-\_("o")_/-""", """-\_("o")_/-""", """\_("o")_/""", """\_("o")_""", """\_("o")""", """\_(~o~)""", """_(~o~)""", """dead!"""]

# man_book = {num: man for man, num in zip(doc, range(10, 0, -1))}
# print(man_book)


man_book ={1: '\\_("_")_/',
         2: '\\_("/)_/',
         3: '\\_("o")_/',
         4:'\\_("o")_/',
         5: '\\_("o")_/',
         6: '\\_("o")_',
         7: '\\_("o")',
         8: '\\_(~o~)',
         9: '(~o~)',
         10: 'dead!'}


def show_man(wrong_attempt:int)->None:
    return man_book[wrong_attempt]
