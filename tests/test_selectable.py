from pages.selectable_page import SelectablePage

def test_selectable_list():
    page = SelectablePage()
    page.open()
    page.switch_to_list_tab()
    page.select_item(0)
    page.item_should_be_active(0)
