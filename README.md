## 🏆 Pokétwo Autocatcher 🏆
A second generation **free** and open-source Pokétwo autocatcher, created with the goal of preventing people from wasting their money.

---

### Features
The bot has the following features:
- ⚙️ Easy Setup (simply run a script and enter the correct information, no 'coding' needed)
- ⬆️ Control Your Auto-Catcher From Other Account(Main Account) with Say Command
- ✨ Get notified when and if you've caught a Pokémon, and also if another event occurs
    - See when a Shiny/Legendary/Ultra Beast/Mythical Pokémon is caught, and which one it is!
- 💲 **Completely free** and open-source (you can see the code as it is currently)
- 💕 **Trustworthy**; this autocatcher is **completely** open-source (meaning you can see the latest code)
- 📜 Support for all Pokémon from generation I to generation VIII, including all Alolan and Galarian Pokémon
- 🏎️ Super fast; the autocatcher can even handle Incense!
- 🔍 Pokétwo-Resistant - the autocatcher sends a random series of numbers to enhance undetectability
- 📄 Catch Logger - It Logs all the Catch that the bot make in a discord channel and Repl as well
- 🛑 Start and Stop Repl - Command that You can Use to Start or Stop the Bot
- 🏓 Captcha Ping - Ping The Owner when Captcha Appears 

### Getting Started:
To start up the bot on replit, go to the 'Secrets' tab on replit (the lock icon) and in the 'key' area, write `user_token`, and then type in your discord account token in the 'value' section. <br>

```Secrets you have to put```
`user_token` ~~-->~~ The token of the user you want to autocatch <br>
`spam_id` ~~-->~~ The id of the channel in which you want to spam<br>
`catch_id` ~~-->~~ The id of the channel in which you want the bot to spam (First you need to redirect Pokétwo's spawns to that channel)<br>
`logs_id` (Optional) ~~-->~~ The id of the channel in which you want the bot to send all information. Every catch, it sends the type of the pokemon you caught, all pokemon, legendary pokemon, mythical pokemon and shiny pokemon you caught during the time the bot was active. This count sometimes reset if the bot is paused some hours, because captcha or other reasons.<br>
`captcha_ping` (Optional) ~~-->~~ Only works if `logs_id` secret exists. It is the id of the player you want to ping. You can get it right-clicking the guy you want to ping and getting his id.

```Things you can change```
Prefix ~~-->~~ You can change the prefix of the commands of the bot by changing the value of the variable `bot_prefix` on the line 6. Default one is `%`.
`%say` is The Command That You can use to say things from Your main to the bot id. <br>
```Other things```
`%start` and `%stop`commands are used to control the bot without accesing replit or uptime robot. We only recommend using them if you have your bot on uptime robot, else, they will be useless because you need to have replit opened, and if you have it opened, you can stop or start it easily. You can't use them if there's a pending captcha. Use the command below instead.<br>
`%captcha_ping` is used to confirm the pending captcha was done. Obviously, you can only use this if there's a pending captcha.

```Important Details```
`%start`, `%stop` and `%captcha_ping` commands can be used by anyone in any server your alt's in. It's recommended to leave all servers before use autocatcher.

After you've done that, please see the below section.

#### <b>Running</b>
Once you have installed the correct dependencies, click the green 'Run' icon at the top of your webpage. If a new window opens up with 'Bot logged on' written inside, and `Logged into account: <account name>` has appeared into your console, then the bot has successfully started.

> Remember to cd into your autocatcher folder as well. If you need any help with something, feel free to open a Github Issue.
> We recommend using Uptime Robot for 24/7 autocatcher.
<br>
>We Suggest to Join our Discord discord.gg/ayMbtc5JyZ

---

## **DISCLAIMER**

Please note that self botting is against Discord's Terms of Service and being discovered using a self bot may result in your account being banned. To avoid this, keep knowledge of your self bot to a minimum and use a throwaway account. I am not responsible for any accounts lost due to the self bot. I also recommend checking the self bot channel's messages occasionally to see if Pokétwo has sent a captcha. **If it has, it would be a good idea to solve it.**

---
