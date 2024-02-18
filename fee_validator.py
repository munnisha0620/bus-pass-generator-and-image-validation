# fee_validator.py
import pandas as pd

fee_structure_df = pd.read_excel("fee_structure.xlsx")

def validate_fee_structure(reg_number, destination_fee):
    row = fee_structure_df[(fee_structure_df["Reg.Number"] == reg_number) & (fee_structure_df["Boarding Point Fee"] == destination_fee)]
    if not row.empty:
        print("Fee structure is valid.")
        return True
    else:
        print("Invalid fee structure.")
        return False

# Example usage
validate_fee_structure("123ABC12345", 16422)
