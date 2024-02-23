# Playwright

Like Selenium, Playwright is an end-to-end testing tool focused on writing tests that interact with a web browser.

TODO
[See the basic actions here](https://playwright.dev/python/docs/writing-tests#basic-actions).

## Try it out

Set up the project with `poetry install`, and then run `poetry run playwright install` to get Playwright to set up the required browsers.

Run `poetry run pytest` to execute the tests. Note that Playwright chooses to default to headless mode, unlike Selenium. Try running them visibly, on Chromium, by adding the `--headed` flag (`poetry run pytest --headed`) or try running them on an alternative browser, e.g. with `--browser firefox`.

## Now it's your turn

A nice feature of Playwright is the ability to generate the code for your tests by interacting with a browser directly. Give that a go, and add a new test exploring the Playwright demo site <demo.playwright.dev/todomvc> by using the `codegen` option:
```
poetry run playwright codegen demo.playwright.dev/todomvc
```

E.g. create a test that:
* Adds two new to-dos to the list
* Checks both are visible
* Marks one as complete, and deletes the other
* Check only the remaining one is visible

[More guidance on using the Codegen tool is available in the docs.](https://playwright.dev/python/docs/codegen-intro#running-codegen)

### Investigate Failures

First, tweak your tests so that they fail, for example in the `test_get_started_link` test you could look for a link with `some text that doesn't exist on the page`.

You should see a timeout error; no link with that text appeared in time, but the stack trace can't offer much more than that. Was the error a case of the page failing to load anything, or did someone just change a key piece of text?

Investigating end-to-end test issues like this can often be a slow affair, involving running the tests locally in a non-headless mode, slowing them down or introducing breakpoints in order to let us diagnose the problem.

Can we investigate those quicker?

When your tests fail, Playwright offers a number of debug helpful options to speed up your troubleshooting. At this stage, it would be nice to reduce the amount of command line flags we need to pass, so you can add a `pytest.ini` file to your `playwright` directory, with the following content:
```ini
[pytest]
# command line options go here, e.g.:
# addopts = --browser firefox
addopts = 
```

Have a play with the following debugging helpers:
* Capturing a screenshot on failure by setting the `--screenshot` flag to `only-on-failure` (or `on`)
* Capturing a video with the `--video` flag (`on`, or `retain-on-failure`)
* Capturing a "trace with the `--tracing` option (`on` or `retain-on-failure`)
  * This will capture the network activity during the test, so it can be replayed later
  * View these through the Trace Viewer either with the `playwright show-trace <path>` command, or [through the online viewer](https://trace.playwright.dev/)

### Further Reading

?