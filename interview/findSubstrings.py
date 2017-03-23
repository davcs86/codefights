def findSubstrings(words, parts):
    parts = sorted(parts, key = len, reverse=True)
    for i, w in enumerate(words):
        psz = 0
        ppos = len(w)
        nw = w
        for p in parts:
            if len(p) >= psz and len(p) <= len(w):
                pos = w.find(p)
                if (len(p) > psz or pos < ppos) and pos >= 0:
                    # found
                    psz = len(p)
                    ppos = pos
                    nw = w.replace(p, "["+p+"]", 1)
            if len(p) < psz:
                break
        words[i] = nw
    return words


words = ["neuroses",
 "myopic",
 "sufficient",
 "televise",
 "coccidiosis",
 "gules",
 "during",
 "construe",
 "establish",
 "ethyl"]
parts = ["aaaaa",
 "Aaaa",
 "E",
 "z",
 "Zzzzz",
 "a",
 "mel",
 "lon",
 "el",
 "An",
 "ise",
 "d",
 "g",
 "wnoVV",
 "i",
 "IUMc",
 "P",
 "KQ",
 "QfRz",
 "Xyj",
 "yiHS"]

print parts

print findSubstrings(words, parts)