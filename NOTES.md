API endpoints in Tautulli exist in one of two places:
- A non-private method directly in [`api2.py`](https://github.com/Tautulli/Tautulli/blob/master/plexpy/api2.py)
- Added to the API via the [`addtoapi` decorator](https://github.com/search?q=repo%3ATautulli%2FTautulli%20%20addtoapi&type=code), to [cut down on code-reuse](https://github.com/Tautulli/Tautulli/blob/master/plexpy/helpers.py#L70)
  - Usually any code labeled with the decorator would exist in [`webserve.py`](https://github.com/Tautulli/Tautulli/blob/master/plexpy/webserve.py)
