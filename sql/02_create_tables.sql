-- ============================================================
-- Hospital Emergency Department Performance Dashboard
-- File: 02_create_tables.sql
-- Purpose: Create the project database tables
-- ============================================================

USE hospital_ed_dashboard;

-- Stores the five Australasian Triage Scale categories
CREATE TABLE triage_categories (
    triage_category_id INT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    target_wait_minutes INT NOT NULL,
    category_description VARCHAR(255)
);

-- Stores the methods patients use to arrive at the ED
CREATE TABLE arrival_methods (
    arrival_method_id INT PRIMARY KEY,
    method_name VARCHAR(50) NOT NULL UNIQUE
);

-- Stores treatment areas within the ED
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL UNIQUE
);

-- Stores staffing numbers for each date and shift
CREATE TABLE staffing_levels (
    staffing_id INT AUTO_INCREMENT PRIMARY KEY,
    roster_date DATE NOT NULL,
    shift_name VARCHAR(20) NOT NULL,
    nurses_on_duty INT NOT NULL,
    doctors_on_duty INT NOT NULL,
    admin_staff_on_duty INT NOT NULL,
    total_staff_on_duty INT NOT NULL,
    
    UNIQUE (roster_date, shift_name)
);

-- Stores one record for each ED attendance
CREATE TABLE ed_attendances (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    arrival_datetime DATETIME NOT NULL,
    first_seen_datetime DATETIME,
    departure_datetime DATETIME,
    
    triage_category_id INT NOT NULL,
    arrival_method_id INT NOT NULL,
    department_id INT,
    
    patient_age INT,
    gender VARCHAR(20),
    diagnosis_group VARCHAR(100),
    discharge_destination VARCHAR(50),
    
    admitted BOOLEAN NOT NULL DEFAULT FALSE,
    left_without_being_seen BOOLEAN NOT NULL DEFAULT FALSE,
    
    waiting_minutes INT,
    length_of_stay_minutes INT,
    seen_within_target BOOLEAN,
    
    shift_name VARCHAR(20),
    arrival_day VARCHAR(10),
    
    CONSTRAINT fk_attendance_triage
        FOREIGN KEY (triage_category_id)
        REFERENCES triage_categories(triage_category_id),
        
    CONSTRAINT fk_attendance_arrival_method
        FOREIGN KEY (arrival_method_id)
        REFERENCES arrival_methods(arrival_method_id),
        
    CONSTRAINT fk_attendance_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
