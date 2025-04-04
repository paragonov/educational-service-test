<h2>Test task of company MetaLamp</h2>

To run, you need to copy <b>.env.sample</b> to <b>.env</b>
### Run project locally:

Install uv and run command
```
uv sync
```

Complete migrations
```
uv run python src/manage.py migrate
```

Run project
```
uv run python src/manage.py runserver 0.0.0.0:8000
```

### Run project in docker:

```
docker-compose up --build -d
```
