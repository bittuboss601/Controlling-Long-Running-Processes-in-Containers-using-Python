from flask import Flask
from flask_restful import Resource, Api, reqparse
import docker

app = Flask(__name__)
api = Api(app)


class Contain(Resource):
    def get(self):
        client = docker.from_env()
        c = {}
        for container in client.containers.list():
            c[container.name] = container.id
        if len(c) > 0:
            return [c,{200:'send POST request to the /container_name to pause,resume & terminate '}]
        else:
            return 'No containers are running'

    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('ContainerName', required=True)  # add args
        parser.add_argument('Pause', required=False)
        parser.add_argument('Resume', required=False)
        parser.add_argument('Terminate', required=False)

        args = parser.parse_args()  # parse arguments to dictionary
        if 'pause' in args.values():
            client = docker.from_env()
            for container in client.containers.list():
                if container.name == args['ContainerName']:
                    container.pause()
                    return {200:container.name+' is paused.'}

        elif 'resume' in args.values():
            client = docker.from_env()
            for container in client.containers.list():
                if container.name == args['ContainerName']:
                    container.unpause()
                    return {200:container.name+' is resumed.'}

        elif 'terminate' in args.values():
            client = docker.from_env()
            for container in client.containers.list():
                if container.name == args['ContainerName']:
                    container.stop()
                    return {200:container.name+' is terminated.'}



api.add_resource(Contain, '/contain')  # add endpoints
if __name__ == '__main__':
    app.run()  # run our Flask app        
