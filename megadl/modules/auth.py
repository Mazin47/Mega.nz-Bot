@CypherClient.on_message(filters.command("login"))
@CypherClient.run_checks
async def mega_logger(client: CypherClient, msg: Message):
    if msg.chat.type != ChatType.PRIVATE:
        return await msg.reply("`You can only login in private chats for obvious reasons`")

    if not client.cipher:
        return await msg.reply("`Cipher not initialized. Check your setup.`")

    user_id = msg.chat.id

    email = await client.ask(user_id, "`Enter your😅 Mega.nz email:`")
    if not email:
        return await msg.reply("You` **must** `send your Mega.nz email in order to log in")
    
    password = await client.ask(user_id, "`Enter your Mega.nz password:`")
    if not password:
        return await msg.reply("`You` **must** `send your Mega.nz password in order to log in`")

    email = client.cipher.encrypt(email.text.encode())
    password = client.cipher.encrypt(password.text.encode())

    await client.database.mega_login(user_id, email, password)
    await msg.reply("`Successfully logged in ✅`")
