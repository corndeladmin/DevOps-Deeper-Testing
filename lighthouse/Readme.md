# Google Lighthouse

[Lighthouse](TODO) is an open-source tool designed for improving websites, particularly with a focus on:
* Performance - fast page loads
* Accessibility - how easy is your site to navigate for users

Lighthouse can be run in a range of ways:
* Within Google Chrome, it can be run from the Lighthouse tab within the Chrome DevTools
  * Accessible through right clicking on a web page in Chrome and selecting Inspect
* Installed through node, which can be used:
  * Directly as a CLI
  * Or programmatically from JavaScript code
* Added as a [Chrome Extension](TODO)

Today we'll run the CLI tool so that we can define our success and failure results consistently, so that we're best placed to integrate our tooling into a Continuous Integration pipeline later down the line.

## Try it out

> Running this tool requires having Google Chrome installed on your machine.

Run `npm install` within this folder to install the lighthouse tool, and then run it using:
```
npx lighthouse https://developer.chrome.com/docs/lighthouse/overview --view
```

Once the test is complete, you'll see a report load up with various scores assigned to different aspects of the site's performance. Take a moment to read through this, what does the site score well on, and what not so well?

If you work on a project that creates or relies on a specific webpage, try running Lighthouse against that next. How does it score? Are you surprised?

> As an alternative to outputting the HTML directly, we can also generate a JSON output by passing the `--output json --output-path output.json` flags, which can be shared with others, and can be viewed on the [Google Lighthouse Viewer](https://googlechrome.github.io/lighthouse/viewer/).

## Defining Success

These reports can be great for providing us with actionable advice & ideas, but they're currently dependent on being opened and reviewed by someone periodically. If instead we can specify pass/fail criteria for our reports, then we can potentially take this further and ensure that once we have a score we are happy with, we are notified if that drops below our chosen thresholds.

In order to add assertions and requirements to our tool, we will need to use the Lighthouse CI tool.

TODO clean:
Create the config file (`.lighthouserc.json`):
```json
{
  "ci": {
    "collect": {
      "url": ["https://developer.chrome.com/docs/lighthouse/overview"],
      "numberOfRuns": 1
    },
  }
}
```

Collect - run the test and store results locally in a `.lighthouseci` folder.
```
npx lhci collect
```

Take a quick look over the folder.

Add an assertions block under the collect block:
```json
{
  "ci": {
    "collect": { ... },
    "assert": {
      "preset": "lighthouse:recommended",
      "assertions": {
        "unused-css-rules": ["warn", {"maxScore": 0}],
        "unminified-javascript": ["warn", {"maxScore": 0}]
      }
    }
  }
}
```

TODO:
DOCS: https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/getting-started.md
Options here: https://github.com/GoogleChrome/lighthouse/blob/v5.5.0/lighthouse-core/config/default-config.js#L375-L407

## performance budgets?
https://github.com/GoogleChrome/lighthouse/blob/main/docs/performance-budgets.md






