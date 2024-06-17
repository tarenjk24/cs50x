-- Keep a log of any SQL queries you execute as you solve the mystery.
-- checking cities to narrow down the place.
SELECT city, id FROM airports;
SELECT origin_airport_id FROM flights ;

--checking crime reports.
SELECT id, day, description
FROM crime_scene_reports
WHERE street = 'Humphrey Street';

SELECT day, street, description, month
FROM crime_scene_reports
WHERE description like "%bakery%";

-- reading interviews.
SELECT name, transcript, day, month FROM interviews WHERE  transcript LIKE '%bakery%';

--witness 1: Ruth
SELECT bakery_security_logs.activity, bakery_security_logs.license_plate, people.name FROM people
JOIN bakery_security_logs ON people.license_plate=bakery_security_logs.license_plate
WHERE day  = 28 AND month = 7 AND hour = 10 AND minute BETWEEN 15 AND 25
ORDER BY day;


-- witness 2: Eugene--
SELECT bank_accounts.person_id, people.name, people.license_plate, bank_accounts.account_number,  atm_transactions.transaction_type
FROM people
INNER JOIN bank_accounts ON bank_accounts.person_id=people.id
INNER JOIN atm_transactions ON bank_accounts.account_number=atm_transactions.account_number
WHERE day =28 AND month =7 AND atm_transactions.atm_location ='Leggett Street' AND atm_transactions.transaction_type='withdraw'
ORDER BY day;


-- witness 3: Raymond--

SELECT  phone_calls.caller, phone_calls.duration, people.name
FROM phone_calls
JOIN people ON phone_calls.caller = people.phone_number
WHERE day = 28 AND month = 7 AND duration < 60;



--escape city
SELECT  flights.id, flights.day, flights.origin_airport_id, flights.destination_airport_id, airports.full_name, airports.city
FROM airports
JOIN flights ON flights.origin_airport_id=airports.id
WHERE day  = 29 AND month = 7 AND city='Fiftyville'  AND origin_airport_id = 8 ORDER BY hour, minute ;


-- collecting informations
SELECT name
FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts ON  bank_accounts.person_id= people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE  bakery_security_logs.month = 7  AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute  BETWEEN 15 AND 25
AND atm_transactions.atm_location = 'Leggett Street'
AND atm_transactions.month = 7  AND atm_transactions.day = 28
AND atm_transactions.transaction_type = 'withdraw'
AND phone_calls.month= 7 AND phone_calls.day = 28
AND phone_calls.duration < 50;


--who is thief
SELECT people.name
FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE passengers.flight_id = 36 AND people.name IN('Bruce','Diana');

--The ACCOMPLICE

SELECT p.name AS receiver
FROM phone_calls
JOIN people ON phone_calls.caller = people.phone_number
JOIN people p ON phone_calls.receiver = p.phone_number
WHERE people.name ='Bruce' AND phone_calls.month=7
AND phone_calls.day=28
AND phone_calls.duration <60;