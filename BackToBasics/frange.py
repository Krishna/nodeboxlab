
#
# from: http://mail.python.org/pipermail/python-list/2006-April/378202.html
#
def frange(start, to, step):
    while start < to:
        yield start
        start += step


for x in frange(1.0, 2.0, 0.1):
    print x