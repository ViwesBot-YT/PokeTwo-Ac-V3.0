import re, os, asyncio, random, string, keep_alive
from discord.ext import commands, tasks

version = 'v8.3'

bot_prefix = '&'  #Your Bot Prefix

#Put EveryThing in Secret Variable
user_token = os.environ['user_token']  #Your Token 

spam_id = os.environ['spam_id'] #Channel id Where to Spam

catch_id = os.environ['catch_id'] #Channel id Where Pokemon will spawn

logs_id = os.environ['logs_id'] #Channel id Where Catch will be Logged

captcha_ping = os.environ['captcha_ping'] #User id to Ping when Captcha come 

user_id = 938357274982879252 #The User id Who can use Say Command 
#Change User id To Your User id to use say command 

try:
    logs_id 
except:
    logs_id = False
try:
    captcha_ping 
except:
    captcha_ping = False

sh_interval = False

with open('data/pokemon', 'r', encoding='utf8') as file:
    pokemon_list = file.read()
with open('data/legendary', 'r') as file:
    legendary_list = file.read()
with open('data/mythical', 'r') as file:
    mythical_list = file.read()
with open('data/level', 'r') as file:
    to_level = file.readline()

num_pokemon = 0
shiny = 0
legendary = 0
mythical = 0

poketwo = 716390085896962058  #Pokétwo's ID

client = commands.Bot(command_prefix=bot_prefix)
stopped = False
captcha_done = True

intervals = [3, 12.2, 12.8, 13.2]  #Set Spam Interval. Dont Put Below 2


def solve(message):
    if not stopped:
        hint = []
        for i in range(15, len(message) - 1):
            if message[i] != '\\':
                hint.append(message[i])
        hint_string = ''
        for i in hint:
            hint_string += i
        hint_replaced = hint_string.replace('_', '.')
        solution = re.findall('^' + hint_replaced + '$', pokemon_list,
                              re.MULTILINE)
        return solution


@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    await channel.send(''.join(
        random.sample(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 7) *
        5))


@spam.before_loop
async def before_spam():
    await client.wait_until_ready()


spam.start()


@client.event
async def on_ready():
    print(f'Logged into account: {client.user.name}')


@client.event
async def on_message(message):
    global stopped
    global captcha_done
    channel = client.get_channel(int(catch_id))
    if logs_id:
        logs_channel = client.get_channel(int(logs_id))
    if message.channel.id == int(catch_id):
        if message.author.id == poketwo:
            if not stopped:
                if message.embeds:
                    embed_title = message.embeds[0].title
                    if 'wild pokémon has appeared!' in embed_title and not stopped:
                        spam.cancel()
                        await asyncio.sleep(5)  #Hint Delay, ffs not do 1
                        await channel.send('<@716390085896962058> h')
                    elif "Congratulations" in embed_title:
                        embed_content = message.embeds[0].description
                        if 'now level' in embed_content:
                            split = embed_content.split(' ')
                            a = embed_content.count(' ')
                            level = int(split[a].replace('!', ''))
                            if level == 100:
                                await channel.send(f".s {to_level}")
                                with open('data/level', 'r') as fi:
                                    data = fi.read().splitlines(True)
                                with open('data/level', 'w') as fo:
                                    fo.writelines(data[1:])
                else:
                    content = message.content
                    if 'The pokémon is ' in content:
                        if not len(solve(content)):
                            print('Pokemon not found.')
                        else:
                            for i in solve(content):
                                await asyncio.sleep(6)  #Catch Delay
                                await channel.send(
                                    f'<@716390085896962058> c {i}')
                        check = random.randint(1, 60)
                        if check == 1:
                            await asyncio.sleep(900)
                            spam.start()
                        else:
                            await asyncio.sleep(1)
                            spam.start()

                    elif 'Congratulations' in content:
                        global shiny
                        global legendary
                        global num_pokemon
                        global mythical
                        num_pokemon += 1
                        split = content.split(' ')
                        pokemon = split[7].replace('!', '')
                        if 'seem unusual...' in content:
                            shiny += 1

                            print('ㅤㅤㅤㅤ')
                            print(
                                '-----------------------------------------------'
                            )
                            print(f'    ⭐ A SHINY Pokémon was caught! ⭐')
                            print('ㅤㅤㅤㅤ')
                            print(f'    → Total Pokémon Caught: {num_pokemon}')
                            print(f'    → Mythical Pokémon Caught: {mythical}')
                            print(
                                f'    → Legendary Pokémon Caught: {legendary}')
                            print(f'    → Shiny Pokémon Caught: {shiny}')
                            print(
                                '-----------------------------------------------'
                            )
                            print('ㅤㅤㅤㅤ')

                            if logs_id:
                                await logs_channel.send(
                                    f'```⭐ A SHINY Pokémon was caught! ⭐```\n→ Total Pokémon Caught: {num_pokemon}\n→ Mythical Pokémon Caught: {mythical}\n→ Legendary Pokémon Caught: {legendary}\n→ Shiny Pokémon Caught: {shiny}'
                                )

                        elif re.findall('^' + pokemon + '$', legendary_list,
                                        re.MULTILINE):
                            legendary += 1

                            print('ㅤㅤㅤㅤ')
                            print(
                                '-----------------------------------------------'
                            )
                            print(f'     💎 A LEGENDARY Pokémon was caught! 💎')
                            print('ㅤㅤㅤㅤ')
                            print(
                                f'     → Total Pokémon Caught: {num_pokemon}')
                            print(
                                f'     → Mythical Pokémon Caught: {mythical}')
                            print(
                                f'     → Legendary Pokémon Caught: {legendary}'
                            )
                            print(f'     → Shiny Pokémon Caught: {shiny}')
                            print(
                                '-----------------------------------------------'
                            )
                            print('ㅤㅤㅤㅤ')

                            if logs_id:
                                await logs_channel.send(
                                    f'```💎 A LEGENDARY Pokémon was caught! 💎```\n→ Total Pokémon Caught: {num_pokemon}\n→ Mythical Pokémon Caught: {mythical}\n→ Legendary Pokémon Caught: {legendary}\n→ Shiny Pokémon Caught: {shiny}'
                                )

                        elif re.findall('^' + pokemon + '$', mythical_list,
                                        re.MULTILINE):
                            mythical += 1

                            print('ㅤㅤㅤㅤ')
                            print(
                                '-----------------------------------------------'
                            )
                            print(f'     💥 A MYTHICAL Pokémon was caught! 💥')
                            print('ㅤㅤㅤㅤ')
                            print(
                                f'     → Total Pokémon Caught: {num_pokemon}')
                            print(
                                f'     → Mythical Pokémon Caught: {mythical}')
                            print(
                                f'     → Legendary Pokémon Caught: {legendary}'
                            )
                            print(f'     → Shiny Pokémon Caught: {shiny}')
                            print(
                                '-----------------------------------------------'
                            )
                            print('ㅤㅤㅤㅤ')

                            if logs_id:
                                await logs_channel.send(
                                    f'```💥 A MYTHICAL Pokémon was caught! 💥```\n→ Total Pokémon Caught: {num_pokemon}\n→ Mythical Pokémon Caught: {mythical}\n→ Legendary Pokémon Caught: {legendary}\n→ Shiny Pokémon Caught: {shiny}'
                                )

                        else:
                            print('ㅤㅤㅤㅤ')
                            print(
                                '-----------------------------------------------'
                            )
                            print(f'     A new Pokémon was caught!')
                            print('ㅤㅤㅤㅤ')
                            print(
                                f'     → Total Pokémon Caught: {num_pokemon}')
                            print(
                                f'     → Mythical Pokémon Caught: {mythical}')
                            print(
                                f'     → Legendary Pokémon Caught: {legendary}'
                            )
                            print(f'     → Shiny Pokémon Caught: {shiny}')
                            print(
                                '-----------------------------------------------'
                            )
                            print('ㅤㅤㅤㅤ')

                            if logs_id:
                                await logs_channel.send(
                                    f'```A new Pokémon was caught!```\n→ Total Pokémon Caught: {num_pokemon}\n→ Mythical Pokémon Caught: {mythical}\n→ Legendary Pokémon Caught: {legendary}\n→ Shiny Pokémon Caught: {shiny}'
                                )

                    elif 'human' in content:
                        spam.cancel()
                        if logs_id:
                            await logs_channel.send(
                                f"```Oops! Captcha detected!```\nYour autocatcher was paused because a pending captcha. Check your catch channel and use the command '%captcha_done' to confirm the autocatcher can continue."
                            )
                            if captcha_ping:
                                await logs_channel.send(
                                    f'Captcha Ping: <@{captcha_ping}>')

                            print(
                                "Captcha detected! Please use '%captcha_done' in discord to reactivate the autocatcher!"
                            )
                            spam.cancel()
                            stopped = True
                            captcha_done = False
    if not message.author.bot:
        await client.process_commands(message)


@client.command()
async def stop(ctx):
    if captcha_done:
        global stopped
        await ctx.send(
            "```→ The autocatcher was stopped. Use '%start' to run it again.```"
        )
        spam.cancel()
        stopped = True
    else:
        await ctx.send(
            "You can't stop the autocatcher while there's a pending captcha! Use `%captcha_done` instead."
        )


@client.command()
async def start(ctx):
    if captcha_done:
        global stopped
        await ctx.send(
            "```→ The autocatcher was started. Use '%stop' to stop it again.```"
        )
        spam.start()
        stopped = False
    else:
        await ctx.send(
            "You can't start the autocatcher while there's a pending captcha! Use `%captcha_done` instead."
        )


@client.command()
async def captcha_done(ctx):
    global captcha_done
    global stopped
    if captcha_done == True:
        await ctx.send("```There aren't any pending captcha!```")

    else:
        await ctx.send(
            "```Captcha confirmed! Autocatcher has been reactivated!```")
        stopped = False
        spam.start()
        captcha_done = True



@client.command()
async def say(ctx, *, arg):
    if ctx.author.id == user_id:
        try:
            await ctx.send(arg)

        except:
            await ctx.send('``→ Put a message to say!``')
    else:
        await ctx.send("This command is not allowed for your user ID.")      

@client.command()
async def show(ctx, *, text):
    if ctx.author.id != user_id:
        await ctx.send("This command is not allowed for your user ID.")
        return
    
    if text.lower() == 'rare': #show rare
        await asyncio.sleep(2)
        await ctx.send('<@716390085896962058>p --leg --myth --ub')
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --sh')
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --ev')
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --al')
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --ga')
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --hi')
    elif text.lower() == 'iv': #show iv
        await asyncio.sleep(2)
        await ctx.send('<@716390085896962058>p --iv >90')
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --iv <10')
    elif text.lower() == 'duel': #show duel
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n rayquaza --hpiv >23 --atkiv >10 --defiv >23 --spdiv 31')

        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n eternatus --hpiv >25 --defiv >26 --spatkiv >20 --spdefiv >27 --spdiv 31')

        await asyncio.sleep(5)  
        await ctx.send('<@716390085896962058>p --n groudon --hpiv >23 --atkiv >17 --defiv >17 --spdefiv >26 --spdiv >28')

        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n kyogre --hpiv >25 --defiv >26 --spatkiv >10 --spdiv 31')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n dialga --hpiv >15 --spatkiv >19 --spdefiv >18 --spdiv >28')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n regigigas --hpiv >10 --atkiv >6 --defiv >6 --spdefiv >11 --spdiv 31')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n arceus --hpiv >15 --defiv >16 --spatkiv >20 --spdiv >28')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n yveltal --hpiv >23 --atkiv >13 --defiv >9 --spdefiv >17 --spdiv 31')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n yveltal --hpiv >23 --atkiv >24 --defiv >23 --spdefiv >17 --spdiv >13')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n xerneas --hpiv >15 --atkiv >26 --spdefiv >15 --spdiv >28')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n giratina --hpiv >25 --defiv >25 --spdiv >28')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n mewtwo --hpiv >24 --defiv >25 --spatkiv >9 --spdiv >28')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n slakoth --spdiv 31 --hpiv >20 --atkiv >29 --defiv >21')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n beldum --n metang --n metagross --hpiv >14 --atkiv >19 --defiv >14 --spdiv >29')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n wimpod --n golisopod --hpiv >21 --atkiv >22 --defiv >22 --spdefiv >16')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n magikarp --n gyarados --hpiv >16 --atkiv >19 --defiv >16 --spdefiv >12 --spdiv >25')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n bagon --n shelgon --n salamence --spdiv >28 --hpiv >23 --defiv >23 --atkiv >21')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n gible --n gabite --n garchomp --hpiv >19 --atkiv >25 --defiv >19 --spdefiv >17 --spdiv >28')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n ralts --n kirlia --n gardevoir --hpiv >21 --defiv >22 --spatkiv >16 --spdefiv >15 --spdiv 31')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n abra --n kadabra --n alakazam --hpiv >7 --defiv >8 --spatkiv >21 --spdiv >21')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n gastly --n haunter --n gengar --hpiv >19 --defiv >19 --spatkiv >15 --spdiv >27')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n froakie --n frogadier --n greninja --hpiv >22 --atkiv >14 --defiv >23 --spatkiv >23 --spdefiv >15 --spdiv >27')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n axew --n fraxure --n haxorus --hpiv >24 --atkiv >23 --spdefiv >24')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n Ampharos --n mareep --n flaaffy --hpiv >20 --spatkiv >23 --defiv >20 --spdefiv >15')
        
        await asyncio.sleep(5)
        await ctx.send('<@716390085896962058>p --n larvitar --n pupitar --n tyranitar --hpiv >18 --atkiv >21 --defiv >11 --spdefiv >19')

    else:
        await ctx.send("type either &show iv or rare or duel")
      
print(
    f'Pokétwo Autocatcher {version}\nA free and open-source Pokétwo autocatcher Modified by Viwes Bot & Sernon158\nEvent Log:'
)
keep_alive.keep_alive()
client.run(f"{user_token}")

# Congratulations! You readed our code! You won a PlayStation 25!