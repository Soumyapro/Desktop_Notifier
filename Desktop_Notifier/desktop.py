import time
import json
from plyer import notification

class DesktopNotifier:
    def __init__(self):
        self.new_data = None

    def setup_notifier(self):
        with open('news.json','rb') as file:
            self.new_data = json.load(file)
            file.close()

        articles = self.new_data.get('articles',[])

        if articles:
            articles_info = articles[0]['description']
            articles_title = articles[0]['title'][:64]
            notification.notify(
                title = articles_title,
                message = articles_info,
                timeout = 10,
            )
            time.sleep(10)

        else:
            print("No articles found")


if __name__ == '__main__':
    notifier = DesktopNotifier()
    notifier.setup_notifier()

