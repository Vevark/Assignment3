from run_celery import count

res = count.delay()
# print(res.get())
print(res.id)
print(res.state)
