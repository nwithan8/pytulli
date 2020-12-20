Introduction
============

The ``tautulli`` Python modules allows you to interact with a Tautulli instance's API.

This modules covers nearly 100% of Tautulli's available API endpoints.

The module has built-in type and choice checks to prevent users from making incorrect API requests.

Most functions return either a True/False boolean based on the "result" message from the server, or a raw JSON object parsed from the server's "data" response.

A handful of functions will instead return raw strings or bytearrays (in the case of downloading files)

Motivation
**********

Myself alone, I've probably written a dozen Python scripts and bots that interact with Tautulli in one way or another. And each time, I have to write out the API endpoints and parse the response data myself.

I figured it was about time someone made a Python library that can handle that part.