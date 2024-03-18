def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):    #填充"0"，将两个字符串变为等长
            temp = a
            a = b
            b = temp
        a = a[::-1]           #倒序二进制字符串
        b = b[::-1]
        while len(a)!=len(b):     #二进制字符串长度设置相同
            b = b+"0"
        extra = 0             #进位
        new_binary = ""
        for index, num in enumerate(a):     #遍历
            import pdb;pdb.set_trace()
            b_sum = int(b[index])
            new_binary = new_binary + str((int(num) + b_sum + extra) % 2)     #二进制加法运算
            if int(num) + b_sum + extra > 1:     #是否进位
                extra = 1
            else:
                extra = 0
        if extra == 1:        #最高位是否进位
            new_binary = new_binary + "1"     
        return new_binary[::-1]    #倒序输出

case_input = ["1101", "110"]
out = addBinary(case_input[0], case_input[1])
print(out)