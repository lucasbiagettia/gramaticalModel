import yaml
import os

PROMPTS_FILE_PATH = '/home/lbiagetti/Documentos/gitPr/gramaticalModel/src/prompt/prompt.yml'
GRAMATICAL_ERROR_TYPE_FILE_PATH = '/home/lbiagetti/Documentos/gitPr/gramaticalModel/src/prompt/gramatical_errors_type.yml'

def load_prompts():
    """Carga todos los prompts desde el archivo YAML."""
    with open(PROMPTS_FILE_PATH, 'r', encoding='utf-8') as file:
        prompts = yaml.safe_load(file)
    with open(GRAMATICAL_ERROR_TYPE_FILE_PATH, 'r', encoding='utf-8') as file:
        gramatical_errors = yaml.safe_load(file)
    return prompts, gramatical_errors

prompts_data, gramatical_errors_data = load_prompts()

def get_errors_generator_prompt(correct_text):
    base_prompt = prompts_data['general_prompt']
    prompt = base_prompt.format(correct_text=correct_text)
    return prompt


def get_errors_generator_prompt_with_error_type(correct_text):
    base_prompt = prompts_data['general_prompt_with_error_type']
    error_types = get_error_types()
    formated_error_texts = []
    for et in error_types:
        formated_error_text = get_formated_error_text(et)
        formated_error_texts.append(formated_error_text)
    prompt = base_prompt.format(correct_text=correct_text, formated_error_texts=formated_error_texts)
    return prompt


def get_error_types():
    return [gramatical_errors_data['error_types']['Errores de concordancia'],
            gramatical_errors_data['error_types']['Pleonasmos innecesarios']]

def get_formated_error_text(error_type):
    error_name = error_type['Name']
    error_definition = error_type['Definition']
    samples = error_type['Samples']
    error_format_samples = []
    for es in samples:
        error_format_sample = get_error_format_sample(es)
        error_format_samples.append(error_format_sample)
    error_format = prompts_data['error_type_format']
    formated_error_text = error_format.format(error_name=error_name, error_definition=error_definition, error_format_samples=error_format_samples)
    return formated_error_text

def get_error_format_sample(error_sample):
    incorrect = error_sample['incorrect']
    correct = error_sample['correct']
    explanation = error_sample['explanation']
    sample_format = prompts_data['sample_format']
    error_format_sample = sample_format.format(incorrect=incorrect, correct=correct, explanation=explanation)
    return error_format_sample