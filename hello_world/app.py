import boto3
import os
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, CORSConfig
from aws_lambda_powertools.utilities.validation import validate
from aws_lambda_powertools.event_handler.exceptions import NotFoundError, BadRequestError

tracer = Tracer()
logger = Logger()
dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table(os.environ.get("USERS_TABLE"))

cors_config = CORSConfig()
app = APIGatewayRestResolver(cors=cors_config)

@app.post("/users")
@tracer.capture_method
def new_user():
    body = app.current_event.json_body

    # setup the User record for dynamodb item
    user = { "email" : body.get("email"), "name": body.get("name"), "username": body.get("username"), "password": body.get("password")}
    table.put_item(Item=user)

    return {"message": "ok"}

@app.get("/users/<email>")
@tracer.capture_method
def get_user(email):
    if email == "":
        raise BadRequestError("no email provided")

    user = table.get_item(Key={"email": email})
    if not 'Item' in user:
        raise NotFoundError("user not found")

    return user.get("Item")

@app.get("/hello/<name>")
@tracer.capture_method
def get_hello_universe(name):
    if name == "michael":
        name = "michael, go away!"
    return {"message": f"hello {name}"}

# You can continue to use other utilities just as before
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
