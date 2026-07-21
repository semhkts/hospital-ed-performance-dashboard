-- ============================================================
-- Hospital Emergency Department Performance Dashboard
-- File: 02_create_tables.sql
-- Purpose: Create the project database tables
-- ============================================================

USE hospital_ed_dashboard;

CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(20),
    postcode_group VARCHAR(10)
);

CREATE TABLE triage_categories (
    triage_category_id INT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    target_wait_minutes INT NOT NULL,
    category_description VARCHAR(255)
);

CREATE TABLE arrival_methods (
    arrival_method_id INT PRIMARY KEY,
    method_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE diagnosis_groups (
    diagnosis_group_id INT PRIMARY KEY,
    diagnosis_group_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE staffing_levels (
    staffing_id INT AUTO_INCREMENT PRIMARY KEY,
    roster_date DATE NOT NULL,
    shift_name VARCHAR(20) NOT NULL,
    nurses_on_duty INT NOT NULL,
    doctors_on_duty INT NOT NULL,
    admin_staff_on_duty INT NOT NULL,

    UNIQUE (roster_date, shift_name)
);

CREATE TABLE ed_attendances (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,

    arrival_datetime DATETIME NOT NULL,
    first_seen_datetime DATETIME,
    departure_datetime DATETIME,

    triage_category_id INT NOT NULL,
    arrival_method_id INT NOT NULL,
    department_id INT,
    diagnosis_group_id INT,

    admitted BOOLEAN NOT NULL DEFAULT FALSE,
    left_without_being_seen BOOLEAN NOT NULL DEFAULT FALSE,
    discharge_destination VARCHAR(50),

    CONSTRAINT fk_attendance_patient
        FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    CONSTRAINT fk_attendance_triage
        FOREIGN KEY (triage_category_id)
        REFERENCES triage_categories(triage_category_id),

    CONSTRAINT fk_attendance_arrival_method
        FOREIGN KEY (arrival_method_id)
        REFERENCES arrival_methods(arrival_method_id),

    CONSTRAINT fk_attendance_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id),

    CONSTRAINT fk_attendance_diagnosis
        FOREIGN KEY (diagnosis_group_id)
        REFERENCES diagnosis_groups(diagnosis_group_id)
);
