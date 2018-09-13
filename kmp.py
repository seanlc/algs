def getLPS(pattern):
    lps = []
    for i,char in enumerate(pattern):
        if i == 0:
            lps.append(0)
        else:
            lastLPS = lps[i-1]
            secondToLastLPS = lastLPS - 1
            if pattern[i] == pattern[lastLPS]:
                lps.append(lastLPS + 1)
            elif pattern[i] == pattern[secondToLastLPS]:
                lps.append(lastLPS)
            else:
                lps.append(0)
    return lps

pattern = "AAACAAAAAC"
pattern2 = "AAABAAA"
lps = getLPS(pattern2)
print(lps)
