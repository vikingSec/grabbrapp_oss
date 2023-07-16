
# https://github.com/vikingSec/grabbrapp_oss/python/pull_ssl_cert
# This Python code will utilize the GrabbrApp API to pull down SSL certificate information on a domain.
# NOTE: You can obtain your API key by going to grabbrapp.io/user if you already have an account, or go to grabbrapp.io/signup to sign up for a free account
# INPUT:
# 	arg1 - Domain - The domain that you would like to look up
# 	.env - ENV file - An environment variable file containing your EMail and the API key associated with your email. Please reference the .sampleenv file
# OUTPUT:
# 	This will output to a file named {domain}_ssl.json . If you would like for it to simply output to stdout, you can pass in the --out flag like the second example given below
# Example:
# 	python pull.py youtube.com
# 	python pull.py youtube.com --out
import os, sys, requests, hashlib
from dotenv import load_dotenv

load_dotenv()
def main():
    try:
        domain = sys.argv[1]
    except:
        print("[x] Please run the python file with a domain as the first argument")
    apikey = os.getenv("GRABBRAPP_APIKEY")
    email = os.getenv("GRABBRAPP_EMAIL")
    if apikey == None:
        print("No API key in ./.env file")
        return
    
    if email == None:
        print("No email in ./.env file")
        return
    if "http" not in domain and "https" not in domain:
        domain = "http://"+domain
    postdata = {
		"email":  email,
		"apikey": apikey,
		"domain": domain
	}
    print(postdata)
    url = "https://grabbrapp.io/api/dapi/file"
    res = requests.post(url=url, json=postdata)
    if "--out" in sys.argv:
        print(res.text)
        return
    else:
        md5 = hashlib.md5(res.text.encode('utf-8')).hexdigest()

        f = open("./"+md5,"w")
        f.write(res.text)
        f.close()
        return
if __name__ == "__main__":
    main()