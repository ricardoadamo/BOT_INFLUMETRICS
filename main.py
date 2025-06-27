from instaloader import Instaloader, Profile

print("BOT_INFLUMETRICS funcionando!")

L = Instaloader()
print("Instaloader carregado!")

username = 'influcall.bot'
password = 'InflumetricsTest!'
L.login(username, password)
print("Login feito!")

profile = Profile.from_username(L.context, 'instagram')

followers = profile.get_followers()

lista = []
for seguidor in followers:
    lista.append(seguidor.username)

print("Seguidores capturados:", lista)
