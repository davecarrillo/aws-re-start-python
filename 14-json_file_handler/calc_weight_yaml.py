import yaml_file_handler

data = yaml_file_handler.read_yaml_file('aws-re-start-python/14-json_file_handler/files/insulin.yaml')

if data != "" :
    b_insulin = data['molecules']['bInsulin']
    a_insulin = data['molecules']['aInsulin']
    insulin = b_insulin + a_insulin
    molecular_weight_insulin_actual = data['molecularWeightInsulinActual']
    print('b_insulin: ' + b_insulin)
    print('a_insulin: ' + a_insulin)
    print('molecular_weight_insulin_actual: ' + str(molecular_weight_insulin_actual))
    
    # Calculating the molecular weight of insulin  
    # Getting a list of the amino acid (AA) weights  
    aa_weights = data['weights']
    
    # Count the number of each amino acids  
    aa_count_insulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    
    # Multiply the count by the weights  
    molecular_weight_insulin = sum({x: (aa_count_insulin[x]*aa_weights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    
    print("The rough molecular weight of insulin: " +
    str(molecular_weight_insulin))
    print("Percent error: " + str(((molecular_weight_insulin - molecular_weight_insulin_actual)/molecular_weight_insulin_actual)*100))
else:
    print("Error. Exiting program")
