#!/usr/bin/env bash

commands=(
  "CREATE DATABASE gistified;"
  "CREATE USER gistified_user WITH PASSWORD 'nopasswd';"
  "GRANT ALL PRIVILEGES ON DATABASE gistified TO gistified_user;"
  "ALTER USER gistified_user CREATEDB;"
)

if [ $(uname) == 'Darwin' ]
then
  for command in "${commands[@]}"; do psql -U postgres -c "$command"; done
else
  for command in "${commands[@]}"; do sudo -u postgres psql -c "$command"; done
fi
