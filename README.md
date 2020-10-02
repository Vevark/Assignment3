# Applied-Cloud-Computing-Assignment-III
Using RabbitMQ as the borker for the Celery, and using Flask to show a json document as well.
The data is json files of Tweets given by the teacher.
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
5. Show the josn file through Flask
```bash
curl -i http://ip_address:5000/result
```
