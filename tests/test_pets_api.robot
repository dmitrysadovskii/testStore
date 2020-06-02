*** Settings ***
#Documentation    Suite description
Variables  ../config2/endpoints.yaml
Variables  ../config2/test_data.yaml

Library  ../storeLibrary/PetsLibrary.py  ${pets}  ${petsData}

*** Variables ***
${PET_STATUS}  ST49
${PET_NAME}    Kurt
${PET_NAME_UPDATED}    new_name

*** Test Cases ***
Test pets endpointes
    ${pets_id} =  create pets via api  ${PET_NAME}
    update pets name    ${pets_id}  ${PET_NAME_UPDATED}  ${PET_STATUS}
    update pets name with invalid data in json  45645645111111111145564565   Homies  500
    update pets name with invalid data in json  abs   Homies  500
    find pets    ${pets_id}  ${PET_NAME_UPDATED}  ${PET_STATUS}
    delete pets  ${pets_id}




*** Keywords ***
create pets via api
    [Arguments]    ${name}
    LOG  ${name}
    ${pets_id} =  add pets to store  ${name}
    add_pets_to_store_with_invalid_id
    [Return]  ${pets_id}

update pets name
    [Arguments]    ${pets_id}   ${name}  ${status}
    update pets name by id  ${pets_id}   ${name}  ${status}

update pets name with invalid data in json
    [Arguments]  ${pets_id}     ${name}   ${status_code}
    update_pets_name_with_invalid_data   ${pets_id}  ${name}   ${status_code}

find pets
    [Arguments]  ${pets_id}     ${name}     ${status}
    find_pets_by_status      ${pets_id}     ${name}     ${status}
    find_pets_by_id  ${pets_id}     ${name}
    find pets by invalid id  123435757375    404

delete pets
    [Arguments]  ${pets_id}
    delete pets by id  ${pets_id}



