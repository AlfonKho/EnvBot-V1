import discord
from discord.ext import commands
from botlogic import pass_gen

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passgen(ctx):
    await ctx.send("Halo berikut adalah password kamu:") 
    await ctx.send(pass_gen(8))

@bot.command()
async def pangkatdua(ctx):
    await ctx.send("Masukkan angka bebas, nanti aku hitung pangkat 2 nya")
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    await ctx.send(f"pangkat 2 dari angka yang kamu kirimkan adalah {(int(message.content)**2)}")

@bot.command()
async def meme(ctx):
    import random, os
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animal(ctx):
    import random, os
    animal_meme = random.choice(os.listdir("Animal Meme"))
    with open(f'Animal Meme/{animal_meme}', 'rb',) as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():
    import requests
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command("duck")
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

sampah = ["botol plastik", "koran", "majalah",
          "botol kaca", "kaleng minuman", "wadah makanan"
          "pakaian bekas", "kain bekas" "komponen barang elektronik bekas",]

@bot.command()
async def cek_sampah(ctx):
    await ctx.send("Apa sampah yang ingin kamu periksa")
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message)

    #proses pemeriksaan
    if message.lower() in sampah:
        await ctx.send("Sampah tersebut harus di daur ulang, berikut cara mendaur ulang nya")
        await ctx.send("https://youtu.be/ts0DYCU5cM8?si=tlermtJLM-A6Ymur")
    else:
        await ctx.send("Sampah tersebut tidak dapat dimusnahkan dengan bijak")
        await ctx.send("https://benpas.subang.go.id/berita/sering-tertukar-kenali-jenis-sampah-daur-ulang-dan-tak-bisa-daur-ulang")
