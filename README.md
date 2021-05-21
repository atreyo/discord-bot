# discord-bot
- [Português](#Português) 🇧🇷 
- [English](#English)

## Português 🇧🇷 

Um ambiente python com bot para discord 

clica no link abaixo para conseguir o DISCORD_BOT_TOKEN 
 
https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ 
 
então, substitua YOUR_TOKEN_HERE pelo token: 

```
docker run -it -e DISCORD_BOT_KEY=YOUR_TOKEN_HERE atreyo/discord-bot:latest 
```

ou(preferência) coloque seu TOKEN em um arquivo env

```
docker run -it --env-file env atreyo/discord-bot:latest 
```

Diga $eai e ele vai responder  

## English

A environment python with a discord bot

follow this link below to get a DISCORD_BOT_TOKEN 
 
https://www.freecodecamp.org/news/create-a-discord-bot-with-python/ 
 
then: 

```
docker run -it -e DISCORD_BOT_KEY=YOUR_TOKEN_HERE atreyo/discord-bot:latest 
```

or put your TOKEN in a env file 

```
docker run -it --env-file env atreyo/discord-bot:latest 
```

Say $hello and he will answer back


# thanks Beau Carnes