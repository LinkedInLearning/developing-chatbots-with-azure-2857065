# Steps

1. `pip install -r requirements.txt`
2. `cookiecutter https://github.com/microsoft/botbuilder-python/releases/download/Templates/echo.zip`
3. Download cookiecutter project and give your bot a name and description

```
bot_name [my_chat_bot]: redtech30_product_bot
bot_description [Demonstrate the core capabilities of the Microsoft Bot Framework]: A chatbot that answers questions about products of redtech 30
```

4. Running the application 

- Checkout to the bot directory `cd redtech30_product_bot`
- Install bot specific requirements `pip install -r requirements.txt`
- Run the bot `python app.py`

5. Test Echo Bot

- Start bot emulator
- Copy the API endpoint from previous step `http://localhost:<port>/api/messages` and paste it under bot URL
- Connect and test


