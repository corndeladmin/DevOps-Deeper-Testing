# Selenium

## Before you start

This assumes you have:
- Poetry installed on your machine
  - If not, install it [according to the instructions here](https://python-poetry.org/docs/#installation). 
- Chrome installed
  - The test can easily be adjusted for FireFox or Safari if you prefer those.

## What is Selenium?

[Selenium](https://www.selenium.dev/) is a popular open-source UI testing library. It creates language-specific bindings for programmatically controlling a web browser so you can write tests in almost any mainstream programming language, including Python. Let’s look at how you can use Selenium, with Python, to automate UI interactions.

To run Selenium, you'll need a web driver for a browser that you have installed locally. Recent versions of Selenium should install that for you when it runs, but you can find web drivers to download yourself listed [in the selenium docs](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver). 

## Try it out

Set up the project with `poetry install` from the `e2e-selenium` folder.

You should then be able to run the existing test with `poetry run pytest` - check that you can see a browser appear and navigate Google without input!

> If you aren't using Chrome, take a look at the `.env` file and adjust the variable to run the browser of your choice.

## Now it's your turn

### Extend the steps
Have a play with the Selenium code written, and extend the test to click on the first linked website that appears.

> Without control over how Google shows the information on the page, this may not be as easy as it sounds!

Feel free to hardcode values to start with (e.g. the link text), but ultimately we want this to work for different typed text.

You may want to look at the docs for:
* [Locating by XPath](https://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath)
* [Locating by Link Text](https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text)

> Selenium can be a little slow to fire up, so your feedback loop for testing different code can easily crawl! A good pattern is to add an appropriate breakpoint and run your test in debugging mode, so you can take advantage of the Debug Console for quick experimentation of different code.

<details> <summary>Hint</summary>

Unfortunately, if you try getting the first `<a>` tag, you'll find it's not the desired search result.

First we need to find a consistent route to navigate the HTML that we can describe. Can you find any ids that get us to the correct part of the page?

One way to do this is to find the first anchor tag (`<a>`) that sits within the search results.

We can do that either as part of a complex XPath string, or by iterating over anchor tags in Python.

</details>

### Save an output screenshot

Debugging Selenium tests can get fiddly, particularly with the pace at which the browser often navigates. Try saving a screenshot with the `driver.save_screenshot(<filename>)` function at different stages of your test.

### Speed it up

Now that it's working, try switching your driver into "headless mode" - this runs without the browser UI appearing, and is a common requirement for environments that lack a display (e.g. allowing you to run these tests within a container).

<details> <summary>Hint</summary> 

```python
  opt = webdriver.ChromeOptions()
  opt.add_argument("--headless=new")
```
</details>

### Test your own sites

Add a new test file in the `tests` folder, and point your test at another website, for example one that you work on or with. Can you get the test to navigate through a simple real user journey?

> If you don't have an appropriate website to trial, we'll shortly use [the Playwright demo site](https://demo.playwright.dev/todomvc) to test Playwright, so you can use that to get a comparison.

> Alternatively, have a go at adding useful end-to-end tests to the [Chessington testing exercise](https://github.com/corndeladmin/Devops-Chessington-Python) - can you get Selenium to play out a game of chess?

### Further reading

- [Selenium's documentation](https://www.selenium.dev/documentation/)
- [Selenium Pytest integration plugin](https://pytest-selenium.readthedocs.io/en/latest/user_guide.html)
  - Adds a number of useful features to simplify management of large Selenium repositories