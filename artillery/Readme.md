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

### Our first load test

To start with, run a quick test against this single endpoint:
* Run `npm install` in this `artillery` directory to install the tool
* Try running `npx artillery quick http://asciiart.artillery.io:8080/dino` to fire off requests

> Artillery recommend installing the tool globally with `npm install -g artillery`, in which case we could run these tests without the npx prefix; we have chosen to isolate that instead, and to specify the version, by using a local `package.json`.

Artillery will produce reports for each 10 second period as it runs, and then a final summary report, which should look something like:

```
All VUs finished. Total time: 3 seconds

--------------------------------
Summary report @ 15:20:37(+0000)
--------------------------------

http.codes.200: ................................................................ 100
http.downloaded_bytes: ......................................................... 54500
http.request_rate: ............................................................. 84/sec
http.requests: ................................................................. 100
http.response_time:
  min: ......................................................................... 25
  max: ......................................................................... 46
  mean: ........................................................................ 29.6
  median: ...................................................................... 29.1
  p95: ......................................................................... 36.2
  p99: ......................................................................... 40.9
http.responses: ................................................................ 100
vusers.completed: .............................................................. 10
vusers.created: ................................................................ 10
vusers.created_by_name.0: ...................................................... 10
vusers.failed: ................................................................. 0
vusers.session_length:
  min: ......................................................................... 330.4
  max: ......................................................................... 426.2
  mean: ........................................................................ 356.6
  median: ...................................................................... 347.3
  p95: ......................................................................... 368.8
  p99: ......................................................................... 368.8
```

Take a moment to read over those stats, and understand those; note that all "time" results are measured in milliseconds.

`pXX` refers to the XXth percentile, e.g. `p95` refers to the 95th percentile, so in this case a `p95` value of 36.2 means that 95% of responses were handled in under 36.2 milliseconds. Why do you think that's a specific stat that Artillery outputs?

Take a moment to discuss this with your room, before you read on.

<details> <summary>Why use p95 or p99?</summary> 

In many scenarios, we care most about some form of _average_ result, but not always. In particular, it's easy for those to be skewed:
* If one request takes 1 second, but nine requests take 10 milliseconds, the _mean_ is going to be ~100ms; quite a misleading average!
* Likewise, the median can miss out a long tail; if 60% of results take 10ms, but 40% take 500ms, then a median of 10ms is equally misleading

By comparison, a p95 of 50ms tells us that 95% of requests took under 50ms; it doesn't give us as much specific info, but it does assure us that most requests were met in time. 

Given that network response times are often quite variable - e.g. based on other traffic in the network, the route a packet takes, or even the physical location of the device testing - using this approach is a good way to reduce the noise but still focus on "did the majority of requests get satisified in a reasonable timeframe".

</details>

As our load-testing jobs get longer, we could easily lose info from the outputted stats. Run the test again, but this time [add the `-o` flag and specify a json file](https://www.artillery.io/docs/reference/cli/run#--output---create-a-json-report) to write the summary results to.

Check out those stats, how many requests were made total? What was the 75th percentile response time?

You can view those stats better by generating a HTML page through the `report` option:
* `npx artillery report <json_file>`

> If using VSCode, there are several "Open In Browser" extensions that will give you an easy option to view the HTML in your Browser without navigating File Explorer/Finder.

### Adding more structure

Next, we'll run through a similar example to [the Artillery tutorial](https://www.artillery.io/docs/get-started/first-test).

Take a quick look at the `first-test.yml` file, and then trigger your first test with `npx artillery run first-test.yml`

As it runs, read [the Artillery docs about how Virtual Users work](https://www.artillery.io/docs/get-started/core-concepts#virtual-users). Note that a given "user" maintains its own cookies, so they can handle some degree of statefulness.

Once the test has passed, review its results again.

### Plugins
Enable the plugins section in the yml file, including the `apdex` and `ensure` sections, and run the test again.

Ensure: report success or failure

// discuss apdex
https://www.artillery.io/docs/reference/extensions/apdex

### Playwright

## Extending the test

TODO:
> Can we make smarter tests, e.g. navigating a few pages?