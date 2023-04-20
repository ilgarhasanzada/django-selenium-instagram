from celery import shared_task
from .models import Instagram
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@shared_task
def check_instagram_profile():
    for user in Instagram.objects.all():
        profile_url = f"https://www.instagram.com/{user.username}"

        driver = webdriver.Chrome()

        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        driver.find_element('name',"username").send_keys(user.username)
        driver.find_element('name',"password").send_keys(user.password)
        driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button").click()
        time.sleep(5)

        driver.get(profile_url)
        time.sleep(5)

        followers = driver.find_element(By.XPATH,"//a[contains(@href,'followers')]/span")
        user.followers = followers.text

        following = driver.find_element(By.XPATH,"//a[contains(@href,'following')]/span")
        user.following = following.text
        user.save()

        driver.quit()

    return "added"