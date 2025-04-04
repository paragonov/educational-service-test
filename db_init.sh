#!/bin/bash

psql -U postgres  <<-EOSQL
  CREATE DATABASE app;
  GRANT ALL PRIVILEGES ON DATABASE app TO postgres;

EOSQL
