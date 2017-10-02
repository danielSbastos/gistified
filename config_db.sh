#!/usr/bin/env bash

commands=(
  "CREATE DATABASE gistified;"
  "CREATE USER gistified_user WITH PASSWORD 'nopasswd';"
  "GRANT ALL PRIVILEGES ON DATABASE gistified TO gistified_user;"
  "ALTER USER gistified_user CREATEDB;"
)

commands2=(
  "CREATE DATABASE gistified_test;"
  "CREATE USER gistified_test_user WITH PASSWORD 'nopasswd';"
  "GRANT ALL PRIVILEGES ON DATABASE gistified_test TO gistified_test_user;"
  "ALTER USER gistified_test_user CREATEDB;"
)

# TODO: put both commands in one if
if [ $(uname) == 'Darwin' ]
then
  for command in "${commands[@]}"; do psql -U postgres -c "$command"; done
else
  for command in "${commands[@]}"; do sudo -u postgres psql -c "$command"; done
fi

if [ $(uname) == 'Darwin' ]
then
  for command in "${commands2[@]}"; do psql -U postgres -c "$command"; done
else
  for command in "${commands2[@]}"; do sudo -u postgres psql -c "$command"; done
fi
