# Selenium

## What is Selenium?

[Selenium](https://www.selenium.dev/) is a popular open-source UI testing library. It creates language-specific bindings for programmatically controlling a web browser so you can write tests in almost any mainstream programming language, including Python. Let’s look at how you can use Selenium, with Python, to automate UI interactions.

To run Selenium, you'll need a web driver for a browser that you have installed locally. Recent versions of Selenium should install that for you when it runs, but you can find web drivers to download yourself listed [in the selenium docs](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver). 

## Try it out

This assumes you have poetry installed on your machine; if not, install it [according to the instructions here](https://python-poetry.org/docs/#installation). 

The test as written also assume that you have Chrome installed, but offers alternatives for FireFox or Safari if you prefer those.

Set up the project with `poetry install`.

You should then be able to run the existing test with `poetry run pytest` - check that you can see a browser appear and navigate Google without input!

> If you aren't using Chrome, take a look at the `.env` file and adjust the variable to run the browser of your choice.

