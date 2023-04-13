from MeowerBot import Bot, __version__
from os import environ as env
from logging import basicConfig, DEBUG

basicConfig(level=DEBUG)

bot = Bot()


actions = ["rock","paper","scissors"]

def login(*_, **__):
	print("login CB")
	bot.send_msg("TESTING!!!!!!!! O_O", to='home')
	bot.send_msg("MeowerBot.py " + __version__, to='home')




@bot.command(args=1)
def rps(action):
	if action in actions:

	

@bot.command(args=0)
def reloadtime(ctx):
	ctx.send_msg(f"My reload time is {round(bot.autoreload_time)}" )
	

bot.callback(login, cbid="login")


bot.run(env['username'], env['password'])