#!/usr/bin/env bash

set -e

SHORT_HASH=`git rev-parse --short=7 HEAD`
ENV=$(echo "$1" | awk '{print tolower($0)}')
PROJECT="alvtime"
KEY_VAULT="$PROJECT$ENV"
RESOURCE_GROUP_NAME="rg-alvtime-$ENV-westeurope"
KUBERNETES_CLUSTER_NAME="aks-alvtime-$ENV-westeurope"

function getSecret() {
  az keyvault secret show --vault-name $KEY_VAULT --name $1 | jq '.value' -r
}

echo "Getting secrets from key vault $KEY_VAULT..."
HOSTNAME="$(getSecret hostname)"
REPORT_USER_PERSONAL_ACCESS_TOKEN="$(getSecret report-user-personal-access-token)"
SLACK_ADMIN_USERS="$(getSecret slack-admin-users)"
SLACK_BOT_TOKEN="$(getSecret slack-bot-token)"
SLACK_SIGNING_SECRET="$(getSecret slack-signing-secret)"
SP_ALVTIME_AUTH_SLACK_APP_SECRET="$(getSecret sp-alvtime-auth-slack-app-secret)"
MONGO_DB_ENCRYPTION_KEY="$(getSecret mongo-db-encryption-key)"
MONGO_DB_CONNECTION_STRING="$(getSecret mongo-db-connection-string)"
MONGO_DB_PRIMARY_KEY="$(getSecret mongo-db-primary-key)"
SQL_CONNECTION_STRING="$(getSecret sql-connection-string)"
