-- ============================================================
-- Hospital Emergency Department Performance Dashboard
-- File: 03_insert_lookup_data.sql
-- Purpose: Populate lookup tables
-- ============================================================

USE hospital_ed_dashboard;

-------------------------------------------------------------
-- TRIAGE CATEGORIES
-------------------------------------------------------------

INSERT INTO triage_categories (
    triage_category_id,
    category_name,
    target_wait_minutes,
    category_description
)
VALUES
(1, 'Category 1', 0, 'Immediate life-threatening condition'),
(2, 'Category 2', 10, 'Imminently life-threatening'),
(3, 'Category 3', 30, 'Potentially life-threatening'),
(4, 'Category 4', 60, 'Potentially serious'),
(5, 'Category 5', 120, 'Less urgent');

-------------------------------------------------------------
-- ARRIVAL METHODS
-------------------------------------------------------------

INSERT INTO arrival_methods (
    arrival_method_id,
    method_name
)
VALUES
(1, 'Ambulance'),
(2, 'Walk-in'),
(3, 'GP Referral'),
(4, 'Police'),
(5, 'Transfer'),
(6, 'Helicopter');

-------------------------------------------------------------
-- DEPARTMENTS
-------------------------------------------------------------

INSERT INTO departments (
    department_id,
    department_name
)
VALUES
(1, 'Resuscitation'),
(2, 'Acute Care'),
(3, 'Fast Track'),
(4, 'Mental Health'),
(5, 'Paediatrics'),
(6, 'Short Stay');
