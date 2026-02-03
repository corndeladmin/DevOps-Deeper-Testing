# Contract Testing with Pact

In this exercise we will motivate and setup contract testing with [Pact](https://docs.pact.io/).

In this folder we have an application (a Restaurant Booking Website) & a backend service/API that it communicates with (the Reservations API).

**[You will need Docker installed to run this exercise](https://docs.docker.com/get-started/get-docker/)**

## Running the example system

To run both services side-by-side please run the following command from this folder:

```
docker compose up --build
```

To run the tests for both services:

```
docker compose -f docker-compose-test.yml up --build
```

## Reviewing the existing tests

Note that we currently have 5 tests:
* 1 Unit Test for the reservation service in [test_reservation.py](./reservations/test_reservation.py)
* 2 Integration Tests for the Flask app reservation service in [test_app.py](./reservations/test_app.py)
* 2 Unit Tests for the reservations client in [test_reservations_client.py](./restaurant/reservations_client.py)

Ideally we'd want to be able to test that the two services work correctly together. Traditionally this would involve creating either an integration or end-to-end test that would require running both services simultaneously. This might not be too complex for our example but if we had complex systems with, say, dozens of services, then this approach could be too resource intensive and time consuming (put simply, this strategy doesn't scale very well!).


## API Updates without Contract Testing

Before we begin implementing contract testing let's see how we might end up this API relationship/contract (without end-to-end tests).

Note that in the scenario here we have a restaurant that wants to use a reservations service to manage its bookings. In this model the consumer is the restaurant website and the API provider is the reservations service.

It's perfectly reasonable for the Restaurant to want to add new features over time, which may require the restaurant asking the service to support new features.

So... what would likely happen in practice is:
1. The restaurant team talks to the reservations team about what features they want
1. The reservations team implement the feature on their end
1. The reservations team publishes the new feature
1. The restaurant team uses the new API feature and (hopefully!) gets what they want
1. Both teams write tests for the new features

Now this approach has some problems:
1. There might be some miscommunication of the requirements of the new feature(s)
1. The restaurant team potentially has to wait a long time between specifying the requirements they want and actually implementing the new feature (they're waiting on the reservations team)
1. Both teams are likely going to have to write tests at the end as well (i.e. extra work/overhead that might get left behind in the name of efficiency)

Contract testing aims to solve some of these problems by putting the test writing front and center. You can think of it as Test Driven Development (TDD) for API tests.

