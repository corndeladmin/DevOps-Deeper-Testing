# ZAP

## Before you start

This exercise assumes you have [Docker installed on your machine](https://docs.docker.com/engine/install/). We will cover Docker in detail later in the course, so for now you will only need to run provided commands. 

## What is it?

> Read the warnings about trying this against live site!
https://www.zaproxy.org/faq/is-there-any-danger-when-scanning-with-zap-against-a-live-website-e-g-create-delete-update-corrupt-data/

## Try it out

Later on in the course we'll try manually breaking into the [Damn Vulnerable Web App](TODO:LINK), so today we'll try letting ZAP scan another open-source vulnerability hotspot - the [Juice Shop](TODO: LINK).

Because of the security concerns, we'll be hosting this ourselves!

Docker or download the tool directly.

`docker compose up`

http://localhost:8080/zap/

Scan the URL: `http://juice:3000`

Results:
* Spider: trying to track down different URLs, see if any look suspicious or interesting!
* Active Scan: Investigating what's actually present at all those URLs - are there any concerns?
