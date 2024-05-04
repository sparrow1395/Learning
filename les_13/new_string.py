class String(str):
    def __add__(self, other):
        new_s = str(self)
        new_o = str(other)
        result = new_s + new_o
        return result

    def __sub__(self, other):
        result = ""
        new_s = str(self)
        new_o = str(other)
        if new_o in new_s:
            result = new_s.replace(new_o, "", 1)
        else:
            result = new_s
        return result


print(String("Jake7") - "Jake")
