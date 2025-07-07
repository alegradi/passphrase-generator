#!/usr/bin/env python3
import random

generated_components = {}
special_characters = ["<", ">", "[", "]", "{", "}", "#", "£", "€", "%", "^", "?", "!", "+", "-", "/", "_", "*", "@"]


# Create lists from files to use as the basis of passphrase generation
with open("data/adverbs.txt", "r") as file:
    adverbs_list = file.read().splitlines()

with open("data/adjectives.txt", "r") as file:
    adjectives_list = file.read().splitlines()

with open("data/nouns.txt", "r") as file:
    nouns_list = file.read().splitlines()

with open("data/verbs.txt", "r") as file:
    verb_list = file.read().splitlines()


# Function definitions
def generate_random_components():

    # Read the word lists and choose random
    generated_components["adverb"] = random.choice(adverbs_list)
    generated_components["adjective"] = random.choice(adjectives_list)
    generated_components["noun"] = random.choice(nouns_list)
    generated_components["verb"] = random.choice(verb_list)

    return generated_components

# DEBUG PRINT
# print(generate_random_components())


def add_special_character(selected_words):

    modifiable_options = list(selected_words.keys())
    what_to_modify = random.choice(modifiable_options)
    selected_words[what_to_modify] += random.choice(special_characters)
    return selected_words


def capitalize_word(selected_words):

    modifiable_options = list(selected_words.keys())
    what_to_modify = random.choice(modifiable_options)
    word_to_capitalize = selected_words[what_to_modify]
    selected_words[what_to_modify] = word_to_capitalize.title()
    return selected_words


def add_random_number(selected_words):

    modifiable_options = list(selected_words.keys())
    what_to_modify = random.choice(modifiable_options)
    word_to_modify = selected_words[what_to_modify]
    selected_words[what_to_modify] = word_to_modify + str(random.randint(0, 9))
    return selected_words


def generate_passphrase():

    generate_random_components()

    generated_passphrase = ""

    # Select random method to generate
    generation_method = random.randint(1, 3)

    # 
    if generation_method == 1:
        del generated_components["adverb"]

        processed_generated_components = add_special_character(generated_components)
        processed_generated_components = capitalize_word(processed_generated_components)
        processed_generated_components = add_random_number(processed_generated_components)

        generated_passphrase += processed_generated_components['adjective'] + "-"
        generated_passphrase += processed_generated_components['noun'] + "-"
        generated_passphrase += processed_generated_components['verb']

    if generation_method == 2:
        del generated_components["adjective"]

        processed_generated_components = add_special_character(generated_components)
        processed_generated_components = capitalize_word(processed_generated_components)
        processed_generated_components = add_random_number(processed_generated_components)

        generated_passphrase += processed_generated_components['adverb'] + "-"
        generated_passphrase += processed_generated_components['noun'] + "-"
        generated_passphrase += processed_generated_components['verb']

    if generation_method == 3:
        del generated_components["verb"]

        processed_generated_components = add_special_character(generated_components)
        processed_generated_components = capitalize_word(processed_generated_components)
        processed_generated_components = add_random_number(processed_generated_components)

        generated_passphrase += processed_generated_components['adverb'] + "-"
        generated_passphrase += processed_generated_components['adjective'] + "-"
        generated_passphrase += processed_generated_components['noun']

    return generated_passphrase


print(generate_passphrase())
