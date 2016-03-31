# tone-analyzer
Little Python script to play with IBM Watson and its tone analyzer. Reads in a directory of text files, each of which must not be empty. Prints out the mean anger, fear, disgust, joy, and sadness associated with the files in the directory. 

## Usage
```
python tone_analyze.py <dir_name> <username> <password>
```

`dir_name` is the directory where your files are located. For example, `./files/example` would work on all of the files located beneath the `example` directory.

`username` is the IBM Bluemix username associated with your Tone Analyzer service. `password` is the password. 

## Questions? Improvements?

[Give me a shout](mailto:me@ericzaporzan.com). Or make a pull request. 
