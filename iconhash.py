import requests
import base64
import mmh3
import threading

class IconHash:
    def __init__(self, ui):
        self.ui = ui

    def icohash(self):
        self.ui.textBrowser.clear()
        your_search = self.ui.ico_hash.text()

        self.ui.shuchu.append(f'iconhash正在查询 ==> {your_search}，请稍后...' + '\n')

        thread = threading.Thread(target=self.icohash_threadSend,
                                  args=(your_search,))
        thread.start()

    def icohash_threadSend(self, your_search):
        try:
            r = requests.get(your_search)
            favicon = base64.encodebytes(r.content)
            hash = mmh3.hash(favicon)
            result = 'icon_hash="{}"'.format(hash)
            self.ui.textBrowser.append(result)
            self.ui.shuchu.append(result + '\n')
            self.ui.shuchu.append('icon_hash 已查询完成' + '\n' + '-' * 29)
            print(result)
        except requests.exceptions.MissingSchema as e:
            self.ui.shuchu.append(str(e) + '\n' + '-' * 29)
        except requests.exceptions.ConnectionError as e:
            self.ui.shuchu.append(str(e) + '\n' + '-' * 29)
