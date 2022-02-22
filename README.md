# Cross-Chain Django SSO Application

## Instructions

#### Start the SSO service
```bash
source .env/bin/activate
cd ./user
python manage.py runserver 0.0.0.0:10000
```

#### Install a virtual environment
```bash
virtualenv -p python3 .env
source .env/bin/activate
pip install -r requirements.txt
```

#### Start the Auth service
```bash
source .env/bin/activate
cd ./auth
python manage.py migrate && python manage.py runserver 0.0.0.0:10000
```

#### Start the Ethereum service
```bash
source .env/bin/activate
cd ./eth
python manage.py migrate && python manage.py runserver 0.0.0.0:10001
```

#### Start the Solana service
```bash
source .env/bin/activate
cd ./sol
python manage.py migrate && python manage.py runserver 0.0.0.0:10002
```

#### Start the Polygon service
```bash
source .env/bin/activate
cd ./pol
python manage.py migrate && python manage.py runserver 0.0.0.0:10003
```

#### Start the Binance service
```bash
source .env/bin/activate
cd ./bnb
python manage.py migrate && python manage.py runserver 0.0.0.0:10004
```

## Authentication

#### Login to create a new User on the SSO server
```bash
curl --cookie-jar 'session.jar' -X POST 'http://0.0.0.0:10000/users/' \
    -H 'content-type: application/json' \
    -d '{"wallet": "0xdea6e2a13d869d7d9b4c6078a9ac9ebe4ee597db", "password": "loremipsumdolor"}'
```
```bash
{
  "wallet": "0xdea6e2a13d869d7d9b4c6078a9ac9ebe4ee597db",
}
```

#### Check if you are authenticated by fetching your session
```bash
curl --cookie "session.jar" -X GET http://0.0.0.0:10000/session/
```
```bash
{
  "wallet": "0xdea6e2a13d869d7d9b4c6078a9ac9ebe4ee597db",
}
```

#### Get your balance on Ethereum
```bash
curl --cookie "session.jar" -X GET http://0.0.0.0:10001/balance/
```
```bash
{
  "wallet": "0xdea6e2a13d869d7d9b4c6078a9ac9ebe4ee597db",
  "balance": 488492839234,
  "network": "Ethereum"
}
```

#### Get your balance on Solana
```bash
curl --cookie "session.jar" -X GET http://0.0.0.0:10002/balance/
```
```bash
{
  "wallet": "0xdea6e2a13d869d7d9b4c6078a9ac9ebe4ee597db",
  "balance": 12912,
  "network": "Solana"
}
```

#### Get your balance on Polygon
```bash
curl --cookie "session.jar" -X GET http://0.0.0.0:10003/balance/
```
```bash
{
  "wallet": "0xdea6e2a13d869d7d9b4c6078a9ac9ebe4ee597db",
  "balance": 43,
  "network": "Polygon"
}
```

#### Get your balance on Binance
```bash
curl --cookie "session.jar" -X GET http://0.0.0.0:10004/balance/
```
```bash
{
  "wallet": "0xdea6e2a13d869d7d9b4c6078a9ac9ebe4ee597db",
  "balance": 889382984982,
  "network": "Binance"
}
```
