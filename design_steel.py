from connect_to_sap import sap_model
import unit
import other_func, constants
from tkinter import messagebox

def run_analysis() -> bool:
    """Run the analysis."""
    is_success = not sap_model.Analyze.RunAnalysis()
    return is_success

def design_steel() -> bool:
    """Start the steel frame design."""
    is_success = not sap_model.DesignSteel.StartDesign()
    return is_success

def get_steel_code() -> str:
    """Return the steel design code"""
    current_code = sap_model.DesignSteel.GetCode()
    current_code = current_code[0]
    return current_code

def overwite_section(new_section_name: str) -> bool:
    """Overwite design section for all selected frame objects."""
    # ItemType: Object = 0; Group = 1; SelectedObjects = 2
    label = "N/A"
    item_type = 2 if label == "N/A" else 0
    
    if isinstance(new_section_name, str):
        is_success = not sap_model.DesignSteel.SetDesignSection(label, new_section_name, False, ItemType=item_type)
    else:
        raise TypeError(f"overwite_section() argument must be a str, not '{other_func.type_of_variable(new_section_name)}'")
    return is_success

def overwrite_steel_aisc(item: int, value: float | int = 0) -> bool:
    """Set the value of a steel design overwrite item.\n
    item argument in range(1, 43).\n
    Value >= 0; 0 means use program determined value."""
    """
    18 = Unbraced length ratio, Major
    19 = Unbraced length ratio, Minor
    20 = Unbraced length ratio, Lateral Torsional Buckling
    37 = Compressive capacity, Pnc
    38 = Tensile capacity, Pnt
    39 = Major bending capacity, Mn3
    40 = Minor bending capacity, Mn2
    41 = Major shear capacity, Vn2
    42 = Minor shear capacity, Vn3"""
    
    label = "N/A"
    item_type = 2 if label == "N/A" else 0
    current_unit = unit.get_current_unit()
    unit.set_unit(constants.UNIT["kN_m_C"])
    
    if isinstance(item, int) and item in range(1,44):
        if isinstance(value, (float, int)) and value >= 0:
            current_code = get_steel_code()
            # set overwrite item
            if current_code == "AISC 360-16":
                is_success = not sap_model.DesignSteel.AISC360_16.SetOverwrite(label, item, value, ItemType=item_type)
            elif current_code == "AISC 360-10":
                is_success = not sap_model.DesignSteel.AISC360_10.SetOverwrite(label, item, value, ItemType=item_type)
            elif current_code == "AISC360-05/IBC2006":
                is_success = not sap_model.DesignSteel.AISC360_05_IBC2006.SetOverwrite(label, item, value, ItemType=item_type)
            else:
                messagebox.showwarning(constants.TITLE, f"This version does not support {current_code}.")
        else:
            raise TypeError(f"overwrite_steel_aisc() argument 2 must be a positive real number, not '{other_func.type_of_variable(value)}'")
    else:
        raise TypeError(f"overwrite_steel_aisc() argument 1 must be an int, not '{other_func.type_of_variable(item)}'")
    unit.set_unit(current_unit)
    return is_success
