USERNAME=$1
PASSWORD=$2

curl "https://api.m3o.com/v1/user/Login" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $M3O_API_KEY" \
-d '{
  "email": "$USERNAME",
  "password": "$PASSWORD"
}'
