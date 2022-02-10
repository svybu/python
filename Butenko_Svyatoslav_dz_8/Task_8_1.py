import re
result = {}
def email_parse(email_address):
    try:
        result1 = re.match(r'^([a-z0-9]+[\\._]?[a-z0-9]+)[@](\w+[.]\w{2,3}$)', email_address).group(1)
        result2 = re.match(r'^([a-z0-9]+[\\._]?[a-z0-9]+)[@](\w+[.]\w{2,3}$)', email_address).group(2)
        result['username'] = result1
        result['domain'] = result2
        print(result)
    except:
        msg = 'wrong email: ', email_address
        raise ValueError(msg)
email_parse('xaxaxa@gmail.com')