package main

/*
	https://github.com/vikingSec/grabbrapp_oss/golang/pull_file
	This Golang code will utilize the GrabbrApp API to pull down a file from a URL.
	NOTE: You can obtain your API key by going to grabbrapp.io/user if you already have an account, or go to grabbrapp.io/signup to sign up for a free account
	INPUT:
		arg1 - URL - The URL of the file you'd like to download
		.env - ENV file - An environment variable file containing your EMail and the API key associated with your email. Please reference the .sampleenv file
	OUTPUT:
		This will output to a file named by the MD5 hash of the file you're downloading . If you would like for it to simply output to stdout, you can pass in the --out flag like the second example given below
	Example:
		go run main.go youtube.com
		go run main.go youtube.com --out
*/
import (
	"bytes"
	"crypto/md5"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"

	"github.com/joho/godotenv"
	"golang.org/x/exp/slices"
)

type PostData struct {
	Email  string `json:"email"`
	Apikey string `json:"apikey"`
	Domain string `json:"domain"`
}

func main() {
	err := godotenv.Load()
	if err != nil {
		panic(err)
	}
	apikey := os.Getenv("GRABBRAPP_APIKEY")
	email := os.Getenv("GRABBRAPP_EMAIL")
	if apikey == "" {
		panic("[x] API Key (under the environment variable GRABBRAPP_APIKEY) not found")
	}
	if email == "" {
		panic("[x] EMail (under the environment variable GRABBRAPP_EMAIL) not found")
	}
	if len(os.Args) < 2 {
		panic("[x] Please pass a domain you would like to look up as an argument")
	}
	domain := os.Args[1]
	// domain = strings.Split(domain, "://")[1]
	postdata := PostData{
		Email:  email,
		Apikey: apikey,
		Domain: domain,
	}
	postdatabuffer, err := json.Marshal(postdata)
	fmt.Println(string(postdatabuffer))
	url := "http://localhost:3000/api/dapi/file"
	// url := "http://localhost:3000/api/dapi/ssl/domain"
	client := http.Client{}
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(postdatabuffer))
	req.Header.Add("content-type", "application/json")
	res, err := client.Do(req)
	resbody, err := io.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}
	if slices.Contains(os.Args, "--out") {
		fmt.Println(string(resbody))
	} else {
		md5 := md5.Sum(resbody)
		f, err := os.OpenFile(fmt.Sprintf("./%s", fmt.Sprintf("%x", md5)), os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		f.Write(resbody)
		f.Close()
		if err != nil {
			panic(err)
		}
	}

	// fmt.Println(string(resbody))
}
