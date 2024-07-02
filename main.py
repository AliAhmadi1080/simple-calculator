import subprocess


class Priority:
    def __init__(self,name:str, priority:int, index:int, symbol:str) -> None:
        self.name = name
        self.index = index
        self.symbol = symbol
        if not isinstance(priority,int):
            raise ValueError('priority should be int')
        self.priority = priority

    def __repr__(self) -> str:
        return f'Priority<priority:{self.priority}, index:{self.index}>'
    
    

class Calculator:
    def __init__(self, string:str) -> None:
        self.string = string.replace(' ', '')
        self.symbols:list[Priority] = []
        self.done = True
        self.is_have_brocet = True if self.string.count('(') else False
        if not self.is_correct_brocet():
            raise SyntaxError(f'I got {self.string.count("(")} "(" but i got {self.string.count(")")} ")"')
            
        self.get_priority()
        
        while (not self.done==False) and (not self.string[1:] in ['+']):
            try:
                float(self.string)
                break
            except:
                pass
            self.get_priority()
            self.calculate()

    def __str__(self) -> str:
        return f'string: {self.string}'
    
    def get_priority(self):
        self.symbols = []
        for i in self.string:
            if i in '+-':
                self.symbols.append(Priority('pos', 2, self.string.index(i), i))
            elif i in '*/':
                self.symbols.append(Priority('div', 1, self.string.index(i), i))
            elif i == '(':
                
                self.symbols.append(Priority('div', 1, self.string.index(i), Calculator(self.string[self.string.index(i):len(self.string)-self.string[::-1].index(')')-1])))
        self.symbols = sorted(self.symbols,key=lambda o:o.priority)

    def is_correct_brocet(self):
        if self.string.count('(') == self.string.count(')'):
            return True
        return False

    def calculate(self):
        priority = self.symbols[0]
        priority_index = priority.index
        priority_symbol = priority.symbol
        before_num,after_num = '',''
        invalid_symbols = ['+','-','*','/']
        index = 1
        while True:
            if priority_index-index >=0:
                num = priority_index-index
            else:
                before_num = before_num[::-1]
                break
            string = self.string[num]
            if not string in invalid_symbols:
                before_num += string
                index += 1
            else:
                before_num = before_num[::-1]
                break

        index = 1
        while True:
            if priority_index+index <= len(self.string)-1:
                num = priority_index+index
            else:
                break
            string = self.string[num]
            if not string in invalid_symbols:
                after_num += string
                index += 1
            else:
                break
        len_befor_num,len_after_num = len(before_num), len(after_num)
        before_num,after_num = float(before_num), float(after_num)
        a = list(self.string)
        for i in range(priority_index-len_befor_num,priority_index+len_after_num+1):
            a[i] = ''
        b = self.string[priority_index+len_after_num+1:len(self.string)]
        a[priority_index+len_after_num+1:] = ''
        
        if priority_symbol == '+':
            result = before_num + after_num

        elif priority_symbol == '-':
            result = before_num - after_num

        elif priority_symbol == '*':
            result = before_num * after_num

        elif priority_symbol == '/':
            try:
                result = before_num / after_num
            except ZeroDivisionError:
                self.string = 'we can not division by zero'
                self.symbols = []
                self.done = False
                return 

        for i in str(result):
                a.append(i)
        a.extend(b)
        self.string = ''.join(a)
if __name__ == "__main__":
    subprocess.run(['clear'])

    while True:
        try:
            my_input = input('--> ')
        except KeyboardInterrupt:
            exit()
        if my_input.lower() == 'exit':
            break
        if my_input.strip() == '':
            continue
        cal = Calculator(my_input)
        print(cal.string)
    