### AI Text Generator Bot
This project first uses a pre-trained model to generate new texts from given prompts. It then takes that message posts it on discord with stats hidden in spoiler tags on discord.

### Requirements
- Anaconda (I used miniconda)
- A cuda enabled GPU (I use an RTX2070 Super)
- Very basic python knowledge
- Twitter and Discord API access
 - Twitter API access found [here](https://developer.twitter.com/en "here")
  - Discord API access found [here](https://discord.com/developers/applications "here")

### SETUP
#### Setting Up the trained model
Download a model into the directory of this folder, an example model is included using tweets trained from dril & heroicvillain95 (me) on twitter.
If you would like to create a new model from uses tweets I recommend using [this colab](https://colab.research.google.com/github/borisdayma/huggingtweets/blob/master/huggingtweets-demo.ipynb "this colab")

You can then go to the created model on huggingface's site:
https://huggingface.co/huggingtweets/user1-user2-user3
Where 'user1' , 'user2', 'user3' would be replaced by the twitter accounts you trained the model on. Then download this model locally and alter generate.py
`ai = aitextgen(model_folder="dril-heroicvillain95",
               to_gpu=True)` 
Alter to
`ai = aitextgen(model_folder="user1-user2-user3,
               to_gpu=True)"`
#### Setting up configs.yml
After creating your discord and twitter apps through their respective developer pages you need to add the generated access tokens to the configs.yml folder.

#### Setting up anaconda environments
Under construction (environment files will be included)
