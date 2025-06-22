from selene import browser
from selene import have

class SelectablePage:
    def open(self):
        browser.open_url('/selectable')

    def switch_to_list_tab(self):
        browser.element('#demo-tab-list').click()

    def select_item(self, index):
        browser.all('#verticalListContainer li')[index].click()

    def item_should_be_active(self, index):
        browser.all('#verticalListContainer li')[index].should(have.css_class('active'))
