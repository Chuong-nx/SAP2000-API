"""Material."""

from connect_to_sap import sap_model
import other_func

def get_material_name_list(material_type: int = 0) -> tuple:
    """Return the name of all material property.\n
    Optional material_type is one of the following items:
    ALL = 0; STEEL = 1; CONCRETE = 2; NODESIGN = 3; ALUMINUM = 4; COLDFORMED = 5; REBAR = 6; TENDON = 7.
    """
    if isinstance(material_type, int):
        material_name_list = sap_model.PropMaterial.GetNameList(MatType=material_type)
        material_name_list = material_name_list[1]
        return material_name_list
    else:
        raise TypeError(f"get_material_name_list() argument must be an int, not '{other_func.type_of_variable(material_type)}'")
