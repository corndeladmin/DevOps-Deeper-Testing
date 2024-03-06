# ZAP

## Before you start

This exercise assumes you have [Docker installed on your machine](https://docs.docker.com/engine/install/). We will cover Docker in detail later in the course, so for now you will only need to run provided commands. 

## What is it?

ZAP (Zed Attack Proxy) is an open source tool provided by OWASP (Open Worldwide Application Security Project) designed for web scanning to identify vulnerabilities to help teams to improve their security.

The tool is designed to scan for URLs and evaluate whether vulnerabilities are potentially present on the site.

> Since the tool is designed to simulate bad actors, it is import to [read the warnings about trying this against live site!](https://www.zaproxy.org/faq/is-there-any-danger-when-scanning-with-zap-against-a-live-website-e-g-create-delete-update-corrupt-data/)

## Try it out

Later on in the course we'll try manually breaking into the [Damn Vulnerable Web App](https://github.com/digininja/DVWA), so today we'll try letting ZAP scan another open-source vulnerability hotspot - the [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/).

Because of the security concerns involved in hosting a site with known vulnerabilities, we'll be hosting this ourselves locally - so do not expose this to the broader internet!

We have set up ZAP and The Juice Shop to run in Docker with:

`docker compose up`

You will then be able to visit the Juice Shop at `http://localhost:3000` so take a quick look round the site.

The ZAP tool is also being hosted, at http://localhost:8080/zap/ so sign in there: this may take a few minutes.

Scan the URL: `http://juice:3000` (note that because of Docker's networking, ZAP will *not* find the Juice's localhost address!)

This will take a while!

Results:
* Spider: trying to track down different URLs, see if any look suspicious or interesting!
* Active Scan: Investigating what's actually present at all those URLs - are there any concerns?
