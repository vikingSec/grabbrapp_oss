
# https://github.com/vikingSec/grabbrapp_oss/golang/pull_ssl_cert
# This Golang code will utilize the GrabbrApp API to pull down SSL certificate information on a domain.
# NOTE: You can obtain your API key by going to grabbrapp.io/user if you already have an account, or go to grabbrapp.io/signup to sign up for a free account
# INPUT:
# 	arg1 - Domain - The domain that you would like to look up
# 	.env - ENV file - An environment variable file containing your EMail and the API key associated with your email. Please reference the .sampleenv file
# OUTPUT:
# 	This will output to a file named {domain}_ssl.json . If you would like for it to simply output to stdout, you can pass in the --out flag like the second example given below
# Example:
# 	go run main.go youtube.com
# 	go run main.go youtube.com --out
import os, sys
from dotenv import load_dotenv

load_dotenv()
def main():

    domain = sys.argv[1]
    apikey = os.getenv("GRABBRAPP_APIKEY")
    email = os.getenv("GRABBRAPP_EMAIL")
    if apikey == None:
        print("No API key in ./.env file")
        return
    
    if email == None:
        print("No email in ./.env file")
        return
    domain = domain.split("://")[1]
	postdata = {
		Email:  "mitch@grabbrapp.io",
		Apikey: "5fa62d6429e17c82e317513bea549581",
		Domain: domain,
	}

if __name__ == "__main__":
    main()