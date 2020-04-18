class Solution:
    def entityParser(self, text: str) -> str:
        replace_dict={"&quot;":'"',"&apos;":"'","&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
        res = []
        flag = False
        keyword = []
        for c in text:
            if c == "&":
                if flag:
                    res.append("".join(keyword))
                flag = True
                keyword = ["&"]
            elif flag:
                keyword.append(c)
                if c == ";":
                    keyword = "".join(keyword)
                    res.append(replace_dict.get(keyword, keyword))
                    flag = False
            else:
                res.append(c)
        if flag:
            res.append("".join(keyword))
        return "".join(res)
