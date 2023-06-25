import AO3
import discord
import os
import dotenv

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
account_name = str(os.getenv("ACCOUNT_NAME"))
series_id = int(os.getenv("SERIES"))

user = AO3.User(account_name)
series = AO3.Series(series_id)
bot = discord.Bot()


@bot.slash_command(name="get_works", description="Get Info about the author's works")
async def get_works(ctx):
    works = []
    threads = []
    string = ""
    for work in series.work_list:
        works.append(work)
        threads.append(work.reload(threaded=True))
    for thread in threads:
        thread.join()

    for i in works:
        string = string + f"Title: {i.title}\nHits: {i.hits}\nKudos: {i.kudos}\n\n"

    await ctx.respond(string)


@bot.slash_command(name="about_me", description="Info about the author")
async def about_me(ctx):
    await ctx.respond(f"Profile: {user.url}\nNumber of works: {user.works}")


bot.run(token)