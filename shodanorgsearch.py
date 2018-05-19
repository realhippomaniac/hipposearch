import shodan,sys
key = "Enter Shodan Key Here!"
api = shodan.Shodan(key)
try:
    print("+-+-+-+-+-+-+-+-+-+-+-+")
    results = api.search(sys.argv[1:])
    for result in results['matches']:
        print(result['ip_str'] + '       :        ' + ''.join(result['hostnames']))
    print("+-+-+-+-+-+-+-+-+-+-+-+\n")
except:
    pass
