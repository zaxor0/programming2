-- Keep a log of any SQL queries you execute as you solve the mystery

-- crime scene notes
SELECT description FROM crime_scene_reports WHERE (year = 2025 AND month = 7 AND day = 28 AND street = "Humphrey Street" AND description LIKE "%duck%");

-- interviews from crime
SELECT * FROM interviews WHERE (year = 2025 AND month = 7 AND day = 28 AND transcript LIKE "%thief%");

-- people who made calls on the day of the theft for less than 60 seconds,
SELECT name FROM people WHERE phone_number in (SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60 ));

-- people who left the parking lot
SELECT name FROM people WHERE license_plate in (SELECT license_plate FROM bakery_security_logs WHERE (year = 2025 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute < 25));

-- people from people who withdrew cash
SELECT name FROM people WHERE id in (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")));

-- people who have the first flight out of fiftyville tomorrow
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1));

-- people who did all four
SELECT name FROM people WHERE name IN (SELECT name FROM people WHERE phone_number in (SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60 ))) AND name IN (SELECT name FROM people WHERE license_plate in (SELECT license_plate FROM bakery_security_logs WHERE (year = 2025 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute < 25))) AND name IN (SELECT name FROM people WHERE id in (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")))) AND name IN (SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1)));

-- who did bruce call?
SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE name = "Bruce") AND (year = 2025 AND month = 7 AND day = 28 AND duration < 60));

-- destination city on the first flight out of Fiftyville
SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1);
