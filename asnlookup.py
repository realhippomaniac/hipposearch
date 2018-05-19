import requests, subprocess, sys, socket, shodan, string
try:
    lol = socket.gethostbyname(sys.argv[1])
except:
    sys.exit()
key = "Enter Shodan Key Here!"
try:
    api = shodan.Shodan(key)
    results = api.host(lol)
    lol = results['asn']
except Exception as e:
    print("Err: %s" % e)
asn = lol.strip("AS")
r = requests.get("http://viewdns.info/asnlookup/?asn=%s" % asn)
a = r.text
b = a.replace("</br>", "\n")
c = b.replace("<br>", "\n")
subprocess.call("touch /tmp/tmp")
fd = open("/tmp/tmp", "wb")
fd.write(c)
fd.close(c)
print("[+] ASN LOOKUP [+]\n+-+-+-+-+-+-+-+-+-+-+-+")
print("Orgnization:    " + results['org'])
subprocess.call('cat /tmp/tmp | grep -e remarks -e  org-name -e OrgTechHandle -e as-name -e as-block -e OrgName -e ASName | uniq -u; grep -Eio "AS-[A-Z]+$" /tmp/tmp | sort | uniq -u') 
subprocess.call('rm /tmp/tmp')
print("+-+-+-+-+-+-+-+-+-+-+-+\n")


