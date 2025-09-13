def campus_chatbot():
    print("Hello! i=Iam your smart campus Assistant.")
    print("Ask me about library,canteen,bus,or exam.")
    while True:
        query=input("You:").lower()
        if "library" in query:
            print("Bot: Library is open from 9AM to 12PM.")
        elif"cateen" in query:
            print("Bot: canteen serves food from 8AM to 4PM.")
        elif"bus" in query:
            print("Bot:campus bus leaves every 30 minutes from main gate.")
        elif"exam" in query:
            print("Bot:Goodbye! have a nice day.")
            break
        else:
            print("Bot:sorry, i don't know that yet.")
#funtion calling
campus_chatbot()
