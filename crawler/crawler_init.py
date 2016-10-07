from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import crawler.config as global_config


class smtm_crawler():
    def __init__(self, email, pwd, target):
        self.email = email
        self.pwd = pwd
        self.target = target

        self.options = Options()
        self.options.add_argument("--disable-notifications")
        # self.options.add_argument("--start-fullscreen")

        self.config = global_config.Fb_config(self.target)
        self.driver = None

    def init(self):
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get("http://www.facebook.org")

        assert "Facebook" in self.driver.title

        self.__signin()

    def __signin(self):
        elem = self.driver.find_element_by_id("email")
        elem.send_keys(self.email)
        elem = self.driver.find_element_by_id("pass")
        elem.send_keys(self.pwd)
        elem.send_keys(Keys.RETURN)

        if self.config.LOGIN_FAILED_TEXT in self.driver.title:
            print("로그인에 실패하였습니다.<br/>")
            quit()

        print("로그인에 성공했습니다.<br/>")

    def start(self):
        data={}
        for key, value in self.config.url_list.items():
            access = yield from self.__access_target(key, value[0], value[1])
            if access:
                yield from self.__scroll_end()
                yield("글을 긁는 중입니다.<br/>")
                posts = self.driver.find_elements_by_css_selector(value[2])

                text_data = ''

                for post in posts:
                    text_data = text_data + post.text

                data[key] = text_data

        yield("페이스북 스크롤이 모두 완료되었습니다.<br/>")
        self.driver.close()
        # return data

    def __access_target(self, key, scope, scope_url):
        yield(self.target + " " + scope + " 에 접근 중입니다.<br/>")

        self.driver.get(scope_url)
        self.driver.implicitly_wait(3)

        # TODO : 로깅 모듈 사용
        if key in self.driver.current_url:
            return True
        elif self.driver.title == "페이지를 찾을 수 없음":
            yield("Error : 페이지를 찾을 수 없음.<br/>")
            return False
        elif key not in self.driver.current_url:
            yield("Warning : 회원이 해당 내용을 공개하지 않았습니다.<br/>")
            return False

    def __scroll_wait(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.implicitly_wait(1)  # seconds

    def __scroll_end(self):
        # TODO : Try Catch 안하고 사용할 수 있는 셀레늄 함수 찾아보기
        try:
            if self.config.NOT_FOUND_TEXT in self.driver. \
                find_element_by_css_selector(self.config.NOT_FOUND_CLASS).text:
                yield("결과가 존재하지 않습니다.<br/>")
                return False
        except:
            pass

        while True:
            yield("스크롤 하는 중입니다.<br/>")
            try:
                if self.driver.find_element_by_css_selector(self.config.STOP_CLASS).is_displayed():
                    break
            except:
                pass

            self.__scroll_wait()
