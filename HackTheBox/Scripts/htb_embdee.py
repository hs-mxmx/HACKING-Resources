
import requests
from BeautifulSoup import BeautifulSoup
import hashlib
import re


problem_url = "http://docker.hackthebox.eu:35416/"

def login_page(url):
    #Set current session
    r = requests.Session()
    problem_url = r.get(url)
    parsed_html_content = BeautifulSoup(problem_url.content)

    #Find string area
    get_textarea = parsed_html_content.find("h3")

    #Extract string
    string = str(get_textarea)
    string_left = string[19:]
    string_right = string_left[:-5]
    string = string_right

    #Generate hash from extracted string
    hash = hashlib.md5(string).hexdigest()

    #Send request
    data = {'hash': hash}
    result = r.post(url = url, data = data)
    print("\n" + result.text)


    #Extract flag
    parsed_html_flag = BeautifulSoup(result.content)
    get_flag = parsed_html_flag.findAll("p")
    flag = str(get_flag)
    flag_left = flag[19:]
    flag_right = flag_left[:-5]

    #Results
    print("\n[+] String extracted: " + string)
    print("[+] MD5 Hash: " + hash)
    print("[*] FLAG: " + str(flag_right) + "\n")


    # T E S T I N G   R E G E X
    print("\n[R E G E X  T E S T]")
    purl = r.get(url)
    purl = re.search("<h3 align='center'>.*</h3>",purl.text)
    purl = re.search(">.*<",purl.group(0))
    purl = re.search("[^>|<]+", purl.group(0))


    #Results
    print("\n[+] String: " + purl.group(0))
    print("[+] MD5 Hash: " + hash)
    print("[*] FLAG: " + str(flag_right) + "\n")

login_page(problem_url)

#html_code = login_page(login, url, payload)
#print(html_code)