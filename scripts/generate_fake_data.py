"""
Hospital Emergency Department Performance Dashboard
File: generate_fake_data.py

Purpose:
Generate fictional patient, staffing and emergency department attendance
datasets for portfolio analysis.

All generated data is synthetic and does not represent real patients.
"""

from pathlib import Path

import numpy as np
import pandas as pd


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

RANDOM_SEED = 42
NUMBER_OF_PATIENTS = 8_000

START_DATE = "2025-01-01"
END_DATE = "2025-12-31"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_FOLDER = PROJECT_ROOT / "data" / "raw"

np.random.seed(RANDOM_SEED)


# ------------------------------------------------------------
# Create output directory
# ------------------------------------------------------------

RAW_DATA_FOLDER.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Generate fictional patients
# ------------------------------------------------------------

def generate_patients(number_of_patients: int) -> pd.DataFrame:
    """
    Generate a fictional patient dataset.

    Parameters
    ----------
    number_of_patients:
        Number of fictional patient records to create.

    Returns
    -------
    pandas.DataFrame
        Fictional patient data.
    """

    patient_ids = np.arange(1, number_of_patients + 1)

    start_date = pd.Timestamp("1925-01-01")
    end_date = pd.Timestamp(END_DATE)

    total_days = (end_date - start_date).days

    random_days = np.random.randint(
        low=0,
        high=total_days + 1,
        size=number_of_patients,
    )

    dates_of_birth = start_date + pd.to_timedelta(
        random_days,
        unit="D",
    )

    genders = np.random.choice(
        ["Female", "Male", "Other", "Not stated"],
        size=number_of_patients,
        p=[0.495, 0.495, 0.005, 0.005],
    )

    postcode_groups = np.random.choice(
        [
            "Sydney CBD",
            "Inner West",
            "Eastern Suburbs",
            "Northern Suburbs",
            "Southern Suburbs",
            "Western Sydney",
            "South Western Sydney",
            "Outside Sydney",
        ],
        size=number_of_patients,
        p=[
            0.08,
            0.17,
            0.13,
            0.12,
            0.12,
            0.18,
            0.14,
            0.06,
        ],
    )

    patients = pd.DataFrame(
        {
            "patient_id": patient_ids,
            "date_of_birth": dates_of_birth,
            "gender": genders,
            "postcode_group": postcode_groups,
        }
    )

    patients["date_of_birth"] = (
        patients["date_of_birth"].dt.strftime("%Y-%m-%d")
    )

    return patients


# ------------------------------------------------------------
# Generate fictional staffing levels
# ------------------------------------------------------------

def generate_staffing_levels(
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """
    Generate fictional ED staffing levels for three daily shifts.

    Parameters
    ----------
    start_date:
        First roster date in YYYY-MM-DD format.

    end_date:
        Last roster date in YYYY-MM-DD format.

    Returns
    -------
    pandas.DataFrame
        Fictional staffing data with one row per date and shift.
    """

    roster_dates = pd.date_range(
        start=start_date,
        end=end_date,
        freq="D",
    )

    shifts = ["Morning", "Evening", "Night"]
    staffing_records = []

    staffing_id = 1

    for roster_date in roster_dates:
        weekday = roster_date.day_name()

        for shift_name in shifts:
            if shift_name == "Morning":
                nurses = np.random.randint(15, 20)
                doctors = np.random.randint(6, 9)
                admin_staff = np.random.randint(3, 6)

            elif shift_name == "Evening":
                nurses = np.random.randint(17, 23)
                doctors = np.random.randint(7, 11)
                admin_staff = np.random.randint(3, 6)

            else:
                nurses = np.random.randint(11, 16)
                doctors = np.random.randint(4, 7)
                admin_staff = np.random.randint(2, 4)

            # Slightly increase staffing during busy weekend evenings
            if (
                weekday in ["Friday", "Saturday"]
                and shift_name == "Evening"
            ):
                nurses += 2
                doctors += 1

            staffing_records.append(
                {
                    "staffing_id": staffing_id,
                    "roster_date": roster_date.strftime("%Y-%m-%d"),
                    "shift_name": shift_name,
                    "nurses_on_duty": nurses,
                    "doctors_on_duty": doctors,
                    "admin_staff_on_duty": admin_staff,
                }
            )

            staffing_id += 1

    return pd.DataFrame(staffing_records)


# ------------------------------------------------------------
# Save datasets
# ------------------------------------------------------------

def main() -> None:
    """Generate and save all fictional datasets."""

    patients = generate_patients(NUMBER_OF_PATIENTS)

    staffing_levels = generate_staffing_levels(
        START_DATE,
        END_DATE,
    )

    patients_output_path = RAW_DATA_FOLDER / "patients.csv"
    staffing_output_path = RAW_DATA_FOLDER / "staffing_levels.csv"

    patients.to_csv(
        patients_output_path,
        index=False,
    )

    staffing_levels.to_csv(
        staffing_output_path,
        index=False,
    )

    print(f"Created {len(patients):,} fictional patients.")
    print(f"Saved file to: {patients_output_path}")

    print(
        f"Created {len(staffing_levels):,} fictional staffing records."
    )
    print(f"Saved file to: {staffing_output_path}")


if __name__ == "__main__":
    main()
