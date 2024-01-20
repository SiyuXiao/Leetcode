def subdomainVisits(cpdomains):
    D = {}
    for a in cpdomains:
        b = a.split()
        num = int(b[0])
        c = b[1].split('.')
        c1 = c[-1]
        if len(c) == 2:
            c2 = c[-2] + '.' + c[-1]
        if len(c) == 3:
            c2 = c[-2] + '.' + c[-1]
            c3 = b[1]
            if c3 not in D:
                D[c3] = num
            else:
                D[c3] += num
        if c1 not in D:
            D[c1] = num
        else:
            D[c1] += num
        if c2 not in D:
            D[c2] = num
        else:
            D[c2] += num
    output = []
    for a in D:
        output.append(str(D[a]) + ' ' + a)
    return output
result = subdomainVisits(["900 google.mail", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
print(result)
#["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]