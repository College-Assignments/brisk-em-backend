```shell
virtualenv -p /usr/bin/python3 quizgen
```

```shell
cd quizgen/bin
source activate envname

# or

source briskenv/bin/activate envname
```

```python
cd question_generation
pip install wikipedia --quiet
# pip install -U transformers==3.0.0 --quiet
pip install -r requirements.txt
python -m nltk.downloader punkt

```

#### git clone https://github.com/patil-suraj/question_generation.git
#### cd question_generation

This project uses code from https://github.com/patil-suraj/question_generation