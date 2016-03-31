import os
import requests
import sys
import urllib


def analyze(directory, username, password):
    anger = list()
    fear = list()
    disgust = list()
    joy = list()
    sadness = list()

    print("Analyzing all files in " + directory)
    for fn in os.listdir(directory):
        print("Working on file: " + os.path.join(directory, fn))
        with open(os.path.join(directory, fn), 'r') as myfile:
            text = myfile.read().replace('\n', '')
            json_output = analyze_single(text, username, password)

            anger.append(json_output['document_tone']['tone_categories'][0]['tones'][0]['score'])
            fear.append(json_output['document_tone']['tone_categories'][0]['tones'][1]['score'])
            disgust.append(json_output['document_tone']['tone_categories'][0]['tones'][2]['score'])
            joy.append(json_output['document_tone']['tone_categories'][0]['tones'][3]['score'])
            sadness.append(json_output['document_tone']['tone_categories'][0]['tones'][4]['score'])

    print("Overview of average emotional levels (0 <= n <= 1)")

    print("Anger: " + str(sum(anger) / len(anger)))
    print("Fear: " + str(sum(fear) / len(fear)))
    print("Disgust: " + str(sum(disgust) / len(disgust)))
    print("Joy: " + str(sum(joy) / len(joy)))
    print("Sadness: " + str(sum(sadness) / len(sadness)))

    return anger, fear, disgust, joy, sadness


# Returns the json for analysis of a single string of any length
def analyze_single(text, username, password):
    if sys.version_info[0] == 2:  # Python 2
        url = "https://gateway.watsonplatform.net/tone-analyzer-beta/api/v3/" \
              "tone?version=2016-02-11&tones=emotion&sentences=false&text=" + urllib.quote(text.encode('utf-8'))
    elif sys.version_info[0] == 3:  # Python 3
        url = "https://gateway.watsonplatform.net/tone-analyzer-beta/api/v3/" \
              "tone?version=2016-02-11&tones=emotion&sentences=false&text=" + urllib.parse.quote(text.encode('utf-8'))

    else:
        raise Exception("Unsupported Python version. 2.7 and 3.x should both work fine.")

    req = requests.get(url, auth=(username, password))
    return req.json()


if __name__ == '__main__':
    argv = sys.argv

    if len(argv) == 4:
        analyze(argv[1], argv[2], argv[3])
    else:
        raise Exception("Wrong number of arguments.")
