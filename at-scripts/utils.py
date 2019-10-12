import os
import fnmatch
import string
import json

def getFileNames():
    '''gets all file patsh starting from the specified root dir'''
    names = []
    for root, dirnames, filenames in os.walk('./'):
        [names.append(os.path.join(root, name)) for name in filenames]
    return names

def getAllPathsWithExtension(extension, filePaths):
    '''from filePaths gets all files with the specified extension'''
    matches = []
    for filePath in fnmatch.filter(filePaths, '*.{}'.format(extension.lower())):
        if '/.' not in filePath:
            matches.append(filePath)
    for filePath in fnmatch.filter(filePaths, '*.{}'.format(extension.upper())):
        if '/.' not in filePath:
            matches.append(filePath)
    return matches

def getAlphabeticalColumnNames(idx):
    '''creates an alphabetical index from an integer index
    e.g. 
        1 => 'A'
        30 => 'AD'
    '''
    q, r = divmod(idx, 26)
    col = []
    if r:
        col = [r]
    while q > 0:
        q, r = divmod(q, 26)
        col = [r] + col
    aplha = ''.join([string.ascii_uppercase[i-1] for i in col])
    return aplha

def isFiltered(path, filters):
    '''Checks if the path should be filtered'''
    filtered = False
    for f in filters:
        if f in path:
            filtered = True
            break
    return filtered

def filterPaths(filePathsUnfiltered, filters):
    '''Removes from the filePathsUnfiltered terms
    that should be filtered.
    '''
    filteredPaths = []
    for path in filePathsUnfiltered:
        filtered = False
        for f in filters:
            if f in path:
                filtered = True
                break
        if not filtered:
            filteredPaths.append(path)
    return filteredPaths

def getPathMapping(path):
    '''Based on a directory_map.json file, converts a 
    directory path to a shortened version.
    e.g.:
        input: 
            ./repo/BASE TABASCO/BD/TABASCO 2017/Modificada/tabasco.csv
        output:
            .A.C.B.A.A.A
    '''
    with open('directory_map.json') as f:
        dirmap = json.load(f)
        structure = path.split('/')[1:]
        dmap = dirmap
        index = ''
        for i, d in enumerate(structure):
            for name in dmap['names']:
                if dmap['names'][name] == d:
                    index = '{}.{}'.format(index, name)
                    if i < len(structure) - 1:
                        dmap = dmap['dir'][name]
                        break
                    else:
                        break
                        
    return index

def getPathFromMapping(mapping):
    '''Based on a directory_map.json file, converts a 
    mapped path to a full directory path.
    e.g.:
        input:
            .A.C.B.A.A.A
        output:
            ./repo/BASE TABASCO/BD/TABASCO 2017/Modificada/tabasco.csv
    '''
    with open('directory_map.json') as f:
        dirmap = json.load(f)
        structure = mapping.split('.')[1:]
        dmap = dirmap
        path = '.'
        for i,d in enumerate(structure):
            for name in dmap['names']:
                if name == d:
                    path = '{}/{}'.format(path, dmap['names'][name])
                    if i < len(structure) - 1:
                        dmap = dmap['dir'][name]
                        break
                    else:
                        break
    return path