import gym
import random

from tensorflow.keras.models import Sequential


env = gym.make('CartPole-v0')
height, width, channels = env.observation_space.shape
actions = env.action_space.n



episodes = 5

for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = random.choice([1,2,3,4,5,])
        n_state, reward, done, info = env.step(action)
        score+= reward
    print("fjdsklfj")

env.close()
