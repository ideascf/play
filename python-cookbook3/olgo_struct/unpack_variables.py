# * expression, can use unpack sequence, such as list, tuple, str, etc.

#### sample 1 #####
print('\n...sample 1...')
record = ('dave', 'dave@example.com', '111111', '2222222', '333333')
name,email,*mobiles = record
print(name, email, mobiles)

#### sample 2, compare front's average with last one
print('\n...sample 2...')
*a,b = [1,2,3,4,5,6,7,8]
print(sum(a)/len(a), b)


#### sample 3, iter list which has variable value
print('\n...sample 3...')
records = [
    ('banana', 1, 2),
    ('organge', 1, 2, 3),
    # ('watermealon'), # Not valid, must have one
    ('pear', 1),
]

for tag, *args in records:
    print(tag, *args)

#### sample 4, parse command line
line = 'bobody:*:-2:-2:Unprivieged user:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, fields, homedir, sh)