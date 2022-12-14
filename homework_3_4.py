def main_function(function_name, *args):
    name = function_name.__name__.title().replace('_', ' ')
    print("Имя функции: " + name + ". " + "Аргумент функции:", *args)

def open_browser(browser_name):
    main_function(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    main_function(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    main_function(find_registration_button_on_login_page, page_url, button_text)


open_browser('Safari')
go_to_companyname_homepage('https://vk.com/')
find_registration_button_on_login_page('https://vk.com/', 'Sign in')