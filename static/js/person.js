const hiddenChange = (attrName, value = "secret") => {
    const input = modalForm.querySelector(`#${attrName}`);
    const parent = input.parentElement
    if(!parent.classList.contains('d-none')) parent.classList.add('d-none')
}

const openChange = (attrName, value = "") => {
    const input = modalForm.querySelector(`#${attrName}`);
    const parent = input.parentElement
    if(parent.classList.contains('d-none')) parent.classList.remove('d-none')
}        

const saveCrud = (item) => {
    openChange('username')    
    openChange('password')
    openChange('confirm')
}

const formChangeInputValues = (item) => {

    inputValueChange(item, 'identityCardNumber')
    inputValueChange(item, 'fullname')
    inputValueChange(item, 'birthday')
    inputValueChange(item, 'phone')
    inputValueChange(item, 'email')

    selectValueChange(item, 'maritalStatus')
    selectValueChange(item, 'gender')
    
    if(item.dataset.method == METHOD_UPDATE || item.dataset.method == METHOD_DELETE) {
        hiddenChange('username')
        hiddenChange('password')
        hiddenChange('confirm')
    }

}
