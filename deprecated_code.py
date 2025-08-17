"""@bot.command(name='check_server')
async def check_server(ctx):
    get_who_called(ctx, "check_server")
    await ctx.send("Checking Fantomland server...")
    server = JavaServer.lookup(fantomland_server_ip)
    try:
        status = server.status()
        await ctx.send("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
    except TimeoutError:
        await ctx.send("Tunnel is dead. Either use !s-restart or tag Prommie.")"""

"""i'm leaving in this function, because you'll never know when would you need JavaServer pckg"""
"""but i already made a better server check function named ping_server()"""
    
"""@bot.command(name='server_ping')
async def server_ping(ctx):
    get_who_called(ctx, "server_ping")
    server = JavaServer.lookup(fantomland_server_ip)
    await ctx.send("The server replied in {0} ms".format(server.ping()))"""

"""@bot.command(name="s-restart")
async def restart_server(ctx):
    get_who_called(ctx, "s-restart")
    if check_process("java.exe"):
        await ctx.send("Restarting server. Please wait.")
        os.system('taskkill /f /im java.exe')
        os.startfile("C:\\Users\\Mozigépész\\Desktop\\run.lnk")
        await ctx.send("Server is starting... Please wait 60 seconds.")
        time.sleep(60)
        server = JavaServer.lookup(fantomland_server_ip)
        await ctx.send("Server is up! Ping: {0}".format(server.status.latency))
    else:
        await ctx.send("I can't restart server. Please tag Prommie.")
        
        ////////////////////////////////////////////////////////////////
        I'm not deleting, because this could be used in the future
        ////////////////////////////////////////////////////////////////
        
        """