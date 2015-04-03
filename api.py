from flask import jsonify
import json
import os


def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


def search_people(path, name):
    jsons = [os.path.join(path, file_name) for file_name in os.listdir(path)
             if file_name.endswith('.json')]

    results = set()

    first = True
    name_found = False
    user_name = ''

    for file_name in jsons:
        if (first):
            first_file_name = file_name[len(path):-10]  # Tfidf.json
            first = False
        else:
            current_file_name = file_name[len(path):-10]
            user_name = longest_common_substring(first_file_name,
                                                 current_file_name)

        if name.lower() in file_name.lower():
            results.add(file_name)

    other_people = []

    for file_path in list(results):
        name = file_path[len(path):-10]

        if (name.find(user_name) == 0):
            second_name = name[len(user_name):]
            other_people.append(second_name)
        else:
            second_name = name[:-len(user_name)]
            other_people.append(second_name)

    return jsonify(paths=list(results), user_name=user_name,
                   other_people=other_people)


def search_tags(path, tag):
    jsons = [os.path.join(path, file_name) for file_name in os.listdir(path)
             if file_name.endswith('.json')]

    results = []
    frequencies = []
    first = True
    name_found = False
    user_name = ''

    for file_name in jsons:
        if (first):
            first_file_name = file_name[len(path):-10]  # Tfidf.json
            first = False
        else:
            current_file_name = file_name[len(path):-10]
            user_name = longest_common_substring(first_file_name,
                                                 current_file_name)

        json_data = open(file_name).read()

        data = json.loads(json_data)

        for entry in data['words']:
            if tag.lower() == entry['word'].lower():
                results.append(file_name)
                frequencies.append(entry['ratio'])

    other_people = []

    for file_path in list(results):
        name = file_path[len(path):-10]

        if (name.find(user_name) == 0):
            second_name = name[len(user_name):]
            other_people.append(second_name)
        else:
            second_name = name[:-len(user_name)]
            other_people.append(second_name)

    user_freq = [(other_people[i], frequencies[i])
                 for i in xrange(len(other_people))]

    sorted_by_freq = sorted(user_freq, key=lambda tup: tup[1])

    other_people = []
    frequencies = []

    for s in sorted_by_freq:
        other_people.append(s[0])
        frequencies.append(s[1])

    return jsonify(paths=results,
                   user_name=user_name,
                   frequencies=frequencies,
                   other_people=other_people)
