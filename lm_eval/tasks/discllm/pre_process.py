def doc_to_text(doc) -> str:
    return_data='Default return'
    if 'relation' not in doc['instruction_type']:
        if doc['instruction_type'] not in ['CDISCK_KG_DESC']:
            return_data=f"You are a Clinician with Clinical Study protocol expertise, below is an INSTRUCTION that describes a task, paired with the INPUT that contains the description of the Study protocol. Write a response that appropriately completes the request. \n {doc['input']}\nQuestion: {doc['instruction']}\nAnswer:"
        else:
            return_data=f"You are a Clinician with Clinical Trial Data Expertise, below is an INSTRUCTION that describes a task. Write a response that appropriately completes the request. \n {doc['input']}\nQuestion: {doc['instruction']} \nAnswer:"
    else:
        return_data=f"{doc['instruction']}\nQuestion: {doc['input']} \nAnswer:"
    
    return return_data
