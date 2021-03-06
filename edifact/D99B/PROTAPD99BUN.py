#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD99BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'GIS', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 99},
    {ID: 'RFF', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'BII', MIN: 0, MAX: 99},
        {ID: 'GIR', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'REL', MIN: 0, MAX: 1},
        ]},
    ]},
    {ID: 'PNA', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'ADR', MIN: 0, MAX: 1},
        {ID: 'BII', MIN: 0, MAX: 1},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'CED', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'EFI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'CED', MIN: 0, MAX: 1},
        {ID: 'DTM', MIN: 0, MAX: 1},
    ]},
    {ID: 'IND', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'BII', MIN: 0, MAX: 1},
        {ID: 'IMD', MIN: 0, MAX: 1},
        {ID: 'RCS', MIN: 0, MAX: 1},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'BII', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'PRI', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'PCD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'RTE', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
    ]},
    {ID: 'UNS', MIN: 1, MAX: 1},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'SCC', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'QTY', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 999},
        ]},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 9999, LEVEL: [
        {ID: 'STS', MIN: 0, MAX: 1},
        {ID: 'BII', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'IMD', MIN: 0, MAX: 9},
        {ID: 'PNA', MIN: 0, MAX: 9},
        {ID: 'CCI', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'PCD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'GIR', MIN: 0, MAX: 9999, LEVEL: [
            {ID: 'REL', MIN: 0, MAX: 1},
            {ID: 'RCS', MIN: 0, MAX: 1},
            {ID: 'BII', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'IMD', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99},
            ]},
            {ID: 'PCD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99},
            ]},
            {ID: 'RTE', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99},
            ]},
        ]},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 99},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
