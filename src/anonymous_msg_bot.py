import time
import g4f
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


messages = []


def get_ai_response(context=None):
    idea = (
        context
        if not context is None
        else "Donne moi une phrase de drague pour une fille, tu peux beaucoup de personalisation , de romantisme et d'autenticité"
    )

    response = g4f.ChatCompletion.create(
        model=g4f.models.blackboxai,
        messages=[
            {
                "role": "user",
                "content": f"{idea} ta phrase ne doit pas faire partir de cette liste de messages {messages} et doit etre breve ecrite en francais ou en allemand c'est toi qui choisi",
            }
        ],
    )
    return response


def do_magic(link, on_get_response, description=None):

    print("starting magic")
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")

    print("starting driver")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )

    print("driver started")
    while True:
        try:
            print("opening link")
            driver.get(link)
            textarea = driver.find_element(By.TAG_NAME, "textarea")
            textarea.click()
            time.sleep(1)
            msg = get_ai_response(description)
            msg = str(msg).split("\n")[-1].split('"')[1]
            # print(f"=> {msg}\n")
            textarea.send_keys(msg)
            button = driver.find_element(By.TAG_NAME, "button")
            button.click()
            messages.append(msg)
            on_get_response(msg)

            with open("messages.txt", "w") as f:
                for item in messages:
                    f.write("%s\n" % item)

            time.sleep(1)
        except Exception as e:
            print(e)
            continue


# if __name__ == "__main__":
#     do_magic()

#     # msg = get_ai_response()
