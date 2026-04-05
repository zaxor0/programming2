
# people who made calls on the day of the theft for less than 60 seconds,
SELECT name FROM people WHERE phone_number in (SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60 ));

# people who left the parking lot
SELECT name FROM people WHERE license_plate in (SELECT license_plate FROM bakery_security_logs WHERE (year = 2025 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute < 25));

# People from people who withdrew cash
SELECT name FROM people WHERE id in (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")));

# people who have the first flight out of fiftyville tomorrow
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1));

# people who did all four
SELECT name FROM people WHERE name IN (SELECT name FROM people WHERE phone_number in (SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60 ))) AND name IN (SELECT name FROM people WHERE license_plate in (SELECT license_plate FROM bakery_security_logs WHERE (year = 2025 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute < 25))) AND name IN (SELECT name FROM people WHERE id in (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")))) AND name IN (SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1)));

# who did bruce call?
SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE caller IN (SELECT phone_number FROM people WHERE name = "Bruce") AND (year = 2025 AND month = 7 AND day = 28 AND duration < 60));

# destination city on the first flight out of Fiftyville
SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1);
#####


# crime scene notes
SELECT description FROM crime_scene_reports WHERE (year = 2025 AND month = 7 AND day = 28 AND street = "Humphrey Street" AND description LIKE "%duck%");
#Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.


# interviews
(year = 2025 AND month = 7 AND day = 28 
SELECT * FROM interviews WHERE (year = 2025 AND month = 7 AND day = 28 AND transcript LIKE "%thief%");

# 161|Ruth|2025|7|28|Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

SELECT license_plate FROM bakery_security_logs WHERE (year = 2025 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute < 25);


callers who also exited the bakery
SELECT * FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60 AND caller in (SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE (year = 2025 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute < 25))));

people who made those calls and exited th bakery
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60 AND caller in (SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE (year = 2025 AND month = 7 AND day = 28 AND activity = "exit" AND hour = 10 AND minute < 25)))));

# 162|Eugene|2025|7|28|I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

#transations at location
SELECT * FROM atm_transactions WHERE  (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street");

# accounts withdrawn from at atm
SELECT account_number FROM atm_transactions WHERE  (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street");

SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE  (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")));


# 163|Raymond|2025|7|28|As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60);

# people who made calls on the day of the theft for less than 60 seconds, where the caller was in the list of people who withdrew cash on legget street
SELECT * FROM people WHERE phone_number in (SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60 AND caller IN (SELECT phone_number FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE  (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street"))))));

SELECT id FROM people WHERE id in (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE (year = 2025 AND month = 7 AND day = 28 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")));


origin city id
 SELECT id FROM airports WHERE city = "Fiftyville";
8

flight id from earliest flight tomorrow
SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1;

passports on that flight
SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1);


people on that flight

SELECT * FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1));


calls made to the airport to people on that flight
SELECT * FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28) AND receiver in (SELECT phone_number FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1)));

SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28) AND receiver in (SELECT phone_number FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1))));

person who made a call on the 28th for less than a minute to someone on the passenger list for the 
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE (year = 2025 AND month = 7 AND day = 28 AND duration < 60) AND receiver in (SELECT phone_number FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE (year = 2025 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville")) ORDER BY hour ASC LIMIT 1))));
