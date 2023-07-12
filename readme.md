# GrabbrApp Open Source
[GrabbrApp](https://grabbrapp.io)   |   [Twitter](https://twitter.com/grabbrappio)
Hello and welcome!

This repository is for all things GrabbrApp Open Source. Below you'll find some information about what GrabbrApp is, who I am, how to contribute and more. Thanks for swinging by!

## What is GrabbrApp?

[GrabbrApp](https://grabbrapp.io) is a cyber security and threat intelligence startup that makes threat intelligence data collection easier by giving analysts and researchers a platform through which they can download malware from threat actors' servers, scan command-and-control (C2) servers and gather information about malicious infrastructure in a secure and scalable manner. It uses ephemeral (short-living) cloud servers that scan malicious infrastructure and pull down malware for the user, storing the data and malware samples indefinitely for threat researchers to benefit from. The servers are then "detonated" every 2 hours, which ensures the privacy and security of GrabbrApp users by ensuring threat actors will never get access to even the limited data that is passed on to GrabbrApp's servers.

You can sign up for a free account at [grabbrapp.io](https://grabbrapp.io/signup), upgrade to a premium account or email me at the address below for an enterprise account!

mitch@grabbrapp.io

## What is this repository?

The GrabbrApp_OSS repository is my way of making it easier for folks to use GrabbrApp. It will be full of easy-to-use example code and scripts for interacting with the GrabbrApp API. I'll be keeping it up to date, but I look forward to building a community around GrabbrApp as well!

## How can I contribute?

I'm always looking for new contributions to GrabbrApp, and any little thing counts. Whether it's a typo, a new way to word some documentation that's clearer than my chicken scratch or a new way to use the API, I'm opening this repository up to any and all recommendations.

Please submit PR's via this repository with the following information:

- What the PR does
- What you changed
- Why you changed it
- What kind of contribution - bug fix, new feature/script/capability, typo fix, documentation, etc.

Also feel free to submit questions, feature requests and more for the application or API via the community or PR tab.

## How is this repo laid out?

I'll have example code laid out in separate sub-folders in this repository labeled by the language the code is written in. I'm going to try my best to mirror all example code across as many languages as possibly by maintaining the same naming conventions between languages, so `python/pull_ssl_cert` and `golang/pull_ssl_cert` are both example scripts that do the same thing.

If you have a favorite language that you like to use for threat intelligence or cyber security research, mirroring code to your preferred language is a fantastic way to contribute! Please document your code as much as possible and submit a PR via the guidelines above.