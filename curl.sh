#curl -X POST http://localhost:5000/temperature -H "Content-Type: application/json" -d '{\"counter\": 1234, \"values\": [{\"id\": \"1\", \"temp\": 11.75}, {\"id\": \"2\", \"temp\": 35.31}, {\"id\": \"3\", \"temp\": 29.69}], \"location\": \"PI-2\"}'
curl -X POST http://localhost:5000/temperature -d '{\"counter\": 1234, \"values\": [{\"id\": \"1\", \"temp\": 11.75}, {\"id\": \"2\", \"temp\": 35.31}, {\"id\": \"3\", \"temp\": 29.69}], \"location\": \"PI-2\"}'

