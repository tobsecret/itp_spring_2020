# 1. Open your file and read it
#
# 2. Filter on "GET" requests
#
# 3. For each valid request:
#     - Extract bytestr
#     - store it
#
# 4. compute average bytes and print


# fh = open('access-log', 'r')
# count = 0
# bytes = 0
#
# for line in fh:
#     if 'GET' in line:
#         # print(line)
#         bytestr = line.split()[-1]
#         if bytestr == '-':
#             continue
#         count += 1
#         bytes += int(bytestr)

# fh.close()
# print('# GETs: ', count)
# print('Total bytes transferred: ', bytes)
# print('Avg bytes per call: ', bytes/count)


def get_requests(fh, rtype='GET'):
    valid_lines = []
    for line in fh:
        if 'GET' in line:
            valid_lines.append(line)
    return valid_lines

def get_bytestrs(valid_lines):
    bytestrs = []
    for valid_line in valid_lines:
        bytestrs.append(valid_line.split()[-1])
    return bytestrs

def get_non_redirects(bytestrs):
    valid_bytestrs = []
    for bytestr in bytestrs:
        if '-' not in bytestr:
            valid_bytestrs.append(int(bytestr))
    return valid_bytestrs


fh = open('access-log', 'r')
valid_lines = get_requests(fh, 'GET')
bytestrs = get_bytestrs(valid_lines)
valid_bytestrs = get_non_redirects(bytestrs)
print(valid_bytestrs)
