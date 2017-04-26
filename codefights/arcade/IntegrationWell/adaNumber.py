import re
def adaNumber(s):
    s = s.replace('_', '')
    if re.match('^[\d]+$', s):
        return True
    x = re.search('^([\d]{1,2})#([\dA-Fa-z]+)#$', s)
    if x:
        try:
            # try to convert to integer
            base = int(x.group(1))
            if base > 1 and base < 17:
                int(x.group(2), base)
                return True
            else:
                return False
        except:
            return False
    else:
        return False

print adaNumber('123_456_789')
print adaNumber('16#123abc#')
print adaNumber('10#123abc#')
print adaNumber('10#10#123ABC#')
print adaNumber('10#0#')
print adaNumber('10##')
print adaNumber('1#0#')