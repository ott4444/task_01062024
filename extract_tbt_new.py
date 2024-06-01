import os
import json
import re


def extract_tbt_values_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    tbt_values = {}
    tbt_pattern = re.compile(r'TBT:\s*(.+)')

    def extract_from_dict(d, parent_key=''):
        for key, value in d.items():
            if isinstance(value, str):
                match = tbt_pattern.search(value)
                if match:
                    tbt_values.setdefault(file_path, {}).setdefault(parent_key, {})[key] = match.group(1).strip()
            elif isinstance(value, dict):
                extract_from_dict(value, key)
            elif isinstance(value, list):
                extract_from_list(value, key)

    def extract_from_list(lst, parent_key=''):
        for index, item in enumerate(lst):
            if isinstance(item, str):
                match = tbt_pattern.search(item)
                if match:
                    tbt_values.setdefault(file_path, {}).setdefault(parent_key, {})[str(index)] = match.group(1).strip()
            elif isinstance(item, dict):
                extract_from_dict(item, str(index))
            elif isinstance(item, list):
                extract_from_list(item, str(index))

    if isinstance(data, dict):
        extract_from_dict(data)
    elif isinstance(data, list):
        extract_from_list(data)

    return tbt_values


def process_json_folder(folder_path):
    all_tbt_values = {}
    json_files = os.listdir(folder_path)
    for file_name in json_files:
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            tbt_values = extract_tbt_values_from_json(file_path)
            all_tbt_values.update(tbt_values)
    return all_tbt_values


def write_result_file(output_path, tbt_values):
    """Write the TBT values to an output file."""
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(tbt_values, output_file, indent=4)


folder_path = os.path.dirname(os.path.abspath(__file__))
output_path = 'tbt_output.json'

tbt_values = process_json_folder(folder_path)

write_result_file(output_path, tbt_values)

print(f'Collected TBT values and wrote them to {output_path}')
