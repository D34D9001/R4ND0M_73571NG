curl "https://api.m3o.com/v1/user/SendVerificationEmail" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $M3O_API_KEY" \
-d '{
  "email": "$EMAIL",
  "failureRedirectUrl": "https://m3o.com/verification-failed",
  "fromName": "Kaotic",
  "redirectUrl": "https://m3o.com",
  "subject": "Email verification",
  "textContent": "Hi there,\n\nPlease verify your email by clicking this link: $micro_verification_link"
}'
