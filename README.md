# Controlling-Long-Running-Processes-in-Containers-using-Python

A python API which gains more control over processes running in docker containers. While sending GET request to localhost at port 5000 with endpoint /contain, it returns the dictionary of running containers. Then user can send POST request using name of running container along with the desired action like pause, resume or terminate. Pause will pause the processes running inside particular container, Resume will resume the paused process of container and Terminate will stop the container.

#### NOTE: Before calling the API you need to start it. For that you can either run the atlan.py locally and then perform the below steps or create docker image of file then run it in container and use the below commands in python idle/shell. Check the "Creating docker image" file for more reference. 

## Check out the following steps to use the API :-

#### Send GET requests to localhost at port 5000. You can change it in atlan.py and replace 5000 with some other port.

response = requests.get('http://127.0.0.1:5000/contain')
print(response.text)

You will get OUTPUT similar to this. It is a list of dictionary which contains Running Container names and their ID. Along with that you will also get a success code 200.

### OUTPUT :-
[
    {
        "xenodochial_ganguly": "f3e9c94fcf9578f363b4c19306575eba5bbb03a8a76f750928d63b7f6d03b0a5",
        "happy_ritchie": "e3ec74b67e663f407727390441d09b0e272ca4b5e00a83a3502e9601d48deffe",
        "confident_mayer": "48982da3b12d82e521b1435416c314103b61833e6cbf3a6e9eea5135e5be2f51"
    },
    {
        "200": "send POST request to the /container_name to pause,resume & terminate "
    }
]

#### Now to perform some action on running processes in your container, you will need to send POST request to api with the running container name and specify the action in it.

post_response = requests.post('http://127.0.0.1:5000/contain?ContainerName=confident_mayer&Pause=pause')
post_response.text

#### This will pause the processes running inside the container. And return status code with string.

'{\n    "200": "confident_mayer is paused."\n}\n'

#### To resume the processes follow the next line.

post_response = requests.post('http://127.0.0.1:5000/contain?ContainerName=confident_mayer&Resume=resume')
post_response.text

#### This will resume the paused processes and will return the following status code.

'{\n    "200": "confident_mayer is resumed."\n}\n'

#### Last but not the least ! To terminate the running processes inside container follow the next line.

post_response = requests.post('http://127.0.0.1:5000/contain?ContainerName=confident_mayer&Terminate=terminate')
post_response.text

#### This will stop the container and return the following.

'{\n    "200": "confident_mayer is terminated."\n}\n'
