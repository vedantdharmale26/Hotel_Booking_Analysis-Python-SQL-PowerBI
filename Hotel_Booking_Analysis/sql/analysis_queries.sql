-- ===============================
-- HOTEL BOOKING ANALYSIS PROJECT
-- STEP 6: SQL ANALYSIS QUERIES
-- ===============================

USE hotel_db;

-- 1. Total number of bookings
SELECT COUNT(*) AS total_bookings
FROM hotel_bookings;

-- 2. Total canceled bookings
SELECT 
    SUM(is_canceled) AS canceled_bookings,
    COUNT(*) AS total_bookings
FROM hotel_bookings;

-- 3. Cancellation rate (%)
SELECT 
    ROUND(SUM(is_canceled) / COUNT(*) * 100, 2) AS cancellation_rate
FROM hotel_bookings;

-- 4. Cancellation rate by hotel type
SELECT 
    hotel,
    ROUND(AVG(is_canceled) * 100, 2) AS cancellation_rate
FROM hotel_bookings
GROUP BY hotel;

-- 5. Bookings by hotel type
SELECT 
    hotel,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY hotel;

-- 6. Monthly booking trend
SELECT 
    arrival_date_month,
    COUNT(*) AS bookings
FROM hotel_bookings
GROUP BY arrival_date_month
ORDER BY bookings DESC;

-- 7. Revenue by market segment
SELECT 
    market_segment,
    ROUND(SUM(adr), 2) AS total_revenue
FROM hotel_bookings
WHERE is_canceled = 0
GROUP BY market_segment
ORDER BY total_revenue DESC;
