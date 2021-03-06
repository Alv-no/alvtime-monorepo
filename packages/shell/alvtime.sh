#!/usr/bin/env bash

test -z "$ALVTIME_TOKEN" && \
  echo "ALVTIME_TOKEN must be set"

URL="${ALVTIME_URL:-https://api.alvtime.no}"

function fetch() {
  curl --silent \
    --header "Accept: application/json" \
    --header "Authorization: Bearer $ALVTIME_TOKEN" \
    "$@"
}

function post() {
  fetch \
    --request POST \
    --header "Content-Type: application/json" \
    --data "$2" \
    "$1"
}

function timeEntriesPost() {
  local TODAY
  TODAY=$(date +'%Y-%m-%d')
  local DATE=${3:-"$TODAY"}
  post "$URL/api/user/TimeEntries" \
    "[{\"date\": \"$DATE\", \"value\": $2, \"taskId\": $1 }]"
}

function multiTimeEntriesPost() {
  # Set file to filename or stdin
  local file=${1:--}
  local OBJECTS=''

  # Read each line of file or stdin
  while IFS= read -r LINE; do
    # Create array of each value in the line
    read -ra ARGS <<< "$LINE"
    OBJECTS="$OBJECTS,{\"date\": \"${ARGS[0]}\", \"value\": ${ARGS[2]}, \"taskId\": ${ARGS[1]} }"
  done < <(cat -- "$file")

  post "$URL/api/user/TimeEntries" \
    "[${OBJECTS:1}]"
}

function holidays() {
  local CURRENT_YEAR
  CURRENT_YEAR=$(date +%Y)
  local YEAR=${1:-"$CURRENT_YEAR"}
  fetch "$URL/api/holidays?year=$YEAR"
}

test "tasks" = "$1"  && \
  fetch "$URL/api/user/tasks"

# Example:
# ./alvtime.sh hours 2019-11-18 2021-11-21
# Returns your registered hours between the two dates
test "hours" = "$1"  && \
  fetch "$URL/api/user/TimeEntries?fromDateInclusive=$2&toDateInclusive=$3"

# Example:
# ./alvtime.sh register 14 3.5 2021-02-11
# Registers 3.5 hours to task id 14 on date 2021-02-11
test "register" = "$1"  && \
  timeEntriesPost "$2" "$3" "$4"

# Example:
# ./alvtime.sh multiregister data.txt
#
# data.txt contains:
#
# 2021-02-10 14 1.5
# 2021-02-11 14 3
# 2021-02-12 14 5
#
# Registers 1.5 hours to task id 14 on date 2021-02-10
# Registers 3 hours to task id 14 on date 2021-02-11
# Registers 5 hours to task id 14 on date 2021-02-12
test "multiregister" = "$1"  && \
  multiTimeEntriesPost "$2"

test "ping" = "$1"  && \
  fetch "$URL/api/ping"

test "profile" = "$1"  && \
  fetch "$URL/api/user/profile"

test "availableHours" = "$1"  && \
  fetch "$URL/api/user/availableHours"

test "flexedHours" = "$1"  && \
  fetch "$URL/api/user/flexedHours"

test "payouts" = "$1"  && \
  fetch "$URL/api/user/payouts"

test "holidays" = "$1"  && \
  holidays "$2"
