class Solution:
    def sortSentence(self, s: str) -> str:
        string_list = list(s.split(" "))
        str_dict = {}
        final = []
        for string in string_list:
            key = int(string[-1])
            new_str = string[:len(string) - 1]
            str_dict[key]  = new_str
        for i in sorted(str_dict.keys()):
            final.append(str_dict[i])
        return " ".join(final)
               
