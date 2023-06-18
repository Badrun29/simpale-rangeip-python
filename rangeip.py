def scan(site):
    ur = site.rstrip()
    ch = site.split('\n')[0].split('.')
    ip1 = ch[0]
    ip2 = ch[1]
    ip3 = ch[2]
    taz = str(ip1) + '.' + str(ip2) + '.' + str(ip3)
    i = 0
    while i <= 255:
        i += 1
        print "Ranging ==>" + str(taz) + '.' + str(i)
        open('hasil.txt', 'a').write(str(taz) + '.' + str(i) + '\n')

def remove_duplicates(file_path):
    lines = set()
    with open(file_path, 'r') as file:
        lines = set(file.readlines())
    with open(file_path, 'w') as file:
        file.writelines(sorted(lines))
        
nam = raw_input('List Ips  :')
with open(nam) as f:
    for site in f:
        scan(site)


remove_duplicates('hasil.txt')