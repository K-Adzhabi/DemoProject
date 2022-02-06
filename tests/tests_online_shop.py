from pages.login_page import Login


def test_making_an_order(browser):
    login_page = Login(browser)
    login_page.enter_login()

    main_page = login_page.get_main_page()
    main_page.add_product(main_page.LOCATOR_backpack_title)

    shopping_cart_page = main_page.get_shopping_page()
    shopping_cart_page.back_to_products()

    main_page.add_product(main_page.LOCATOR_jaket_title)

    shopping_cart_page = main_page.get_shopping_page()
    shopping_cart_page.back_to_products()

    main_page.add_product(main_page.LOCATOR_tshirt_title)

    shopping_cart_page = main_page.get_shopping_page()
    shopping_cart_page.back_to_products()

    main_page.shopping_bag_button()
    assert shopping_cart_page.element_text(shopping_cart_page.LOCATOR_COUNT_PRODUCT_3) == "3", "Товара не 3"
    main_page.remove_product_name(main_page.LOCATOR_jaket_title)

    shopping_cart_page.remove_button()

    main_page.shopping_bag_button()
    assert shopping_cart_page.element_text(shopping_cart_page.LOCATOR_COUNT_PRODUCT_2) == "2", "Товара не 2"

    shopping_cart_page.checkout_button()

    confirm_page = shopping_cart_page.get_confirm_page()
    confirm_page.info_input()
    confirm_page.continue_button()
    confirm_page.finish_button()

    back_home_page = confirm_page.get_back_home_page()
    back_home_page.back_home()


def test_collation_product_name(browser):
    login_page = Login(browser)
    login_page.enter_login()

    main_page = login_page.get_main_page()
    main_page.add_product(main_page.LOCATOR_backpack_title)
    main_page.shopping_bag_button()

    shopping_cart_page = main_page.get_shopping_page()

    assert main_page.element_text(main_page.LOCATOR_backpack_title) == \
           shopping_cart_page.element_text(shopping_cart_page.LOCATOR_PRODUCT_SHOP), "No"
