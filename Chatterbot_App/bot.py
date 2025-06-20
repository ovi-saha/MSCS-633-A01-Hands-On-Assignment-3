from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('TerminalBot', read_only=True)

trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train('chatterbot.corpus.english')

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")