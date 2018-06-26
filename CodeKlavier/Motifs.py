"""Motifs in Dictionaries.

Here you can define the name of the motif and the series of midi-notes that
make up that motif.
Way more efficient than an unjustified class.

TODO: re-order to have a config loader before execution of prototypes, etc...
"""

import configparser
import os

currentpath = os.path.dirname(os.path.abspath(__file__))
projectdir = os.path.abspath(os.path.join(currentpath, os.pardir))

config = configparser.ConfigParser()
config.read(projectdir + '/default_setup.ini')

try:
    motif_1 = config['snippets midi mapping'].get('motif_1').split(',')
    motif_2 = config['snippets midi mapping'].get('motif_2').split(',')
    
    #all are lists
    identity_midi = config['lambda'].get('identity_midi').split(',')
    evaluate_function = config['lambda'].get('evaluate_function').split(',')    
    select_first = config['lambda'].get('select_first_midi').split(',')
    select_second = config['lambda'].get('select_second_midi').split(',')    
    successor = config['lambda'].get('successor_midi').split(',')
    predecessor = config['lambda'].get('predecessor_midi').split(',')  
    add_midi = config['lambda'].get('add_midi').split(',')  
    substract_midi = config['lambda'].get('substract_midi').split(',')
    mult_midi = config['lambda'].get('mult_midi').split(',')    
    division_midi = config['lambda'].get('division_midi').split(',')
    equal_than_midi = config['lambda'].get('equality_midi').split(',')
    greater_than_midi = config['lambda'].get('greater_than_midi').split(',')
    less_than_midi = config['lambda'].get('less_than_midi').split(',')
    
except KeyError:
    raise LookupError('Missing key information in the config file.')

motifs = {}

# motippets
motifs['motif_1'] = list(map(int, motif_1))
motifs['motif_2'] = list(map(int, motif_2))
motifs['mini_motif_1_low'] = [35, 38, 42]
motifs['mini_motif_2_low'] = [26, 32, 35, 38]
motifs['mini_motif_3_low'] = [39, 43, 46]
motifs['mini_motif_1_mid'] = [60, 64, 67]
motifs['mini_motif_2_mid'] = [50, 56, 59, 62]
motifs['mini_motif_1_hi'] = [86, 90, 93]
motifs['mini_motif_2_hi'] = [86, 92, 95, 98]
motifs['conditional_1'] = [36, 31, 29, 26, 28, 35, 38, 33, 24, 26, 31, 28, 33, 21, 23, 29]
motifs['conditional_2'] = [45, 43, 46, 45, 43, 41, 43, 45]
motifs['conditional_3'] = [93, 91, 89, 91, 93, 91, 94, 93]
motifs['conditional_result_1'] = [55, 58, 76, 63, 67]
motifs['conditional_result_2'] = [99, 92, 90, 89, 92, 94]
motifs['conditional_result_3'] = [21,22,23]
motifs['conditional_result_4'] = [23,24,25]
motifs['conditional_result_5'] = [26,23,23]

# lambda calculus
motifs['eval'] = list(map(int, evaluate_function))
motifs['zero'] = list(map(int, identity_midi))
motifs['true'] = list(map(int, select_first))
motifs['false'] = list(map(int, select_second))
motifs['successor'] = list(map(int, successor))
motifs['predecessor'] = list(map(int, predecessor))
motifs['addition'] = list(map(int, add_midi))
motifs['substraction'] = list(map(int, substract_midi))
motifs['multiplication'] = list(map(int, mult_midi))
motifs['division'] = list(map(int, division_midi))
motifs['equal'] = list(map(int, equal_than_midi))
motifs['greater'] = list(map(int, greater_than_midi))
motifs['less'] = list(map(int, less_than_midi))


