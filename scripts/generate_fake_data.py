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
    end_date = pd.Timestamp("2025-12-31")

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

    patients["date_of_birth"] = patients[
        "date_of_birth"
    ].dt.strftime("%Y-%m-%d")

    return patients


# ------------------------------------------------------------
# Save datasets
# ------------------------------------------------------------

def main() -> None:
    """Generate and save all fictional datasets."""

    patients = generate_patients(NUMBER_OF_PATIENTS)

    patients_output_path = RAW_DATA_FOLDER / "patients.csv"

    patients.to_csv(
        patients_output_path,
        index=False,
    )

    print(f"Created {len(patients):,} fictional patients.")
    print(f"Saved file to: {patients_output_path}")


if __name__ == "__main__":
    main()
