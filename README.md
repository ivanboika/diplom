# Setup

## Server
1. Open Docker
2. Open Terminal and move to the repository where project was cloned
3. Run __docker-compose up --build__
4. Wait (I don't how much time it will take on the different system, but for me it takes around 20 minutes)

## Client
1. Inside client folder create virtual environment (can be created via PyCharm or terminal commands)
2. Activate it(recently created virtual enviroment)
3. Run __pip install -r requirements.txt__
4. Wait (Much faster than server)
5. Also setup a run configuration(if you're using PyCharm), otherwise, I guess, you just only need to choose the created environment with installed dependencies

## Usage

1. Even after installing server part, model installing is going to take some time(less than 5 minutes). You'll see in a log that models and server are started,
otherwise something wrong happened
2. Run client and try to record some audio. To stop recording push __Enter__ button.
3. To text button makes 2 requests to the server. First one to STT model to recognize speech, second one to the translation model.
4. If nothing was returned it means that STT model doesn't recognize your speech. That's a problem of current STT model - VOSK. To be more specific, the size of the model. Maybe there are more reasons of that.
5. System also allows to listen last audio that you've recordered to check quality of sound and being different noice sounds in record.

# Issues

1. The current STT model as I metioned can't recognize speech so good that I've wanted before. Probably I should try another model(like Whisper)
2. Punctuation (I've heard that Whisper takes into account punctuation)
3. Sizes of model and time to deploy server (There is no need to explain, it takes too much time and therefore it slows development and testing)

# Suggetions
1. Move core docker file(wsl disk image) to the another system disk. Otherwise this can eat all your memory
