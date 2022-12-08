class Locators():
    base_url = "https://admin.appworkco-beta.com/sessions"
    email_input = 'create_email'
    password_input = 'create_password'
    login_button = '/html/body/div[1]/div/div/form/div[4]/button'
    error_message = '/html/body/div[1]/div[1]'
    sidebar_app = '//*[@id="sidebar-app"]/div/div[4]/div/div/div[1]'
    logout = '//*[@id="sidebar-app"]/div/div[4]/div/div[2]/div/div/div[1]/div[2]'
    logo_url = '/html/body/div[4]/main/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div/input'
    sidebar_popup = '//*[@id="sidebar-app"]/div/div[4]/div/div[2]/div/div/div[2]/div/div'
    settings_button = '//*[@id="sidebar-app"]/div/div[4]/div/div[2]/div/div/div[1]/a[1]'
    #Core Tab
    application_settings = '//*[@id="system-settings-app"]/div/div/a[1]/div'
    setting_logo_url = '//*[@id="application-settings-app"]/div/div/div[3]/div[1]/div'
    primary_color = '//*[@id="rc-editable-input-1"]'
    secondary_color = '//*[@id="rc-editable-input-2"]'
    sidebar_color = '//*[@id="rc-editable-input-3"]'
    sidebar_text = '//*[@id="rc-editable-input-4"]'
    save_button = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div/button'
    rest_logo_url = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[1]/a'
    reset_primary = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[2]/a'
    reset_secondary = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[3]/a'
    reset_sidebar_color = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[4]/a'
    reset_sidebar_text = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[5]/a'
    #Group Block
    group_block = '//*[@id="application-settings-app"]/div/div/div[4]/div[1]/div[2]/div/div[2]'
    new_region = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/div[2]/div[2]'
    region_name = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/div[1]/input'
    save_region1 = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/div[2]/div[2]'
    click_on_selector = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div/div[2]/div/div/div[1]/div[1]'
    select_property1 = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div/div[2]/div/div/div[2]/div[3]/div[1]/div[2]'
    select_property2 = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]'
    search_property1 = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div/div[2]/div/div/div[2]/div[2]/input'
    click_property1 = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div/div[2]/div/div/div[2]/div[3]/div/div[2]'
    click_property2 = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div/div[2]/div/div/div[2]/div[3]/div/div[2]'
    change_name = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[8]/div/div[1]/div[2]/div[1]/div/div[2]'
    update_region = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[8]/div/div[1]/input'
    click_done = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[8]/div/div[1]/div/div[1]/div/div[2]'
    delete_group = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[7]/div/div[1]/div[2]/div[2]/div/div[2]'



    #Edit Region


    #Maintenance Tab under system settings
    maintenance_tab = '//*[@id="application-settings-app"]/div/div/div[3]/div[3]/div'
    workorder_block = '//*[@id="application-settings-app"]/div/div/div[4]/div[1]/div[1]/div/div[1]'
    export_switch_button = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/div/div[2]'
    save_export = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div/button'
    export_reset_default = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/a'
    techs_block = '//*[@id="application-settings-app"]/div/div/div[4]/div[1]/div[2]/div/div[1]'
    maps_switch = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]'
    maps_switch_button = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/div/div[2]'
    tech_save = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div/button'
    reset_tech_maps = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/a'

    #Payment tab Under system settings
    payment_tab = '//*[@id="application-settings-app"]/div/div/div[3]/div[5]/div'
    export_payment = '/html/body/div[4]/main/div/div/div/div/div[4]/div[2]/div[1]/div/div/div[2]'
    save_payment = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div/button'
    reset_payment = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div/a'

    #Property Settings
    property_settings = '//*[@id="application-settings-app"]/div/div/div[1]/div/div[2]/div'
    new_property = '//*[@id="application-settings-app"]/div/div/div[1]/button'
    property_name = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[1]/input'
    enter_code = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[2]/input'
    enter_address = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[3]/input'
    enter_city = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[4]/input[1]'
    click_region = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[4]/div/div/div/div[1]'
    search_region = '//*[@id="react-select-4-input"]'
    select_region = '//*[@id="react-select-4-option-0"]'
    enter_zipcode = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[4]/input[2]'
    enter_integration_id = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[5]/input'
    create_property = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/button'
    select_property = '//*[@id="application-settings-app"]/div/div/div[2]/div[1]/div[2]/div[2]/div/div'
    deactivate_property = '//*[@id="application-settings-app"]/div/div/div[2]/div[2]/button'
    activate_property = '//*[@id="application-settings-app"]/div/div/div[2]/div[2]/button'

    #Update Property Settings
    general_tab = '//*[@id="application-settings-app"]/div/div/div[3]/div[1]/div'
    property_selector = '//*[@id="application-settings-app"]/div/div/div[2]/div[1]/div[1]/div'
    search_property = '//*[@id="application-settings-app"]/div/div/div[2]/div[1]/div[2]/div[1]/input'
    select_property = '//*[@id="application-settings-app"]/div/div/div[2]/div[1]/div[2]/div[2]/div/div'
    update_property_name = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[2]/input'
    update_property_address = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/input'
    update_property_city = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[3]/input[1]'
    update_region = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[3]/div/div/div/div[1]/div[1]/div[1]'
    update_search_region = '//*[@id="react-select-2-input"]'
    update_select_region = '//*[@id="react-select-2-option-0"]'
    update_zipcode = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[3]/input[2]'
    update_property_phone = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[4]/div/div[2]/input'
    update_property_website = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[5]/div/div[2]/input'
    update_property_email = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[6]/div/div[2]/input'
    time_zone = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[8]/div/div/div/div[1]'
    search_timezone = '//*[@id="react-select-3-input"]'
    select_timezone = '//*[@id="react-select-3-option-1"]'
    update_integration_id = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[9]/div/div[2]/input'
    upload_logo = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[2]/div/label/input'
    upload_icon = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[4]/div/label/input'
    upload_banner = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[1]/div[6]/div/label/input'
    save_property = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[10]/button'

    #Documents Block
    document_block  = '//*[@id="application-settings-app"]/div/div/div[4]/div[1]/div[2]/div/div[1]'
    upload_document = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[1]/label/input'
    document_name = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[2]/div[1]/div/div[2]/input'
    file_type = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/div/div[2]/input'
    save_document = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[2]/button'
    view_document = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div[2]/button[1]/i'
    delete_document = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div[2]/button[2]/i'

    #Floor Plan Block
    floor_plan_block = '//*[@id="application-settings-app"]/div/div/div[4]/div[1]/div[3]/div'
    new_floor_plan = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/button'
    floor_name = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/input'
    select_plan = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div/div/div/div/div[1]'
    search_plan = '//*[@id="react-select-4-input"]'
    select_plan1 = '//*[@id="react-select-4-option-41"]'
    select_plan2 = '//*[@id="react-select-4-option-36"]'
    select_plan3 = '//*[@id="react-select-4-option-28"]'
    remove_plan = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]'
    save_plan = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[3]/div/button[2]'
    add_plan = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/table/tbody/tr/td[3]/div'
    cancel_plan = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[3]/div/button[1]'
    delete_plan = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div'
    #Showing Hours Block
    hours_block = '//*[@id="application-settings-app"]/div/div/div[4]/div[1]/div[4]/div/div[2]'
    add_closure = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/a'
    reason_closure = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[1]/input'
    add_new_closure = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/button'
    part_time = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[3]/div[2]/div[1]'
    click_time1 = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[4]/div/div/div/div[1]'
    search_time1 = '//*[@id="react-select-5-input"]'
    select_time1 = '//*[@id="react-select-6-option-0"]'
    click_time2 = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[5]/div/div/div/div[1]'
    search_time2 = '//*[@id="react-select-9-input"]'
    select_time2 = '//*[@id="react-select-9-option-2"]'
    edit_closure = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[3]/div[2]/div[2]/div[1]'
    slots = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/div[3]/div[2]/input'
    save_slot = '//*[@id="application-settings-app"]/div/div/div[5]/div/div[2]/button'
    #API Keys Block
    api_block = '//*[@id="application-settings-app"]/div/div/div[4]/div[1]/div[5]/div'
    click_provider = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[2]/div/div/div/div[1]'
    search_provider = '//*[@id="react-select-10-input"]'
    select_provider = '//*[@id="react-select-10-option-0"]'
    api_keys = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[3]/div/div[2]/input'
    transaction_key = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[4]/div/div[2]/input'
    public_key = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[5]/div/div[2]/input'
    api_login = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[6]/div/div[2]/input'
    api_password = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[7]/div/div[2]/input'
    save_api = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[2]/div[8]/button'
    search_payscape = '//*[@id="react-select-11-input"]'
    provider_payscape = '//*[@id="react-select-11-option-1"]'
    cert = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div[3]/div/div[2]/input'
    term_id = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div[4]/div/div[2]/input'
    payscape_account = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div[5]/div/div[2]/input'
    payscape_login = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div[6]/div/div[2]/input'
    payscape_password = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div[7]/div/div[2]/input'
    save_payscape = '//*[@id="application-settings-app"]/div/div/div[4]/div[2]/div[4]/div[8]/button'











