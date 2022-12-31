with open('sample.text','r')  as  f:
    a=f.read()
    with open('sample.text', 'w') as f: #write always overwrites these things
        a = f.write('me')
    print(a)