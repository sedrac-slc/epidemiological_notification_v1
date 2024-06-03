const METHOD_UPDATE = "update";
const METHOD_DELETE = "delete";

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

const inputValueChange = (item, attrName) => {
    let index = item.dataset.index;
    modalForm.querySelector(`#${attrName}`).value = tableResponsive.querySelector(`#${attrName}-${index}`).innerHTML;
}

const selectValueChange = (item, attrName) => {
    let index = item.dataset.index;
    let select = modalForm.querySelector(`#${attrName}`);
    let value = tableResponsive.querySelector(`#${attrName}-${index}`).dataset.value;
    let children = select.childNodes;
    children.forEach(option => {
        if (option.value == value)  option.selected = true;
    });    
}

const modalHeaderBackgroudChange = (bgColor, textColor, text) => {
    const modalHeader = modalForm.querySelector(".modal-header");
    const modalTitle = modalHeader.querySelector(".modal-title");
    modalHeader.setAttribute("class", `modal-header ${bgColor}`)
    modalTitle.setAttribute("class", `modal-title fs-5 ${textColor}`);
    modalTitle.innerHTML = text;
}

const closedOrOpenFormControl = (isOpen) => {
    const formControl = modalForm.querySelectorAll(".form-control");
    if(isOpen){
        formControl.forEach((item) => { if(item.hasAttribute('disabled')) item.removeAttribute('disabled'); });
    }else{
        formControl.forEach((item) => { if(!item.hasAttribute('disabled')) item.setAttribute('disabled', true); });
    }
}

btnUpdate.forEach( item => {
    item.addEventListener('click', (e) => {
        modelChange(item)
        formChangeInputValues(item)
        closedOrOpenFormControl(true);
        modalHeaderBackgroudChange("bg-warning", "text-white", "Editar");
    })
})

btnDelete.forEach( item => {
    item.addEventListener('click', (e) => {
        modelChange(item)
        formChangeInputValues(item)
        closedOrOpenFormControl(false);
        modalHeaderBackgroudChange("bg-danger", "text-white", "Eliminar");
    })
})

buttonStoreModalCrudAction.addEventListener('click', (e) =>{
    const formControl = modalForm.querySelectorAll('.form-control');
    formControl.forEach((item) => item.value = "");
    actionChange(buttonStoreModalCrudAction)
    closedOrOpenFormControl(true);
    modalHeaderBackgroudChange("bg-none", "text-black", "Adicionar");
    if(typeof saveCrud === 'function') saveCrud(e.target)
})