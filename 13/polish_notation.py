class Solution(object):
    
    def is_number(self, n):
        try:
            float(n)
        except ValueError:
            return False
        return True


    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        _stack = []
        
        for brace in tokens:
            if self.is_number(brace):
                _stack.append(float(brace))
            else:
                
                y = _stack.pop()
                x = _stack.pop()
                if brace == '+':
                    result = x + y
                    print('x + y ',x, y, result)
                if brace == '*':
                    result = x * y
                    print('x * y ',x, y, result)
                if brace == '/':
                    result = x / y
                    print('x / y ',x, y, result)
                    if result < 1 and result > 0:
                        result = 0
                    res_convert = int(result)
                    result = float(res_convert)
                if brace == '-':
                    result = x - y
                    print('x - y ',x, y, result)
                _stack.append(round(result))
        
        last_num = _stack.pop()
        return int(last_num)
    