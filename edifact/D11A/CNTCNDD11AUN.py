#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD11AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 99},
    {ID: 'ALI', MIN: 0, MAX: 99},
    {ID: 'AGR', MIN: 0, MAX: 99},
    {ID: 'MOA', MIN: 0, MAX: 99},
    {ID: 'GEI', MIN: 0, MAX: 99},
    {ID: 'PAI', MIN: 0, MAX: 99},
    {ID: 'TOD', MIN: 0, MAX: 99},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
    ]},
    {ID: 'PRI', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'RNG', MIN: 0, MAX: 99},
    ]},
    {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
    ]},
    {ID: 'CUX', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
    ]},
    {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'MOA', MIN: 0, MAX: 99},
    ]},
    {ID: 'PYT', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'PCD', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 99},
    ]},
    {ID: 'SEQ', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'NAD', MIN: 1, MAX: 1},
        {ID: 'GEI', MIN: 0, MAX: 99},
        {ID: 'FII', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'CTA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 99},
        ]},
        {ID: 'REL', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'NAD', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
        ]},
    ]},
    {ID: 'ALC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'ALI', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 99},
        ]},
        {ID: 'PCD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 99},
        ]},
        {ID: 'RTE', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 99},
        ]},
        {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RNG', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 99},
        ]},
    ]},
    {ID: 'FOR', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'GEI', MIN: 0, MAX: 99},
        {ID: 'ALI', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'FSQ', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RTE', MIN: 0, MAX: 99},
            {ID: 'PCD', MIN: 0, MAX: 99},
            {ID: 'MEA', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'IND', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'ALI', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'QTY', MIN: 0, MAX: 99},
            ]},
        ]},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'PIA', MIN: 0, MAX: 99},
        {ID: 'IMD', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 99},
        ]},
        {ID: 'GEI', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'RTE', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 99},
            {ID: 'TAX', MIN: 0, MAX: 99},
            {ID: 'PCD', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'FOR', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ALI', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'GEI', MIN: 0, MAX: 99},
            {ID: 'FSQ', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RTE', MIN: 0, MAX: 99},
                {ID: 'PCD', MIN: 0, MAX: 99},
                {ID: 'MEA', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 99},
                {ID: 'RFF', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'GEI', MIN: 0, MAX: 99},
                {ID: 'QTY', MIN: 0, MAX: 99},
            ]},
        ]},
        {ID: 'ALC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'ALI', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99},
            ]},
            {ID: 'QTY', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 99},
            ]},
            {ID: 'PCD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 99},
            ]},
            {ID: 'RTE', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 99},
            ]},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RNG', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 99},
            ]},
            {ID: 'TAX', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 99},
            ]},
        ]},
        {ID: 'PRI', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'APR', MIN: 0, MAX: 99},
            {ID: 'RNG', MIN: 0, MAX: 99},
            {ID: 'CUX', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
        ]},
        {ID: 'TOD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 99},
        ]},
        {ID: 'PAC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 99},
            {ID: 'PCI', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'RFF', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'GIN', MIN: 0, MAX: 99},
            ]},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'GEI', MIN: 0, MAX: 99},
            {ID: 'FII', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 99},
            {ID: 'TAX', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
