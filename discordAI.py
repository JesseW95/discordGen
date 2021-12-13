import datetime
import os
import re
import subprocess
import discord
from discord.ext import commands
from random import seed
from random import randint
import yaml
import tweepy
import emoji

# set up API tokens for using discord/twitter services
yaml_file = open('configs.yml', 'r')
creds = yaml.load(yaml_file, Loader=yaml.FullLoader)
try:
    t_consumer_key = creds['t_api_key']
    t_consumer_secret = creds['t_api_secret']
    t_access_token = creds['t_access_token']
    t_access_secret = creds['t_access_secret']
    t_bearer = creds['t_bearer_token']
    d_token = creds['d_token']
except ValueError:
    print('Value does not exist or is invalid.')
# initiate seed random for generation consistency
seed(823)

auth = tweepy.OAuthHandler(t_consumer_key, t_consumer_secret)
auth.set_access_token(t_access_token, t_access_secret)
t_api = tweepy.Client(bearer_token=t_bearer, consumer_key=t_consumer_key, consumer_secret= t_consumer_secret,
                      access_token=t_access_token, access_token_secret=t_access_secret)

tweetedMessages = []
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.user:
            return

        # If bot is mentioned, reply with a messagewhe
        if self.user in message.mentions:
            intgen = randint(1, 99999)
            text = message.content
            servName = message.guild.name
            text = re.sub(r"<!*.+>", "", text, 1)
            text = text.replace("\"", "\\\"")
            out = subprocess.check_output("conda activate tweetGen2 && python generate.py \"%s\" %d" % (text, intgen),
                                          cwd=os.getcwd(), shell=True, encoding='utf-8', errors="ignore")
            # the \bs are for getting rid of the [0m in every string
            logtext = "[%s][%s]" % (str(datetime.datetime.now().strftime('%m-%d-%Y %H:%M')), servName) \
                      + re.sub(r"\|\|\[*.+]\|\|", "", out).strip()
            print(logtext)
            await message.reply(out, mention_author=False)
            return

    async def on_reaction_add(self, reaction, user):
            if reaction.message.author == self.user:
                if type(reaction.emoji) is not str:
                    print(reaction.emoji.name + " added to message \"" + reaction.message.content[:24] + "...\"")
                    if reaction.emoji.name == "KEKW" and reaction.count > 1 and reaction.message.id not in tweetedMessages:
                        text = reaction.message.content
                        text = re.sub(r"\|\|\[*.+]\|\|", "", text)
                        print("Tweeting: \"" + text[:48]+"...\"")
                        t_response = t_api.create_tweet(text=text)
                        tweetedMessages.append(reaction.message.id)
                        await reaction.message.reply("Deemed twitter worthy by my fans "
                                                     "https://twitter.com/jril_bot/status/%s" % t_response.data['id'])
                        return
                    if reaction.emoji.name == "weirdChamp" and reaction.count > 1:
                        await reaction.message.delete()
                        return
                else:
                    emojiStr = emoji.demojize(reaction.emoji)
                    print(emojiStr + " added to message \"" + reaction.message.content[:24] + "...\"")
                    if emojiStr == ":partying_face:" and reaction.count > 1 \
                            and reaction.message.id not in tweetedMessages:
                        text = reaction.message.content
                        text = re.sub(r"\|\|\[*.+]\|\|", "", text)
                        print("Tweeting: \"" + text[:48]+"...\"")
                        t_response = t_api.create_tweet(text=text)
                        tweetedMessages.append(reaction.message.id)
                        await reaction.message.reply("Deemed twitter worthy by my fans "
                                                     "https://twitter.com/jril_bot/status/%s" % t_response.data['id'])
                        return
                    if emojiStr == ":grimacing_face:" and reaction.count > 1:
                        await reaction.message.delete()
                        return


def main():
    client = MyClient()
    client.run(d_token)
    print("")


if __name__ == '__main__':
    main()
