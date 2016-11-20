#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD01AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 1},
    {ID: 'PNA', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'COM', MIN: 0, MAX: 9},
    ]},
    {ID: 'HYN', MIN: 1, MAX: 999999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 5},
        {ID: 'STS', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'PNA', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 1},
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'FTX', MIN: 0, MAX: 999},
        ]},
        {ID: 'IRQ', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 1},
            {ID: 'PNA', MIN: 0, MAX: 2},
            {ID: 'DTM', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]