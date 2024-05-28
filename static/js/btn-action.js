const btnUpdate = document.querySelectorAll('.btn-update');
const btnDelete = document.querySelectorAll('.btn-delete');
const modalForm = document.querySelector('#modalCrudAction');
const tableResponsive = document.querySelector('.table-responsive');
const buttonStoreModalCrudAction = document.querySelector('#buttonStoreModalCrudAction');

const actionChange = (item) => {
    modalForm.querySelector("form").action = item.dataset.action;
}

const modelChange = (item) => {
    actionChange(item);
    modalForm.querySelector("#model").value = item.dataset.model;
}

const valueChange = (item, attrName) => {
    let index = item.dataset.index;
    modalForm.querySelector(`#${attrName}`).value = tableResponsive.querySelector(`#${attrName}-${index}`).innerHTML;
}

btnUpdate.forEach( item => {
    item.addEventListener('click', (e) => {
        modelChange(item)
        formChangeInputValues(item)
    })
})

btnDelete.forEach( item => {
    item.addEventListener('click', (e) => {
        modelChange(item)
        formChangeInputValues(item)
    })
})

buttonStoreModalCrudAction.addEventListener('click', (e) =>{
    const formControl = modalForm.querySelectorAll('.form-control');
    formControl.forEach((item) => item.value = "");
    actionChange(buttonStoreModalCrudAction)
})