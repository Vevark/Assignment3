# Assignment 3 of ACC

Using RabbitMQ as the borker for the Celery, and using Flask to show a json document as well.

The data is json files of Tweets given by the teacher. When handling the data, follow https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/calculate-tweet-word-frequencies-in-python/.

The goal is to count Swedish pronouns frequencies in unique Tweets (not considering ReTweets).

1. Follow https://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#broker-rabbitmq to install and configure RabbitMQ.

2. Follow https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#first-steps to get familiar with Celery.

## Be careful to Python version!

3. Run the Celery worker server

```bash
celery -A celery worker -l INFO
```

In this case, the second 'celery' is the module name of celery.

4. Run the task on the Celery server, and get the result as 'result.json' and 'visualization.png'.

```bash
python run.py
```
5. Run the Flask (REST API) server

```bash
python run_flask.py
```

## All steps above are done on a VM

6. Show the josn file through Flask (in another terminal, e.g. own PC or laptop)

```bash
curl -i http://ip_address:5000/result
```
