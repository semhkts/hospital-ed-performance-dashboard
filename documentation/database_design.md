# Database Design

This project uses a relational database to model emergency department operations.

## Tables

### 1. ed_attendances

Stores one record for each patient attendance in the emergency department.

Primary Key:

* attendance_id

### 2. triage_categories

Stores information about emergency triage categories and their recommended maximum waiting times.

Primary Key:

* triage_category_id

### 3. arrival_methods

Stores how patients arrived at the emergency department.

Examples:

* Ambulance
* Walk-in
* GP Referral
* Police
* Helicopter

Primary Key:

* arrival_method_id

### 4. departments

Stores the treatment areas within the emergency department.

Examples:

* Acute
* Fast Track
* Resuscitation
* Mental Health
* Paediatrics
* Short Stay

Primary Key:

* department_id

### 5. staffing_levels

Stores staffing information for each shift.

Primary Key:

* staffing_id

