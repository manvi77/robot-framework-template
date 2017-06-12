*** Settings ***
Resource   ${PROJECTROOT}${/}resources${/}common.robot

*** Test cases ***

Example test
    Local keyword
    Shared keyword

*** Keywords ***
Local keyword
    [Documentation]    Keywords should only be promoted to resource file when
    ...                they are used in more than one place
    No operation
