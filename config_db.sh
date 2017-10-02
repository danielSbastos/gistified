#!/usr/bin/env bash

commands_dev=(
  "CREATE DATABASE gistified;"
  "CREATE USER gistified_user WITH PASSWORD 'nopasswd';"
  "GRANT ALL PRIVILEGES ON DATABASE gistified TO gistified_user;"
  "ALTER USER gistified_user CREATEDB;"
)

commands_test=(
  "CREATE DATABASE gistified_test;"
  "CREATE USER gistified_test_user WITH PASSWORD 'nopasswd';"
  "GRANT ALL PRIVILEGES ON DATABASE gistified_test TO gistified_test_user;"
  "ALTER USER gistified_test_user CREATEDB;"
)

if [ $(uname) == 'Darwin' ]
then
  for command in "${commands_dev[@]}"; do psql -U postgres -c "$command"; done
  for command in "${commands_test[@]}"; do psql -U postgres -c "$command"; done
else
  for command in "${commands_dev[@]}"; do sudo -u postgres psql -c "$command"; done
  for command in "${commands_test[@]}"; do sudo -u postgres psql -c "$command"; done
fi
