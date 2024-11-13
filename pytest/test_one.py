
def test_one():
    print('hello')

def test_grater():
    n=int(input('enter : '))
    if n>0:
        return 'grater'
    else:
        return 'less'

val=test_grater()
print(val)