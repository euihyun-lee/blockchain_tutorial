curl "localhost:"$1"/tx" -H "Content-Type: application/json" -d '{"from": "'$2'", "to":"'$3'", "amount": '$4'}'

