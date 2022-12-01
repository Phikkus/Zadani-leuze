*** Settings ***
Documentation    Testing the content of the official product page of Leuze electronics
#   Importovani Knihoven tretich stran
Library    SeleniumLibrary
Library    XML
Library    DateTime


*** Variables ***

${wBase}    https://www.leuze.com/
${wTarget}    https://www.leuze.com/en-int/bcl-300i-sm-102-d-h/50116218?p=1
${prdctcls}    bcl300
${prdctname}    BCL 300i SM 102 D H
${brwsr}    Edge

*** Keywords ***
#   Definovani vlastnich keywordu
otevri base    Open Browser    ${wBase}    ${brwsr}
otevri targ    Open Browser    ${wTarget}    ${brwsr}
vypocet nacteni
    otevri targ
    ${t1}=     Get Current Date    result_format=timestamp
    Wait Until Element Is Visible    xpath:/html/body/main/div[2]/div/div/div[1]/div/div[2]/div[2]/img[6]
    ${t2}=     Get Current Date        result_format=timestamp
    ${time_delta}=    Subtract Date From Date    ${t2}    ${t1}    verbose
    Log To Console    \nCas nacteni je ${time_delta}


*** Test Cases ***
#   Start testovaciho programu
Open web check
    #   Kontrola otevreni webu dle zadaneho prohlizece
    otevri base

Search for bcl300
    #   Vyhledavani konkretniho elementu. Dle puvodniho zadani dle specifikace se melo vyhledavat trida produktu a pote vyhledat konkretni produkt. Nicmene z duvodu
    #   vytvoreni formulare hledanych produktu pomoci JavaScriptu neni mozne pouziti statickeho lokatoru
    Wait Until Page Contains Element    xpath: //*[@id="searchCollapse"]/div/form/div[1]/input
    Input Text    xpath: //*[@id="searchCollapse"]/div/form/div[1]/input    ${prdctname}
    Wait Until Page Contains Element   xpath: //*[@id="searchCollapse"]/div/form/div[1]/div/button
    Click Button    xpath: //*[@id="searchCollapse"]/div/form/div[1]/div/button
Product selection
    #   Vyber produktu
    Wait Until Element Is Visible    xpath:/html/body/main/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div/div[1]/a
    Click Element    xpath:/html/body/main/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div/div[1]/a
Figure can vary check
    #   Kontrola zda-li zvoleny produkt zminuje, ze cena se muze lisit
    otevri targ
    Element Should Contain    xpath: /html/body/main/div[2]/div/div/div[1]/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div/div[3]/div/figure/figcaption    Figure can vary

Icon Pressence
    #   Kontrola poctu ikon. Testuje se zda-li je vyobrazeno 6 ikon. Alternativne se da testovat zda-li jsou viditelne vsechny ikony individualne
    Wait Until Element Is Visible    class:single-selector-icon
    Page Should Contain Element    class:single-selector-icon    Page does not contain 6 icons    limit=6

Technical Features list
    #   Kontrola zda-li aktualni zvolena zalozka je "Technical Features"
    Sleep    0.3s
    Element Attribute Value Should Be    xpath://*[@id="technicalFeatures-tab"]    class    nav-link active product-detail-tab-navigation-link    Element neni viditelny!

Time required to load page
    #   Zvoleny test otevre novou instanci prohlizece a pokusi se vypocitat cas mezi zacatkem volani instance a nactenim nejvetsiho elementu stranky, ktery by se mel nacist jako posledni
    vypocet nacteni
