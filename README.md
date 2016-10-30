# Bioskop ML

The recommendations part of the Software Engineering Project, Bioskop.

## What It Does?

Bioskop is a Movie Recommendation Engine based on Collaborative Filtering. On the basis of ratings received from other users and the movies rated by the given user, the user is shown movie recommendation. The recommendation generation script can be run multiple times a day depending on resource and data availability and generate the recommendations for the user. Currently we have implemented it using a relational database MySQL.

## Instructions to set up the database

1. Clone the repository
2. cd into `config/` and run the command `cp config.cfg.sample config.cfg`
3. Fill the `config.cfg` as per your mysql configuration.
4. cd into `schema/` and import the database schema named bioskop.sql into `phpMyAdmin`
5. `cd` into `scripts/` and run `python once.py`

That's it!
