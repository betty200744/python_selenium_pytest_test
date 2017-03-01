


from actions import driver



def check_is_login_succ():
    pass

def check_is_login_failed():
    assert driver.find_element_by_class_name("problem").is_displayed()




