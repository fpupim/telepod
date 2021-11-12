import feedparser
from pyrogram import Client
import urllib
import os

itens = {
    'https://anchor.fm/s/string/podcast/rss': -100telegram_id,
    'https://anchor.fm/s/string/podcast/rss': -100telegram_id,
    'https://anchor.fm/s/string/podcast/rss': -100telegram_id,
    'gerencia': telegram_id,
    }

api_id = api_id
api_hash = api_hash
bot = Client('bot', api_id, api_hash)

diretorio = '/tmp/telepod/'
arquivo = '/usr/share/telepod/log/'


for item in itens:
    feed = feedparser.parse(item)

    for entry in reversed(feed.entries):
        link = entry.link
        
        if open(arquivo+str(itens[(item)])+'.txt').read().find(link) == -1:
            # variables used for general stuff
            author = feed.channel.title
            href = entry.links[1]['href']
            title = entry.title
            description = entry.description
            filepath=diretorio+title+'.mp3'
            
            # download
            data = urllib.request.urlopen(href)
            open(filepath,'wb+').write(data.read())
    
            # upload and deals with files and stuff
            with bot:
                try:
                    bot.send_audio(chat_id=itens[(item)],
                        audio=filepath,
                        title=title,
                        performer=author,
                        caption=title
                        )

                except: # notifies on failure to upload
                    bot.send_message(itens[('gerencia')],
                            text='upload failure: ' + title)
                    os.remove(filepath)

                else: # saves video link 
                    open(arquivo+str(itens[(item)])+'.txt', 'a+').write('\n'+link)
                    os.remove(filepath)
