# Artillery

## What is it?

Artillery is a load testing library; it is designed for triggering large numbers of requests to a service and monitoring how the service under test handles the load.

### An aside on load testing

Running load tests doesn't always have to be hard, but _designing_ good load tests typically is. 

Before setting up load tests, consider what you're actually hoping to achieve with them:
* Do you want to check the system is performing at its usual pace under normal load?
* Do you want to check that it can handle spikes in traffic beyond normal levels?
* Do you want to find out at what level of traffic the system struggles or gives up?
* Do you want to check that the system degrades gracefully under heavy load?

Each of these tests will demand a slightly different configuration, and a different analysis of the results.

## Alternatives?
// TODO
Gatling?

### Disclaimer

You should be wary of just running load tests against arbitrary sites; this is potentially a criminal offence!

Thankfully, Artillery offer a site that they host and allow us to use.

## Try it out

First off, we should know our target! Check out Artillery's practice Dino: <http://asciiart.artillery.io:8080/dino>

Next, we'll run a similar example to [the Artillery tutorial](https://www.artillery.io/docs/get-started/first-test).

Run `npm install` and then trigger your first test with `npm run start`.

TODO:
> read the first-test.yml file, understand what it's saying
> what is apdex?
> Why do we use p99?

## Extending the test

TODO:
> Can we make smarter tests, e.g. navigating a few pages?