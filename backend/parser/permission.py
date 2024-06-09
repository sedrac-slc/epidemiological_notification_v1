
def createTablePlus(permissions, name, title = "Aicionar"):
    html = createRowsPlus(permissions, name)
    return f"""<table class="table table-hover">
                <thead> <th class='text-center'>{title}</th> <th>Código</th>  </thead>
                <tbody>{html}</tbody>
            </table>"""

def createRowsPlus(permissions, name):
    return ''.join([f"""<tr>
        <td class='text-center'><input class="form-check-input border border-primary" type="checkbox" name="{name}" value={i.id}  id="checkPermission{i.id}"/> </td>
        <td><label class="form-label" for="checkPermission{i.id}">{i.name}</label></td>
    </tr>""" for i in permissions])