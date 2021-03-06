#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD06BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'MSG', MIN: 1, MAX: 1},
    {ID: 'RCS', MIN: 0, MAX: 1},
    {ID: 'DII', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 99},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 999},
    {ID: 'PNA', MIN: 0, MAX: 5, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 5},
        ]},
    ]},
    {ID: 'DFN', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'GRU', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'SGU', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'FNT', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'REL', MIN: 0, MAX: 1},
            {ID: 'GIR', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'ELU', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ELM', MIN: 0, MAX: 1},
            {ID: 'EDT', MIN: 0, MAX: 1},
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'GEI', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'MEA', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'ELV', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'CDV', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
        {ID: 'DRD', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
        ]},
    ]},
    {ID: 'AUT', MIN: 0, MAX: 1, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
