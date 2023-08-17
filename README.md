# Unscramble_Jumbles
This Python script allows you to unscramble jumbled words and provides their possible meanings using NLTK and WordNet.

## How to Use

1. Clone this repository to your local machine.

```shell
git clone https://github.com/semeer37/Unscramble_Jumbles.git
```

2. Install the required dependencies listed in the requirements.txt file:
```shell
pip install -r requirements.txt
```

3. Install the required dependencies (NLTK and WordNet):

```shell
pip install nltk
python -m nltk.downloader words
python -m nltk.downloader wordnet
```

4. Run the script:

```shell
python unscramble_words.py
```

5. Enter single or comma-separated jumbled words when prompted. For example:

```shell
Enter single or comma-separated jumbled words (or type 'q' to quit): cimt, olve, saple
```

6. The script will provide you with possible unscrambled words for each input along with their meanings.

## Requirements

- Python 3.x
- NLTK library

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute by opening issues or pull requests!
